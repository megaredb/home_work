import math
from tkinter import Tk, Label
from PIL import Image, ImageTk
from cairo import *


class Gui(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        w, h = 350, 270

        self.geometry("{}x{}".format(w, h))

        with Image.open("hor_lines.png") as im:
            im.thumbnail((330, 330), Image.ANTIALIAS)
            im.save("hor_line_rotated.png", "PNG")
        self.ims = ImageSurface.create_from_png("hor_line_rotated.png")
        self.surface = ImageSurface(FORMAT_RGB24, w, h)
        self.context = Context(self.surface)

        ctx = self.context

        self.last_x, self.last_y = 100, 100
        self.last_width, self.last_height = 100, 100
        for i in range(5):
            ctx.rectangle(self.last_x, self.last_y, self.last_width, self.last_height)
            ctx.set_source_rgb(1, 1, 1)
            ctx.fill_extents()
            ctx.set_source_rgb(0, 0, 0)
            ctx.stroke()

            self.last_x += 10
            self.last_y += 10
            self.last_width -= 20
            self.last_height -= 20

        self._image_ref = ImageTk.PhotoImage(Image.frombuffer("RGBA", (w, h), self.surface.get_data(), "raw", "RGBA",0,1))

        self.label = Label(self, image=self._image_ref, text='df', font=('Arial', 53))
        self.label.pack(expand=True, fill="both")

        self.mainloop()


if __name__ == "__main__":
    Gui()
