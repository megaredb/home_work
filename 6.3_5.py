from tkinter import *

root = Tk()

root.geometry('300x130')

def label_update():
    try:
        result = float(a.get()) + float(b.get()) - float(c.get()) / (float(a.get()) - 2*float(b.get()))
        label.configure(text='Результат: ' + str(result))
    except ZeroDivisionError:
        label.configure(text='Деление на ноль невозможно.')
    except Exception:
        label.configure(text='')
    finally:
        root.after(1, label_update)

label = Label(text='Результат отсутствует.')
a_label = Label(text='a =')
b_label = Label(text='b =')
c_label = Label(text='c =')
v1 = StringVar(value=1)
v2 = StringVar(value=1)
v3 = StringVar(value=1)
a = Entry(textvariable=v1, justify='center')
b = Entry(textvariable=v2, justify='center')
c = Entry(textvariable=v3, justify='center')
label_update()

label.grid(row=0, column=2)
a_label.grid(row=1, column=0, sticky="w")
b_label.grid(row=2, column=0, sticky="w")
c_label.grid(row=3, column=0, sticky="w")
a.grid(row=1,column=1, padx=5, pady=5)
b.grid(row=2,column=1, padx=5, pady=5)
c.grid(row=3,column=1, padx=5, pady=5)

root.mainloop()
