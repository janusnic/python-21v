#!/usr/bin/python
# -*- coding: utf-8 -*-
'''Класс Frame (фрейм) - Элемент,
содержащий в себе другие графические элементы управления.
'''
# импортирование модулей python
from Tkinter import *
import tkFont


class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"

    def __init__(self, master=None):
        Frame.__init__(self, master, height=300, width=300)
        var = StringVar()
        helv30 = tkFont.Font(family="Helvetica", size=30, weight="bold")
        message = Label(master, textvariable=var, fg='red', font=helv30)
        var.set('Hello There, Everyone!')
        message.pack(side=BOTTOM)
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
