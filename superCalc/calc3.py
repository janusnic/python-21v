# -*- coding:utf-8 -*-
# ---------- CALCULATOR ----------
'''
 Program make a simple calculator that can add,
 subtract, multiply and divide using functions
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
    def helloCallBack(self):
        tkMessageBox.showinfo("Hello Python", "Simple Calculator")

    def click(self, key):
        self.entry.insert(END, key)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        btn_list = [
          '7',  '8',  '9',  '*',  'C',
          '4',  '5',  '6',  '/',  'M->',
          '1',  '2',  '3',  '-',  '->M',
          '0',  '.',  '=',  '+',  'neg'
          ]
        # create all buttons with a loop
        r = 1
        c = 0
        for b in btn_list:
            rel = RIDGE
            cmd = lambda x=b: self.click(x)
            Button(master, text=b, width=5, relief=rel, command=cmd).grid(row=r, column=c)
            c += 1
            if c > 4:
                c = 0
                r += 1

        # use Entry widget for an editable display
        self.entry = Entry(master, width=33, bg="yellow")
        self.entry.grid(row=0, column=0, columnspan=5)


def main():
    # Создать приложение
    app = Application()
    # Вызов методов класса менеджера окон (Wm)
    app.master.title("Super Calculator")
    app.master.maxsize(1000, 400)
    # Запуск программы
    app.mainloop()


if __name__ == '__main__':
    main()
