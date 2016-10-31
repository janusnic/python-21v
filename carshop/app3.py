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
        labels = ('make', 'model', 'year', 'wheels', 'mileage', 'sold_on')
        data = [
            ('Ford', 'Rodeo', 2014, 4, 10000, 1),
            ('Toyota', 'Camry CE (Classic Edition)', 2011, 4, 17000, 0),
            ('Toyota', 'Camry LE (Luxury Edition)', 2013, 4, 20000, 1),
            ('Toyota', 'Camry', 2000, 4, 12000, 0),
            ('Ford', 'Rodeo', 2014, 4, 10000, 0),
          ]
        j = 0
        for txt in labels:
            l = Label(text='%s' % txt, relief=RIDGE)
            l.grid(row=0, column=j, sticky=NSEW)
            j += 1

        for i in range(len(data)):
            cols = []
            j = 0
            for d in data[i]:
                e = Entry(relief=RIDGE)
                e.grid(row=i+1, column=j, sticky=NSEW)
                e.insert(END, d)
                j += 1

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
