import math
from tkinter import Tk, Label
from PIL import Image, ImageTk
from cairo import *


class Gui(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        w, h = 550, 550

        self.geometry("{}x{}".format(w, h))

        self.surface = ImageSurface(FORMAT_RGB24, w, h)
        self.context = Context(self.surface)
        self.ims = ImageSurface.create_from_png("bg_grass.png")

        ctx = self.context

        ctx.rectangle(0, 0, w, h)
        ctx.set_source_rgb(1, 0.7, 0)
        ctx.fill()

        ctx.set_source_surface(self.ims, 0, 300)
        ctx.paint()

        ctx.arc(400, 100, 45, 0, 2 * math.pi)
        ctx.set_source_rgb(0.1, 1, 1)
        ctx.fill_preserve()
        ctx.set_line_width(0.5)
        ctx.set_source_rgb(0, 0, 0)
        ctx.stroke()

        ctx.rectangle(100, 200, 180, 200)
        ctx.set_source_rgb(0.15, 0.2, 0.4)
        ctx.fill()

        ctx.move_to(195, 80)
        ctx.line_to(80, 200)
        ctx.line_to(300, 200)
        ctx.set_source_rgb(0, 0.2, 0.4)
        ctx.fill()

        self._image_ref = ImageTk.PhotoImage(Image.frombuffer("RGBA", (w, h), self.surface.get_data(), "raw", "RGBA",0,1))

        self.label = Label(self, image=self._image_ref, text='df', font=('Arial', 53))
        self.label.pack(expand=True, fill="both")

        self.mainloop()


if __name__ == "__main__":
    Gui()
