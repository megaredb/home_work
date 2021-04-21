from tkinter import *

root = Tk()
root.geometry('350x250')


def doFirstExercise():
    try:
        h = float(start_water_level.get())
        p = float(plus_percent.get())
        n = int(hours.get())
        for i in range(n):
            h += h * p / 100
        h = round(h, 3)
        result.configure(text='I: Уровень воды через {0} часов будет {1} метров.'.format(n, h))
    except ValueError:
        result.configure(text='Ошибка: не все поля заполнены верно.')


def doSecondExercise():
    try:
        h = float(start_water_level.get())
        p = float(plus_percent.get())
        k = float(finish_water_level.get())
        n = 0
        while h <= k:
            h += h * p / 100
            n += 1
        result.configure(text='II: Уровень воды {0} метров будет достигнут через {1} часов.'.format(k, n))
    except ValueError:
        result.configure(text='Ошибка: не все поля заполнены верно.')


def doThirdExercise():
    try:
        start_water_level.delete(0, END)
        plus_percent.delete(0, END)
        hours.delete(0, END)
        finish_water_level.delete(0, END)
        if 'II' in str(result.cget('text')):
            result.configure(text='Здесь будет выведен результат.')
    except ValueError:
        result.configure(text='Ошибка: не все поля заполнены верно.')


frame_up = Frame()
left_frame = LabelFrame(frame_up, text='Ввод')
right_frame = LabelFrame(frame_up, text='Обработка')

bottom_frame = Frame()
result_frame = LabelFrame(bottom_frame, text='Результаты')

# ВВОД #
start_water_level = Entry(left_frame)
plus_percent = Entry(left_frame)
hours = Entry(left_frame)
finish_water_level = Entry(left_frame)

# НАДПИСИ #
result = Label(result_frame, text='Здесь будет выведен результат.')
h_level = Label(left_frame, text='h =')
p_percent = Label(left_frame, text='p =')
n_hours = Label(left_frame, text='n =')
k_level = Label(left_frame, text='k =')

# КНОПКИ #
first_exercise = Button(right_frame, text='Задание 1', command=doFirstExercise)
second_exercise = Button(right_frame, text='Задание 2', command=doSecondExercise)
third_exercise = Button(right_frame, text='Задание 3', command=doThirdExercise)

# УПАКОВКА #
frame_up.pack()
bottom_frame.pack()

left_frame.pack(side=LEFT, padx=5, pady=10)
right_frame.pack(side=RIGHT, padx=5, pady=10)
result_frame.pack(side=BOTTOM, padx=5, pady=10)

h_level.grid(row=0, column=0, padx=3, pady=1)
start_water_level.grid(row=0, column=1, padx=3, pady=1)
p_percent.grid(row=1, column=0, padx=3, pady=1)
plus_percent.grid(row=1, column=1, padx=3, pady=1)
n_hours.grid(row=2, column=0, padx=3, pady=1)
hours.grid(row=2, column=1, padx=3, pady=1)
k_level.grid(row=3, column=0, padx=3, pady=1)
finish_water_level.grid(row=3, column=1, padx=3, pady=1)

first_exercise.grid(row=0, column=0, padx=3, pady=1)
second_exercise.grid(row=1, column=0, padx=3, pady=1)
third_exercise.grid(row=2, column=0, padx=3, pady=1)

result.pack()

root.mainloop()
