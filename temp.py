from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter.ttk import Radiobutton
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import Menu
def clicked():
    res = "Привет {}".format(txt.get())
    lbl.configure(text=res)

def clicked1():
    lbl.configure(text=selected.get())

def clicked2():
    messagebox.showinfo('Заголовок', 'Текст0')
    messagebox.showwarning('Заголовок', 'Текст1')  # показывает предупреждающее сообщение
    messagebox.showerror('Заголовок', 'Текст2')  # показывает сообщение об ошибке
    res = messagebox.askquestion('Заголовок', 'askquestion')
    res = messagebox.askyesno('Заголовок', 'askyesno')
    res = messagebox.askyesnocancel('Заголовок', 'askyesnocancel')
    res = messagebox.askokcancel('Заголовок', 'askokcancel')
    res = messagebox.askretrycancel('Заголовок', 'askretrycancel')

'''
window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
lbl = Label(window, text="Привет")
lbl.grid(column=0, row=0)
txt = Entry(window, width=10)
txt.grid(column=1, row=0)
txt.focus()
btn = Button(window, text="Клик!", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
combo = Combobox(window)
combo['values'] = (1, 2, 3, 4, 5, "Текст")
combo.current(1)  # установите вариант по умолчанию
combo.grid(column=0, row=0)
window.mainloop()

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
chk_state = BooleanVar()
chk_state.set(True)  # задайте проверку состояния чекбокса
chk = Checkbutton(window, text='Выбрать', var=chk_state)
chk.grid(column=0, row=0)
window.mainloop()

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
selected = IntVar()
rad1 = Radiobutton(window,text='Первый', value=1, variable=selected)
rad2 = Radiobutton(window,text='Второй', value=2, variable=selected)
rad3 = Radiobutton(window,text='Третий', value=3, variable=selected)
btn = Button(window, text="Клик", command=clicked1)
lbl = Label(window)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
btn.grid(column=3, row=0)
lbl.grid(column=0, row=1)
window.mainloop()

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
txt = scrolledtext.ScrolledText(window, width=30, height=10)
txt.grid(column=0, row=0)
txt.insert(INSERT, 'Текстовое поле')
# txt.delete(1.0, END)  # мы передали координаты очистки
window.mainloop()

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
btn = Button(window, text='Клик', command=clicked2)
btn.grid(column=0, row=0)
window.mainloop()

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
var = IntVar()
var.set(36)
spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var)
# spin = Spinbox(window, values=(3, 8, 11), width=5)
spin.grid(column=0, row=0)
window.mainloop()

'''

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='black')


'''
window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
menu = Menu(window)
new_item = Menu(menu)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label='Новый')
new_item.add_separator()
new_item.add_command(label='Изменить')
menu.add_cascade(label='Файл', menu=new_item)
window.config(menu=menu)
new_item.add_command(label='Новый', command=clicked)
window.mainloop()

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Первая')
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Вторая')
lbl1 = Label(tab1, text= 'Во тута отодвинуто ...', padx=10, pady=10)
lbl1.grid(column=0, row=0)
lbl2 = Label(tab2, text='Вкладка 2')
lbl2.grid(column=0, row=0)
tab_control.pack(expand=2, fill='both')
window.mainloop()
'''