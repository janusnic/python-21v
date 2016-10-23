#!/usr/bin/python
# -*- coding: utf-8 -*-
'''создает пустое окно 200x150 с названием "создание окна",
    расположенное в центре экрана.
'''
# импортирование модулей python
from Tkinter import *

# создание окна
root = Tk()
root.title('создание окна')
root.geometry('400x250+300+225')

# вывод окна на экран
root.mainloop()
