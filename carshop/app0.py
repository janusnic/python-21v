# -*- coding:utf-8 -*-
# ---------- Cars Shop ----------
'''
 Program make a simple Cars Shop
'''
# импортирование модулей python
try:
    # for Python2
    from Tkinter import *   # notice capitalized T in Tkinter
    import tkFont
    import tkMessageBox
except ImportError:
    # for Python3
    from tkinter import *   # notice lowercase 't' in tkinter here
    from tkinter import font
    from tkinter import messagebox


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self._init_gridbox()

    def _init_gridbox(self):
        for i in range(5):
            for j in range(4):
                l = Label(text='%d.%d' % (i, j), relief=RIDGE)
                l.grid(row=i, column=j, sticky=NSEW)

    def about(self):
        tkMessageBox.showinfo("Old Cars Shop", "Old Cars Shop")


def main():
    # Создать приложение
    app = Application()
    # Вызов методов класса менеджера окон (Wm)
    app.master.title("Old Cars Shop")
    app.master.maxsize(1000, 400)
    # Запуск программы
    app.mainloop()


if __name__ == '__main__':
    main()
