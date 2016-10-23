#!/usr/bin/python
# -*- coding: utf-8 -*-
'''создает пустое окно 200x150 с названием "создание окна",
    расположенное в центре экрана.
'''
# импортирование модулей python
import Tkinter as tk


class Main(object):

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()


def main():
    # создание окна
    root = tk.Tk()
    root.geometry('400x250+300+225')
    root.title('создание окна')

    app = Main(root)
    # вывод окна на экран
    root.mainloop()

if __name__ == '__main__':
    main()
