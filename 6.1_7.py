from tkinter import *

root = Tk()
root.geometry('100x100')

def every_tick():
    try:
        result.configure(text='Результат: ' + str((3 * float(a.get()) - 2 * float(b.get()) * float(c.get())))
        root.after(1, every_tick)
    except:
        root.after(1, every_tick)

def validate(action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed:
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False

vcmd = (root.register(validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
a = Entry(root, validate = 'key', validatecommand = vcmd)
b = Entry(root, validate = 'key', validatecommand = vcmd)
c = Entry(root, validate = 'key', validatecommand = vcmd)
result = Label(text='Результат: 0')
every_tick()
a.pack()
b.pack()
c.pack
result.pack()


root.mainloop()
