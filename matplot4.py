import math
from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
from cairo import *


class Gui(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.w, self.h = 700, 450

        self.title('#7 стр. 228')
        # Фреймы

        self.img_frame = LabelFrame(self, text='Изображение')
        self.options_frame = LabelFrame(self, text='Настройки')

        # Поля

        self.list_of_shapes = Combobox(self.options_frame, values=['Квадрат',
                                                                   'Круг',
                                                                   'Треугольник'])
        self.list_of_shapes.current(0)

        # Кнопки

        self.change_shape = Button(self.options_frame, text='Сменить фигуру', command=self._draw_shapes)

        # Флажки

        self.is_lw_checked = BooleanVar()
        self.is_color_checked = BooleanVar()
        self.is_fill_style_checked = BooleanVar()

        self.line_width = Checkbutton(self.options_frame, text='Толщина обводки - 4.',
                                      var=self.is_lw_checked)
        self.color = Checkbutton(self.options_frame, text='Цвет заливки - зелёный.',
                                 var=self.is_color_checked)
        self.fill_style = Checkbutton(self.options_frame, text='Заливка - диаг. линии.',
                                      var=self.is_fill_style_checked)

        # Отрисовка фигур
        with Image.open("hor_lines.png") as im:
            im.thumbnail((512, 512), Image.ANTIALIAS)
            im = im.rotate(45)
            im.save("hor_line_rotated.png", "PNG")
        self.ims = ImageSurface.create_from_png("hor_line_rotated.png")
        self.geometry("{}x{}".format(self.w, self.h + 100))
        self.surface = ImageSurface(FORMAT_RGB24, 350, 350)
        self.context = Context(self.surface)

        # Упаковка
        self.img_frame.pack(expand=True, fill="both", side=TOP)
        self.options_frame.pack(expand=True, fill="both", side=BOTTOM)

        self._image_ref = ImageTk.PhotoImage(
            Image.frombuffer("RGBA", (350, 350), self.surface.get_data(), "raw", "RGBA", 0, 1))
        self.img = Label(self.img_frame, image=self._image_ref)
        self.img.pack()
        self.list_of_shapes.grid(row=1, column=0)
        self.change_shape.grid(row=2, column=0)
        self.line_width.grid(row=0, column=1)
        self.color.grid(row=1, column=1)
        self.fill_style.grid(row=2, column=1)
        self.mainloop()

    def _draw_shapes(self):
        self.surface = ImageSurface(FORMAT_RGB24, 350, 350)
        self.context = Context(self.surface)
        ctx = self.context
        if self.list_of_shapes.current() == 0:
            ctx.rectangle(100, 100, 100, 100)
        elif self.list_of_shapes.current() == 1:
            ctx.arc(175, 175, 45, 0, 2 * math.pi)
        else:
            ctx.move_to(165, 30)
            ctx.line_to(90, 200)
            ctx.line_to(240, 200)

        if self.is_color_checked.get():
            ctx.set_source_rgb(0, 0.8, 0.5)
        else:
            ctx.set_source_rgb(0, 0.7, 1)

        if self.is_lw_checked.get():
            ctx.set_line_width(4)
        else:
            ctx.set_line_width(1)

        if not self.is_fill_style_checked.get():
            ctx.fill_preserve()
            ctx.set_source_rgb(0, 0, 0)
            ctx.stroke()
        else:
            ctx.clip()
            ctx.mask_surface(self.ims, -200, -200)

        self._image_ref = ImageTk.PhotoImage(
            Image.frombuffer("RGBA", (350, 350), self.surface.get_data(), "raw", "RGBA", 0, 1))
        self.img.config(image=self._image_ref)


if __name__ == "__main__":
    Gui()
