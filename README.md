# python-21v unit 08
# Основы Tkinter
Tkinter - это интерфейс Python к GUI-инструментарию Tk.

Tkinter был разработан Стином Лумхольтом (Steen Lumholt) и Гвидо ван Россумом.
Tk был создан Джоном Остерхутом (John Ousterhout), работавшим в ту пору в Беркли.

# Tkinter Виджеты
Tkinter предоставляет различные элементы управления, такие как кнопки, метки и текстовые поля, используемые в приложениях с графическим интерфейсом. Эти элементы управления обычно называют виджетов.

## Есть 15 типов виджетов в Tkinter.
кнопка
   Кнопка виджет используется для отображения кнопок в вашем приложении.

холст
   Canvas виджет используется для рисования фигур, таких как линии, овалы, многоугольники и прямоугольники, в вашем приложении.

Checkbutton
   Виджет Checkbutton используется для отображения ряда опций, как флажки. Пользователь может выбрать несколько вариантов одновременно.

запись
   Запись виджет используется для отображения текстового поля в одну строку для приема значения от пользователя.

Рамка
   Виджет Рама используется в качестве контейнера виджета, чтобы организовать другие виджеты.

метка
   Виджет Ярлык используется для обеспечения однострочный заголовок для других виджетов. Он также может содержать изображения.

Listbox
   Listbox виджет используется для предоставления списка опций пользователю.

кнопку MENU
   Виджет кнопку MENU используется для отображения меню в приложении.

Меню
   Виджет меню используется для предоставления различных команд пользователю. Эти команды содержатся внутри кнопку MENU.

Сообщение
   Виджет сообщений используется для отображения многострочных текстовых полей для приема значений от пользователя.

Переключатель
   Виджет RadioButton используется для отображения ряда опций, как радио-кнопок. Пользователь может выбрать только один вариант одновременно.

Масштаб
   Шкала виджет используется для обеспечения слайдера виджет.

Полоса прокрутки
   Виджет Scrollbar используется для добавления прокрутки возможность различных виджетов, таких как списков.

Текст
   Текстовый виджет используется для отображения текста в нескольких строках.

Верхний уровень
   Toplevel виджет используется для обеспечения отдельного контейнера окна.

со счётчиком
   Виджет со счётчиком представляет собой вариант стандартного ввода Tkinter виджета, который может быть использован для выбора из фиксированного числа значений.

PanedWindow
   PanedWindow является контейнером виджет, который может содержать любое количество панелей, расположенных по горизонтали или по вертикали.

LabelFrame
   Labelframe простой контейнер виджет. Его основная цель состоит в том, чтобы действовать в качестве прокладки или контейнера для сложных оконных раскладок.

tkMessageBox
   Этот модуль используется для отображения окон сообщений в приложениях.

## Стандартные атрибуты
   Габаритные размеры
   Цвета
   шрифты
   Якоря
   стили Рельефные
   Bitmaps
   курсоры

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

## Создание окна window_01.py
        #!/usr/bin/python
        # -*- coding: utf-8 -*-
        '''
        создает пустое окно 200x150 с названием "создание окна",
        расположенное в центре экрана.
        '''
        # импортирование модулей python
        from Tkinter import *

        #создание окна
        root = Tk()
        root.title('создание окна')
        root.geometry('200x150+300+225')

        # вывод окна на экран
        root.mainloop()

        #!/usr/bin/python
С этой строки начинается всякий исполняемый модуль Python в Linux. Символ # используется в Python для комментариев, так что интерпретатор строчку проигнорирует. Но в bash это не комментарий, и данная строка будет прочитана. В ней содержатся путь к интерпретатору python и указание исполнить код, записанный на Python. Такие инструкции называют "the pound bang" ["Pound" - "фунт" - так часто называют знак "#". "Bang" - сленговое название восклицательного знака "!".], и их ставят в каждой программе на первой строке.

    # импортирование модулей python
    from Tkinter import *
Данная строка загружает в Python весь модуль Tkinter целиком. В результате у Python появляется библиотека для построения оконного интерфейса.

    # создание окна
    root = Tk()
    root.title('myWindow')
    root.geometry('200x150+300+225')
Tk() - это функция Tkinter, открывающая главное окно любого приложения. Здесь мы создаем экземпляр с именем root. Это общая черта всех классов Tkinter - они должны быть присвоены какой-либо переменной. В следующих двух командах задаются некоторые свойства root, определяющие заголовок и размеры окна. Это другой общий факт - взаимодействие с объектами Tkinter происходит через задание свойств [и вызов методов]. '200x150+300+225' означает [ширина x высота + координата_x_верхнего_левого_угла + координата_y_верхнего_левого_угла].

    # запуск окна
    root.mainloop()
Наконец, в этой строке происходит вызов метода Tk() под названием mainloop(), который держит окно раскрытым, пока оно не будет закрыто нажатием кнопки [x] на окне или вызовом метода Tk() destroy().

##  Экземпляры классов - это объекты, обладающие свойствами и методами.
Python - это объектно-ориентированный язык программирования. Tk() и Toplevel() являются классами Tkinter, принимающими форму объектов для создания на экране графических окон. Программирование на Tkinter подразумевает комбинирование и преобразование встроенных классов Tkinter в новые классы с индивидуальными свойствами и методами.

### Общее для всех виджетов
Все виджеты в Tkinter обладают некоторыми общими свойствами. Виджеты создаются вызовом конструктора соответствующего класса. Первый аргумент (как правило неименованный, но можно использовать имя master) это родительский виджет, в который будет упакован (помещён) наш виджет. Родительский виджет можно не указывать, в таком случае будет использовано главное окно приложения. Далее следуют именованные аргументы, конфигурирующие виджет. Это может быть используемый шрифт (font=...), цвет виджета (bg=...), команда, выполняющаяся при активации виджета (command=...) и т.д. Полный список всех аргументов можно посмотреть в man options и man-странице соответствующего виджета (например man button, см. разделы "STANDARD OPTIONS" и "WIDGET-SPECIFIC OPTIONS").

## Создание окна window_02.py
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


# Класс Frame (фрейм)
Элемент, содержащий в себе другие графические элементы управления.
Виджет Frame (рамка) предназначен для организации виджетов внутри окна.

        from Tkinter import *
        root=Tk()
        # Свойство bd отвечает за толщину края рамки.
        frame1=Frame(root,bg='green',bd=5)
        frame2=Frame(root,bg='red',bd=5)
        button1=Button(frame1,text=u'Первая кнопка')
        button2=Button(frame2,text=u'Вторая кнопка')
        frame1.pack()
        frame2.pack()
        button1.pack()
        button2.pack()
        root.mainloop()

### Опции
Используются в качестве ключевых слов - аргументов при конструировании элементов управления или совместно с методами их настройки.

        height
        width

        class Application(Frame):
            def __init__(self, master=None):
                Frame.__init__(self, master, height=300, width=300)
                self.pack()

Frame (рамка) - хороший инструмент для организации остальных виджет в группы внутри окна, а также оформления.

                from tkinter import *

                root = Tk()

                fra1 = Frame(root,width=500,height=100,bg="darkred")
                fra2 = Frame(root,width=300,height=200,bg="green",bd=20)
                fra3 = Frame(root,width=500,height=150,bg="darkblue")

                fra1.pack()
                fra2.pack()
                fra3.pack()

                root.mainloop()

Данный скрипт создает три фрейма разного размера. Свойство bd (сокращение от boderwidth) определяет расстояния от края рамки до заключенных в нее виджетов (если они есть).

На фреймах также можно размещать виджеты как на основном окне (root). Здесь текстовое поле находится на рамке fra2.

                ent1 = Entry(fra2,width=20)
                ent1.pack()

# Управление геометрией
Все виджеты TkInter имеют доступ к конкретным методам управления геометрией, которые имеют целью организации виджетов по всей области виджета родителя. Tkinter предоставляет следующие геометрии менеджера классов: упаковка, сетки, и место.
packer() - Менеджер геометрии организует виджеты в блоки перед помещением их в родительский виджет.

# Упаковщик (packer)
Упаковщик (менеджер геометрии, менеджер расположения) это специальный механизм, который размещает (упаковывает) виджеты на окне. В Tkinter есть три упаковщика: pack, place, grid. Обратите внимание, что в одном виджете можно использовать только один тип упаковки, при смешивании разных типов упаковки программа, скорее всего, не будет работать.

Упаковщик pack() является самым интеллектуальным (и самым непредсказуемым). При использовании этого упаковщика с помощью свойства side нужно указать к какой стороне родительского виджета он должен примыкать. Как правило этот упаковщик используют для размещения виджетов друг за другом (слева направо или сверху вниз). Пример:

        from tkinter import *
        root=Tk()
        button1 = Button(text="1")
        button2 = Button(text="2")
        button3 = Button(text="3")
        button4 = Button(text="4")
        button5 = Button(text="5")
        button1.pack(side='left')
        button2.pack(side='top')
        button3.pack(side='left')
        button4.pack(side='bottom')
        button5.pack(side='right')
        root.mainloop()

Для создания сложной структуры с использованием этого упаковщика обычно используют Frame, вложенные друг в друга.

### Аргументы
При применении этого упаковщика можно указать следующие аргументы:

    side ("left"/"right"/"top"/"bottom") - к какой стороне должен примыкать размещаемый виджет.
    fill (None/"x"/"y"/"both") - необходимо ли расширять пространство предоставляемое виджету.
    expand (True/False) - необходимо ли расширять сам виджет, чтобы он занял всё предоставляемое ему пространство.
    in_ - явное указание в какой родительский виджет должен быть помещён.

### Дополнительные функции
Кроме основной функции у виджетов есть дополнительные методы для работы с упаковщиками.

    pack_configure - синоним для pack.
    pack_slaves (синоним slaves) - возвращает список всех дочерних упакованных виджетов.
    pack_info - возвращает информацию о конфигурации упаковки.
    pack_propagate (синоним propagate) (True/False) - включает/отключает распространении информации о геометрии дочерних виджетов. По умолчанию виджет изменяет свой размер в соответствии с размером своих потомков. Этот метод может отключить такое поведение (pack_propagate(False)). Это может быть полезно, если необходимо, чтобы виджет имел фиксированный размер и не изменял его по прихоти потомков.[7]
    pack_forget (синоним forget) - удаляет виджет и всю информацию о его расположении из упаковщика. Позднее этот виджет может быть снова размещён.

Диспетчеры компоновки применяются для задания относительного взаиморасположения элементов управления внутри контейнера - их общего родителя. Упаковщику достаточно качественного описания взаимного расположения - above (над), to the left of (слева от), filling (заливка) и т.д., - на основании которого находится точное местоположение элемента.

Размер любого родительского элемента управления определяется размером находящихся внутри него "дочерних" элементов. Упаковщик контролирует, где в родительском элементе управления появится дочерний элемент, упаковываемый внутри своего родителя. Элементы управления можно упаковать во фреймы, а эти фреймы - в другие фреймы, ради того чтобы получить желаемую компоновку. Кроме того, полученная компоновка уже после упаковки динамически корректируется, отслеживая все изменения конфигурации.

Обратите внимание, что элементы управления не появятся на экране, пока диспетчер компоновки не задаст их геометрию. Графический элемент управления обретает право на существование, только когда к нему применят, например, метод упаковщика pack().

Метод pack() может вызываться с парами ключевое слово-опция/значение, контролирующими расположение элемента управления внутри контейнера и его поведение при изменении размеров окна основного приложения.

## Метки Класс Label (метка)
Метки (или надписи) — это достаточно простые виджеты, содержащие строку (или несколько строк) текста и служащие в основном для информирования пользователя.

    lab = Label(root, text="Это метка! \n Из двух строк.", font="Arial 18")
### Опции
Используются в качестве ключевых слов - аргументов при конструировании элементов управления или совместно с методами их настройки.
        class Application(Frame):
            def __init__(self, master=None):
                Frame.__init__(self, master)
                var = StringVar()

                message = Label(master, textvariable=var)
                var.set('Hello There, Everyone!')
                message.pack() #по умолчанию side = "top"
                self.pack()

## Объединение переменных графических элементов управления
Текущее значение некоторых элементов управления (таких как элементы, предназначенные для ввода текста) с помощью специальных опций может быть напрямую связано с переменными приложения. Вот эти опции: variable (переменная), textvariable (текстовая переменная), onvalue (включить+значение), offvalue (выключить+значение) и value (значение). Связь получается двусторонней: если переменная по какой-либо причине изменяется, связанный с ней элемент управления также соответствующим образом изменится.

Уже существует довольно много полезных подклассов Variable: StringVar, IntVar, DoubleVar и BooleanVar. Чтобы считать текущее значение такой переменной, скажем myval, нужно применить к ней метод get(), а изменить значение переменной можно с помощью метода set(). Если следовать данному соглашению, графический элемент управления будет всегда отслеживать значение указанной переменной уже без вашей помощи.

                Например:
                class App(Frame):
                    def __init__(self, master=None):
                        Frame.__init__(self, master)
                        self.pack()

                        self.entrythingy = Entry()
                        self.entrythingy.pack()

                        self.button.pack()
                        # Создается переменная приложения
                        self.contents = StringVar()
                        # Ей присваивается некоторое значение
                        self.contents.set("this is a variable")
                        # Элемент для ввода текста начинает
                        # отслеживать значение переменной
                        self.entrythingy["textvariable"] = self.contents

                        # Когда пользователь нажимает клавишу "Enter",
                        # происходит обратный вызов,
                        # и программа начинает выводить на экран
                        # значение переменной приложения.
                        self.entrythingy.bind('<Key-Return>',
                				      self.print_contents)

                    def print_contents(self, event):
                        print "hi. contents of entry is now ---->",
                		      self.contents.get()

### Опции упаковщика
        anchor
            Вид указателя. Обозначает, где упаковщик должен размещать каждый дочерний элемент.
        expand (развертывать)
            Логическое выражение, 0 или 1
                             message.pack(expand = 1)
        fill (заполнять)
            Допустимые значения: "x", "y", "both" (оба), "none" (ни один).
        ipadx и ipady
            Расстояние, указывающее, какой промежуток должен оставаться внутри у каждой стороны дочернего элемента управления.
        padx и pady
            Расстояние, указывающее, какой промежуток должен оставаться извне у каждой стороны дочернего элемента управления.
        side (сторона)
            Допустимые значения: "left" (слева), "right" (справа), "top" (наверху), "bottom" (внизу). "Внутренние" элементы управления (дочерние) упаковываются как можно ближе к заданной стороне внешнего элемента (родителя).
                        BOTTOM
                            message.pack(side=BOTTOM)

## Шрифты object Fonts
Простые Кортеж шрифты
В качестве кортежа, первый элемент которого семейство шрифта, а затем размер в точках, за которым может следовать строка, содержащая один или несколько модификаторов типа жирный, курсив, подчеркивание и Overstrike.

    ( "Helvetica", "16") для 16-балльной Helvetica регулярно.

    ( "Таймс", "24", "жирный текст") для 24-балльной Таймс выделены жирным курсивом.

Вы можете создать "шрифт объекта" путем импорта модуля tkFont и с помощью его конструктора класса Font

        import tkFont
        font = tkFont.Font ( option, ... )

Вот список опций:

    Семейство: имя шрифта семьи в виде строки.

    Размер: Высота шрифта как целое число в пунктах.Чтобы получить шрифт N пикселей высокий, используйте -n.

    вес: "смелый" для жирным шрифтом, "нормальный" для регулярного веса.

    наклонная: "наклонным" для курсива, "романо" для unslanted.

    Подчеркиваю: 1 для подчеркнутого текста, 0 для обычных.

    Повторноенажатие: 1 для overstruck текста, 0 для нормальной.

пример

    helv36 = tkFont.Font(family="Helvetica",size=36,weight="bold")
    text.configure(font=("Times New Roman", 12, "bold"))

    try:
        # python 2
        from tkFont import Font
    except ImportError
        # python 3
        from tkinter.font import Font

    myFont = tkFont.Font(family="Times New Roman", size=12)
    text.configure(font=myFont)

    myFont.configure(size=14)

Есть ли способ изменить Tkinter виджета и стиля шрифта, не зная виджета семейство и размер шрифта?

Мы создаем пользовательский интерфейс с помощью стандартного Tkinter виджеты (Метка, Вступление, Text, и др.). А наше приложение запускается мы хотим, чтобы динамически изменять шрифт, стиль этих виджетов для смелых и/или курсивом (.config() метод.

    # Note: Neither of these examples work!
    widget.config( font='bold' )

    -OR-

    widget.config( font=( None, None, 'bold' ) )

        import tkFont
        font = tkFont.Font ( option, ... )

Here is the list of options:

    family: The font family name as a string.
    size: The font height as an integer in points. To get a font n pixels high, use -n.
    weight: "bold" for boldface, "normal" for regular weight.
    slant: "italic" for italic, "roman" for unslanted.
    underline: 1 for underlined text, 0 for normal.
    overstrike: 1 for overstruck text, 0 for normal.


        from Tkinter import *
        import tkFont

        class Application(Frame):

            def __init__(self, master=None):
                Frame.__init__(self, master, height=300, width=300)
                var = StringVar()
                helv30 = tkFont.Font(family="Helvetica", size=30, weight="bold")
                message = Label(master, textvariable=var, fg='red', font=helv30)
                var.set('Hello There, Everyone!')
                message.pack()
                self.pack()

## Color options
    You can use a string specifying the proportion of red, green and blue in hexadecimal digits. For example, "#fff" is white, "#000000" is black, "#000fff000" is pure green, and "#00ffff" is pure cyan (green plus blue).

    You can also use any locally defined standard color name. The colors "white", "black", "red", "green", "blue", "cyan", "yellow", and "magenta" will always be available.

#  Менеджер окон
В Tk имеется полезная команда, Wm, для организации взаимодействия с менеджером окон. Опции команды wm позволяют управлять заголовками, расположением, картинками на иконках и т.п. В Tkinter эти команды реализованы в виде методов класса Wm. Элементы управления Toplevel ведут свое происхождение от класса Wm и поэтому могут напрямую обращаться к методам Wm.

Для того чтобы получить окно верхнего уровня, содержащее нужный элемент управления, часто достаточно сослаться на его родительский элемент. Конечно, если заданный элемент управления уже упакован внутри фрейма, его родитель не будет окном верхнего уровня. Получить окно верхнего уровня с произвольным элементом управления можно, вызвав метод _root(). Название метода начинается с символа подчеркивания; это показывает, что настоящая функция является частью реализации, а не интерфейсом к функциональности Tk.

## Менеджер окон window_04.py                    
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
# Класс Button (кнопка)
Командная кнопка.

        from Tkinter import *
        def button_clicked():
            print (u"Клик!")
        root=Tk()
        # кнопка по умолчанию
        button1 = Button()
        button1.pack()
        # кнопка с указанием родительского виджета и несколькими аргументами
        button2 = Button(root, bg="red", text=u"Кликни меня!", command=button_clicked)
        button2.pack()
        root.mainloop()

Виджет Button - самая обыкновенная кнопка, которая используется в тысячах программ. Пример кода:

    from Tkinter import *
    root=Tk()
    button1=Button(root,text='ok',width=25,height=5,bg='black',fg='red',font='arial 14')
    button1.pack()
    root.mainloop()

За создание окна отвечает класс Tk(), и первым делом нужно создать экземпляр этого класса. Этот экземпляр принято называть root, хотя вы можете назвать его как угодно. Далее создаётся кнопка, при этом мы указываем её свойства (начинать нужно с указания окна, в примере - root). Здесь перечислены некоторые из них:

    text - какой текст будет отображён на кнопке (в примере - ок)
    width,height - соответственно, ширина и длина кнопки.
    bg - цвет кнопки (сокращенно от background, в примере цвет - чёрный)
    fg - цвет текста на кнопке (сокращённо от foreground, в примере цвет - красный)
    font - шрифт и его размер (в примере - arial, размер - 14)

Далее, нашу кнопку необходимо разместить на окне. Для этого, в Tkinter используются специальные упаковщики( pack(), place(), grid() ).

Код self.button = tk.Button(self.master, text = 'myButton') связывает элемент управления Button() с классом main [все элементы управления кроме Tk() кому-нибудь "принадлежат"], а text = 'myButton' задает значение свойства text [текст, который отобразится на кнопке во время исполнения программы].

Строка self.button.pack(side = tk.BOTTOM) определяет, в какой части окна появится наша кнопка - эта кнопка пока ничего не делает.

## Создание Button window_05.py
        class Application(Frame):
            def __init__(self, master=None):
                Frame.__init__(self, master, height=300, width=300)
                var = StringVar()
                helv30 = tkFont.Font(family="Helvetica", size=30, weight="bold")
                self.message = Label(master, textvariable=var, fg='red', font=helv30)
                var.set('Hello There, Everyone!')
                self.message.pack(side=BOTTOM)
                self.button = Button(master, text='myButton')
                self.button.pack(side=TOP)
                self.pack()

## Задание опций
Опции определяют такие вещи, как цвет или толщина рамки элемента управления. Задавать опции можно тремя способами:

Во время создания объекта с помощью ключевых слов-аргументов:
                    self.button = Button(self, fg = "red", bg = "blue")
После создания объекта, рассматривая название опции как индекс словаря:

        def __init__(self, master=None):
            Frame.__init__(self, master, height=300, width=300)
            var = StringVar()
            helv30 = tkFont.Font(family="Helvetica", size=30, weight="bold")
            self.message = Label(master, textvariable=var, fg='red', font=helv30)
            var.set('Hello There, Everyone!')
            self.message.pack(side=BOTTOM)
            self.button = Button(master, text='myButton', fg='red', bg='white')
            self.button["activebackground"] = "red"
            self.button["activeforeground"] = "white"
            self.button.pack(side=TOP)
            self.pack()

После создания объекта, изменяя значения атрибутов при помощи метода config():
                    self.button.config(fg = "red", bg = "blue")

Некоторые опции нельзя применять по отношению к определенным элементам управления. Ответ на вопрос, имеет ли данный элемент управления ту или иную опцию, зависит от класса этого элемента управления; у кнопок есть опция "command" ("команда"), у меток - нет.

(Некоторые опции, такие как bg, являются синонимами обычных опций с длинными названиями (bg это сокращение для background - "фон"). В случае опции с сокращенным названием метод config() возвратит не 5 кортежей, а только 2, причем в них будет содержаться полное имя "настоящей" опции-синонима (bg, background).)

Любая кнопка должна что-нибудь делать. В данном случае мы свяжем событие "нажатие кнопки" с выводом сообщкеия 'Hello There!' в поле entry. Для этого в класс main вводится метод helloCallBack.
        import tkMessageBox
        def helloCallBack(self):
            tkMessageBox.showinfo("Hello Python", "Hello World")

Метод - это то, что класс main делает, а не то, чем класс main является...

                self.button = Button(master, text ="Hello", command=self.helloCallBack, fg='red', bg='white')

Обращение к helloCallBack содержит self. Это означает, что метод helloCallBack является внутренним по отношению к main.

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
                self.button = Button(master, text ="Hello", command=self.helloCallBack, fg='red', bg='white')
                self.button["activebackground"] = "red"
                self.button["activeforeground"] = "white"
                self.button.pack(side=TOP)
                self.pack()

## Relief styles
                FLAT
                RAISED
                SUNKEN
                GROOVE
                RIDGE

### bottomframe into Frame

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

## Создание окна window_05.py
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
# Управление геометрией
## Geometry Management grid

Метод grid() - Менеджер геометрии организует виджеты в табличном структуры родительского виджета. Этот упаковщик представляет собой таблицу с ячейками, в которые помещаются виджеты.

Аргументы

    row - номер строки, в который помещаем виджет.
    rowspan - сколько строк занимает виджет
    column - номер столбца, в который помещаем виджет.
    columnspan - сколько столбцов занимает виджет.
    padx / pady - размер внешней границы (бордюра) по горизонтали и вертикали.
    ipadx / ipady - размер внутренней границы (бордюра) по горизонтали и вертикали. Разница между pad и ipad в том, что при указании pad расширяется свободное пространство, а при ipad расширяется помещаемый виджет.
    sticky ("n", "s", "e", "w" или их комбинация) - указывает к какой границе "приклеивать" виджет. Позволяет расширять виджет в указанном направлении. Границы названы в соответствии со сторонами света. "n" (север) - верхняя граница, "s" (юг) - нижняя, "w" (запад) - левая, "e" (восток) - правая.
    in_ - явное указание в какой родительский виджет должен быть помещён.

Для каждого виджета указываем, в какой он находится строке, и в каком столбце. Если нужно, указываем, сколько ячеек он занимает (если, например, нам нужно разместить три виджета под одним, необходимо "растянуть" верхний на три ячейки). Пример:

    entry1.grid(row=0,column=0,columnspan=3)
    button1.grid(row=1,column=0)
    button2.grid(row=1,column=1)
    button3.grid(row=1,column=2)

Дополнительные функции

    grid_configure - синоним для grid.
    grid_slaves (синоним slaves) - см. pack_slaves.
    grid_info - см. pack_info.
    grid_propagate (синоним propagate) - см. pack_propagate.
    grid_forget (синоним forget) - см. pack_forget.
    grid_remove - удаляет виджет из-под управления упаковщиком, но сохраняет информацию об упаковке. Этот метод удобно использовать для временного удаления виджета (см. пример в описании метода destroy).
    grid_bbox (синоним bbox) - возвращает координаты (в пикселях) указанных столбцов и строк.[9]
    grid_location (синоним location) - принимает два аргумента: x и y (в пикселях). Возвращает номер строки и столбца в которые попадают указанные координаты, либо -1 если координаты попали вне виджета.
    grid_size (синоним size) - возвращает размер таблицы в строках и столбцах.
    grid_columnconfigure (синоним columnconfigure) и grid_rowconfigure (синоним rowconfigure) - важные функции для конфигурирования упаковщика. Методы принимают номер строки/столбца и аргументы конфигурации. Список возможных аргументов:
        minsize - минимальная ширина/высота строки/столбца.
        weight - "вес" строки/столбца при увеличении размера виджета. 0 означает, что строка/столбец не будет расширяться. Строка/столбец с "весом" равным 2 будет расширяться вдвое быстрее, чем с весом 1.
        uniform - объединение строк/столбцов в группы. Строки/столбцы имеющие одинаковый параметр uniform будут расширяться строго в соответствии со своим весом.
        pad - размер бордюра. Указывает, сколько пространства будет добавлено к самому большому виджету в строке/столбце.

Пример, текстовый виджет с двумя полосами прокрутки:

        from Tkinter import *
        root=Tk()
        text = Text(wrap=NONE)
        vscrollbar = Scrollbar(orient='vert', command=text.yview)
        text['yscrollcommand'] = vscrollbar.set
        hscrollbar = Scrollbar(orient='hor', command=text.xview)
        text['xscrollcommand'] = hscrollbar.set
        # размещаем виджеты
        text.grid(row=0, column=0, sticky='nsew')
        vscrollbar.grid(row=0, column=1, sticky='ns')
        hscrollbar.grid(row=1, column=0, sticky='ew')
        # конфигурируем упаковщик, чтобы текстовый виджет расширялся
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        root.mainloop()

Example
        import Tkinter
        root = Tkinter.Tk(  )
        for r in range(3):
            for c in range(4):
                Tkinter.Label(root, text='R%s/C%s'%(r,c),
                    borderwidth=1 ).grid(row=r,column=c)
        root.mainloop(  )

# calc1.py
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

            def cmd(self):
                pass

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
                    Button(master, text=b, width=5, relief=rel, command=self.cmd).grid(row=r, column=c)
                    c += 1
                    if c > 4:
                        c = 0
                        r += 1

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
            # (*)
# Класс Entry (ввод)
Поле для ввода текста.
Entry - это виджет, позволяющий пользователю ввести одну строку текста. Имеет дополнительное свойство bd (сокращённо от borderwidth), позволяющее регулировать ширину границы.

    borderwidth - ширина бордюра элемента
    bd - сокращение от borderwidth
    width - задаёт длину элемента в знакоместах.
    show - задает отображаемый символ.
# Text
Text - это виджет, который позволяет пользователю ввести любое количество текста. Имеет дополнительное свойство wrap, отвечающее за перенос (чтобы, например, переносить по словам, нужно использовать значение WORD).Например:

    from Tkinter import *
    root=Tk()
    text1=Text(root,height=7,width=7,font='Arial 14',wrap=WORD)
    text1.pack()
    root.mainloop()

Методы insert, delete и get добавляют, удаляют или извлекают текcт. Первый аргумент - место вставки в виде 'x.y', где x – это строка, а y – столбец. Например:

    text1.insert(1.0,'Добавить Текст\n\ в начало первой строки')
    text1.delete('1.0', END)   # Удалить все
    text1.get('1.0', END)      # Извлечь все


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
                Button(master, text=b, width=5, relief=rel, command=self.cmd).grid(row=r, column=c)
                c += 1
                if c > 4:
                    c = 0
                    r += 1

            # use Entry widget for an editable display (*)
            entry = Entry(master, width=33, bg="yellow")
            entry.grid(row=0, column=0, columnspan=5)

# calc2.py
            class Application(Frame):
                def helloCallBack(self):
                    tkMessageBox.showinfo("Hello Python", "Simple Calculator")

                def cmd(self):
                    self.entry.insert(END, 'Hello Button')

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
                        Button(master, text=b, width=5, relief=rel, command=self.cmd).grid(row=r, column=c)
                        c += 1
                        if c > 4:
                            c = 0
                            r += 1

                    # use Entry widget for an editable display
                    self.entry = Entry(master, width=33, bg="yellow")
                    self.entry.grid(row=0, column=0, columnspan=5)
