from tkinter import *

root = Tk()
root.geometry('560x300')
root.title('Площади прямоугольников.')

frame = Frame()
f_left = LabelFrame(frame, text="Прямоугольник 1")
f_right = LabelFrame(frame, text="Прямоугольник 2")

frame_down = Frame()
f_down = LabelFrame(frame_down, text="Результаты")


# ФУНКЦИИ #

def areaCompare():
    try:
        area_a = float(width_a.get()) * float(height_a.get())
        area_b = float(width_b.get()) * float(height_b.get())
        result.configure(text='Площадь 1 = ' + str(area_a) + "\n" +
                              'Площадь 2 = ' + str(area_b) + "\n")
        if area_a > area_b:
            result.configure(text=str(result.cget('text')) + 'Площадь 1 больше, чем площадь 2.')
        elif area_b > area_a:
            result.configure(text=str(result.cget('text')) + 'Площадь 2 больше, чем площадь 1.')
        else:
            result.configure(text=str(result.cget('text')) + 'Площади равны.')
    except ValueError:
        result.configure(text='Ошибка. Не все параметры указаны верно.')


def rectIsSquareCheck():
    try:
        value = selrect.get()
        if value == 0:
            if float(width_a.get()) != float(height_a.get()):
                result.configure(text='Прямоугольник 1 не является квадратом.')
            else:
                result.configure(text='Прямоугольник 1 является квадратом.')
        else:
            if float(width_b.get()) != float(height_b.get()):
                result.configure(text='Прямоугольник 2 не является квадратом.')
            else:
                result.configure(text='Прямоугольник 2 является квадратом.')
    except ValueError:
        result.configure(text='Ошибка. Не все параметры указаны верно.')


def fitsCheck():
    try:
        value = selrect.get()
        if value == 0:
            if float(width_a.get()) < float(width_b.get()) and float(height_a.get()) < float(height_b.get()):
                result.configure(text='Прямоугольник 1 поместится в прямоугольнике 2.')
            else:
                result.configure(text='Прямоугольник 1 не поместится в прямоугольнике 2.')
        else:
            if float(width_a.get()) > float(width_b.get()) and float(height_a.get()) > float(height_b.get()):
                result.configure(text='Прямоугольник 2 поместится в прямоугольнике 1.')
            else:
                result.configure(text='Прямоугольник 2 не поместится в прямоугольнике 1.')

    except ValueError:
        result.configure(text='Ошибка. Не все параметры указаны верно.')


# ВВОД #

width_a = Entry(f_left)
height_a = Entry(f_left)
width_b = Entry(f_right)
height_b = Entry(f_right)

# ТЕКСТ #
label_wa = Label(f_left, text='a =')
label_ha = Label(f_left, text='b =')

label_wb = Label(f_right, text='a =')
label_hb = Label(f_right, text='b =')
result = Label(f_down, text='В этом месте будет результат.')

# ГАЛОЧКИ #

selrect = IntVar()
selectRect1 = Radiobutton(f_left, text='Прямоугольник 1', variable=selrect, value=0)
selectRect2 = Radiobutton(f_right, text='Прямоугольник 2', variable=selrect, value=1)

# КНОПКИ #

get_area_comparison = Button(f_down, text='Сравнить площади', command=areaCompare, width=23)
is_it_square = Button(f_down, text='Проверить на квадрат', command=rectIsSquareCheck, width=23)
fitsButton = Button(f_down, text='Проверить, поместится ли', command=fitsCheck, width=23)

# УПАКОВКА #
frame.pack()
frame_down.pack()
f_left.pack(side=LEFT, padx=5, pady=10)
f_right.pack(side=RIGHT, padx=5, pady=10)
f_down.pack(side=BOTTOM, padx=5, pady=10)

selectRect1.grid(row=2, column=0, padx=3, pady=1)
label_wa.grid(row=0, column=0, padx=3, pady=1)
label_ha.grid(row=1, column=0, padx=3, pady=1)
width_a.grid(row=0, column=1, padx=3, pady=1)
height_a.grid(row=1, column=1, padx=3, pady=1)

selectRect2.grid(row=2, column=0, padx=3, pady=1)
label_wb.grid(row=0, column=0, padx=3, pady=1)
label_hb.grid(row=1, column=0, padx=3, pady=1)
width_b.grid(row=0, column=1, padx=3, pady=1)
height_b.grid(row=1, column=1, padx=3, pady=1)

get_area_comparison.grid(row=0, column=0, padx=3, pady=1)
is_it_square.grid(row=1, column=0, padx=3, pady=1)
fitsButton.grid(row=2, column=0, padx=3, pady=1)
result.grid(row=0, column=1, padx=3, pady=1)

root.mainloop()
