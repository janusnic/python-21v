# python-21v unit 09
# Lambda в Python
Выражение (statement) lambda в Python - это анонимная или несвязанная функция.

Выражение lambda создает функцию, которая будет вызываться позднее, но в отличие от инструкции def, выражение возвращает функцию, а не связывает ее с именем.

lambda - анонимны, то есть без имени. На практике они часто используются, как способ получить встроенную функцию  или отложить выполнение  фрагмента программного кода.

    lambda argument1, argument2,... argumentN : выражение, использующее аргументы

## Различия lambda от def:
- lambda – это выражение, а не инструкция. По этой причине ключевое слово lambda  может  появляться там, где синтаксис  языка  Python не позволяет использовать инструкцию def, – внутри литералов или в вызовах функций, например.

- Тело  lambda – это не блок инструкций, а единственное выражение.  Тело
lambda-выражения сродни тому, что вы помещаете в инструкцию return внутри определения def, – вы просто вводите результат в виде выражения вместо  его явного  возврата.

Типичный пример, как выглядит нормальная функция, а затем - ее lambda-эквивалент:
### Без выражения lambda:
    import math
    #----------------------------------------------------------------------
    def sqroot(x):
        """
        Извлекает квадратный корень из числа на входе
        """
        return math.sqrt(x)
### С выражением lambda:
    square_rt = lambda x: math.sqrt(x)
### Без выражения lambda:
     def func(x, y, z): return x + y + z
     func(2, 3, 4)
### С выражением lambda:
     f = lambda x, y, z: x + y + z
     f(2, 3, 4)

## Использование значений по умолчанию в lambda-выражениях:
     x = (lambda a=”fee”, b=”fie”, c=”foe”: a + b + c)
     x(“wee”)

Те же самые правила поиска переменных в областях видимости, что и для вложенных инструкций def:
## lambda-выражения
создают локальную область видимости, как и вложенные инструкции def, и автоматически получают доступ к именам в объемлющих функциях, в модуле
и во встроенной области видимости (в соответствии с правилом LEGB).
     def knights():
         title = ‘Sir’
         action = (lambda x: title + ‘ ‘ + x) # Заголовок в объемлющей def
         return action                        # Возвращает функцию

     act = knights()
     act(‘robin’)

Когда можно использовать lambda-выражения:
- Для создания таблиц переходов, которые представляют собой списки или словари действий, выполняемых по требованию.
Например:
    L = [lambda x: x**2,   # Встроенные определения функций
        lambda x: x**3,
        lambda x: x**4]   # Список из трех функций

    for f in L:
       print(f(2))        # Выведет 4, 8, 16

    print(L[0](3))         # Выведет 9

Тот же пример без использования lambda:
    def f1(x): return x ** 2
    def f2(x): return x ** 3   # Определения именованных функций
    def f3(x): return x ** 4

    L = [f1, f2, f3]           # Ссылка по имени

    for f in L:
       print(f(2))            # Выведет 4, 8, 16

    print(L[0](3))             # Выведет 9

Подобные таблицы действий в языке Python можно создавать с помощью словарей и других структур данных.
Пример, выполненный в интерактивном сеансе:
 key = ‘got’
 {‘already’: (lambda: 2 + 2),
...  ‘got’:     (lambda: 2 * 4),
...  ‘one’:     (lambda: 2 ** 6)}[key]()


Тот же пример без использования lambda:
 def f1(): return 2 + 2
...
 def f2(): return 2 * 4
...
 def f3(): return 2 ** 6
...
 key = ‘one’
 {‘already’: f1, ‘got’: f2, ‘one’: f3}[key]()
64


Так же возможна реализация логики выбора внутри lambda-функций:
 lower = (lambda x, y: x if x < y else y)
 lower(‘bb’, ‘aa’)
‘aa’
 lower(‘aa’, ‘bb’)
‘aa’


Если необходимо выполнить цикл внутри lambda, то можно использовать map и генераторы списков:
Пример №1
 import sys
 showall = lambda x: list(map(sys.stdout.write, x))
                                   # Функция list
                                   # необходима в 3.0
 t = showall([‘spam\n’, ‘toast\n’, ‘eggs\n’])
spam
toast
eggs

Пример №2
 showall = lambda x: [sys.stdout.write(line) for line in x]
 t = showall((‘bright\n’, ‘side\n’, ‘of\n’, ‘life\n’))
bright
side
of
life


Вложенные lambda-выражения и области видимости:
Соблюдается правило LEGB.
Например, lambda-выражение находится внутри  инструкции  def – типичный  случай – и  потому  получает значение имени x из области видимости объемлющей функции, имевшееся на момент ее вызова:
 def action(x):
...     return (lambda y: x + y) # Создать и вернуть ф-цию,
...                              # запомнить x
 act = action(99)
 act
<function <lambda> at 0x00A16A88>
 act(2)         # Вызвать функцию, созданную ф-цией action
101

Предыдущая инструкция def в виде lambda-выражения:
 action = (lambda x: (lambda y: x + y))
 act = action(99)
 act(3)
102
 ((lambda x: (lambda y: x + y))(99))(4)
103
Эта  структура  lambda-выражений  создает функцию,  которая при  вызове создает  другую функцию. В обоих случаях вложенное  lambda-выражение имеет доступ к переменной x в объемлющем lambda-выражении.

# обратные вызовы (callbacks)
Один из основных участков в Python, где lambda используется регулярно,- это обратные вызовы (callbacks) Tkinter.

# Tkinter + lambda
простой сценарий с тремя кнопками, две из которых связаны с их обработчиком событий посредством lambda:

        import Tkinter as tk
        ############################################
        class App:
            """"""
            #------------------------------------------------------------------
            def __init__(self, parent):
                """Конструктор"""
                frame = tk.Frame(parent)

                frame.pack()

                btn22 = tk.Button(frame, text="22", command=lambda: self.printNum(22))

                btn22.pack(side=tk.LEFT)
                btn44 = tk.Button(frame, text="44", command=lambda: self.printNum(44))

                btn44.pack(side=tk.LEFT)

                quitBtn = tk.Button(frame, text="QUIT", fg="red", command=frame.quit)

                quitBtn.pack(side=tk.LEFT)

            #------------------------------------------------------------------
            def printNum(self, num):
                """"""
                print "You pressed the %s button" % num

        if __name__ == "__main__":
            root = tk.Tk()
            app = App(root)
            root.mainloop()

Мы создаем экземпляр tk.Button и привязываем его к нашему методу printNum. Lambda присваивается параметру command этой кнопки. Это значит, что мы создаем для этой команды одноразовую функцию, подобно как в кнопке выхода вызывается метод quit для frame. Разница здесь в том, что данная lambda есть метод, вызывающий другой метод и передающий в последний целое число. Метод printNum печатает на стандартном выводе, какая кнопка была нажата, используя информацию, переданную ему функцией lambda.

## calc3.py
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
            # use Entry widget for an editable display (*)
            self.entry = Entry(master, width=33, bg="yellow")
            self.entry.grid(row=0, column=0, columnspan=5)

Tkinter предоставляет два виджета, позволяющие пользователю вводить текст: Entry – поле ввода в одну строку и Text – многострочное поле ввода.
Методы insert, delete и get добавляют, удаляют или извлекают текcт.

новый объект Entry:
            entry = Entry(text='Текст по умолчанию.')

Опция text позволяет вам поместить текст в это поле уже после его создания, а метод get возвращает содержимое объекта Entry (которое могло быть уже изменено пользователем):
            entry.get() 'Текст по умолчанию.'

Метод insert помещает текст в виджет Entry:
            entry.insert(END, 'Строка текста.')
END это специальный индекс, который означает последний символ в виджете

Метод get читает текст в виджете. В качестве аргументов он принимает начальный и конечный индексы.
            self.txt = self.entry.get()[:-1]

Метод delete удаляет текст из виджета. Следующий пример удаляет весь текст, кроме первых двух символов:
            self.entry.delete(0, END)

## виджет Text:
            text = Text(width=100, height=5)
Параметры width иheight задают размеры виджета в символах и строках соответственно.

Метод insert помещает текст в виджет Text:
            text.insert(END, 'Строка текста.')
END это специальный индекс, который означает последний символ в виджете Text.

Вы можете также задавать положение символов при помощи точечной записи, например, 1.1, где число до точки означает номер строки, а число после – номер колонки. Следующий пример добавляет буквы 'nother' первого символа первой строки:
            text.insert(1.1, 'nother')

Метод get читает текст в виджете. В качестве аргументов он принимает начальный и конечный индексы. Следующий пример возвращает весь текст виджета, включая символ новой строки:
            text.get(0.0, END)
            'Другая строка текста.\n'

Метод delete удаляет текст из виджета. Следующий пример удаляет весь текст, кроме первых двух символов:
            text.delete(1.2, END)
            text.get(0.0, END)

### clear entry
            def click(self, key):
                self.entry.insert(END, key)

                def click(self, key):
                    self.entry.insert(END, key)
                    if key == 'C':
                        # clear entry
                        self.txt = self.entry.get()[:-1]
                        self.entry.delete(0, END)
                        self.entry.insert(0, self.txt[:-1])
                    elif key == 'AC':
                        self.entry.delete(0, END)  # clear all entry

## calc4.py
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
                if key == 'C':
                    # clear entry
                    self.txt = self.entry.get()[:-1]
                    self.entry.delete(0, END)
                    self.entry.insert(0, self.txt[:-1])
                elif key == 'AC':
                    self.entry.delete(0, END)  # clear all entry

            def __init__(self, master=None):
                Frame.__init__(self, master)
                btn_list = [
                  '7',  '8',  '9',  '*', '%',  'M',
                  '4',  '5',  '6',  '÷', '√ ', 'MS',
                  '1',  '2',  '3',  '-',  'x²', 'MR',
                  '0',  '.',  '=',  '+',  '-x', 'MC'
                  ]
                # create all buttons with a loop
                r = 1
                c = 0
                for b in btn_list:
                    rel = RIDGE
                    cmd = lambda x=b: self.click(x)
                    Button(master, text=b, width=5, relief=rel, command=cmd).grid(row=r, column=c)
                    c += 1
                    if c > 5:
                        c = 0
                        r += 1
                # use Entry widget for an editable display
                self.entry = Entry(master, width=33, bg="yellow")
                self.entry.grid(row=0, column=0, columnspan=5)

                Button(master, text='C', width=3, command=lambda x='C': self.click(x)).grid(row=0, column=4)
                Button(master, text='AC', width=3, command=lambda x='AC': self.click(x)).grid(row=0, column=5)

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
