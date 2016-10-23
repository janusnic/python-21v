#!/usr/bin/python
# -*- coding: utf-8 -*-
'''Класс Frame (фрейм) - Элемент,
содержащий в себе другие графические элементы управления.
'''
# импортирование модулей python
from Tkinter import *
import tkFont
import tkMessageBox


class Application(Frame):
    def helloCallBack(self):
        tkMessageBox.showinfo("Hello Python", "Hello World")

    def __init__(self, master=None):
        Frame.__init__(self, master, height=300, width=300)
        var = StringVar()
        helv30 = tkFont.Font(family="Helvetica", size=30, weight="bold")
        self.message = Label(master, textvariable=var, fg='red', font=helv30)
        var.set('Hello There, Everyone!')
        self.message.pack(side=BOTTOM)
        self.button = Button(master, text="Hello", command=self.helloCallBack, fg='red', bg='white')
        self.button["activebackground"] = "red"
        self.button["activeforeground"] = "white"
        self.button.pack(side=TOP)

        bottomframe = Frame(master)
        bottomframe.pack(side=BOTTOM)

        redbutton = Button(bottomframe, text="Red FLAT", fg="red", relief=FLAT)
        redbutton.pack(side=LEFT)

        greenbutton = Button(bottomframe, text="Brown RAISED", fg="brown", relief=RAISED)
        greenbutton.pack(side=LEFT)

        bluebutton = Button(bottomframe, text="Blue SUNKEN", fg="blue", relief=SUNKEN)
        bluebutton.pack(side=LEFT)

        magentabutton = Button(bottomframe, text="Magenta GROOVE", fg="magenta", relief=GROOVE)
        magentabutton.pack(side=LEFT)

        blackbutton = Button(bottomframe, text="Black RIDGE", fg="black", relief=RIDGE)
        blackbutton.pack(side=BOTTOM)

        self.pack()


def main():
    # Создать приложение
    app = Application()
    # Вызов методов класса менеджера окон (Wm)
    app.master.title("My TkInter Wm Application")
    app.master.maxsize(1000, 400)
    # Запуск программы
    app.mainloop()


if __name__ == '__main__':
    main()
