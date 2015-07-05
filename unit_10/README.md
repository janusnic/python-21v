# Исключения в Питоне
# Errors
<pre>
def fetcher(obj, index):
	return obj[index]

x = 'spam'
fetcher(x, 3)           # Like x[3] 'm'

fetcher(x, 4)

Traceback (most recent call last):
File "<stdin>", line 1, in ?
File "<stdin>", line 2, in fetcher
IndexError: string index out of range

try:
    fetcher(x, 4)
except IndexError:
    print 'got exception' # got exception

def catcher():
    try:
        fetcher(x, 4)
    except IndexError:
        print 'got exception'
    print 'continuing'

catcher() # got exception continuing
</stdin>
# Исключения
Исключения свидетельствуют об ошибках и прерывают нормальный ход выполнения программы. Исключения возбуждаются с помощью инструкции raise. В общем случае инструкция raise имеет следующий вид: 
raise Exception([value]), где Exception – тип исключения, а value – необязательное значение с дополнительной информацией об исключении. 
<pre>
Например:
raise RuntimeError(“Неустранимая ошибка”)


Перехватить исключение можно с помощью инструкций try и except:

class Bad(Exception): pass

def doomed(): raise Bad()

try:
    doomed()
except Bad:
    print 'got Bad'

# got Bad

</pre>
Если инструкция raise используется без дополнительных параметров, она повторно возбуждает последнее исключение (однако такой прием работает только в процессе обработки возникшего исключения).
Рассмотрим простейший пример: открытие файла. Если всё нормально — open(filename, 'r') возвращает объект этого самого файла Если файл не может быть открыт — выбрасывается исключение:
<pre>
try:
    f = open(filename, 'r')
    try:
        print(f.read())
    finally:
        f.close()
except OSError as ex:
    print("Cannot process file", filename, ": Error is", ex)
</pre>
Обратите внимание: файл нужно не только открыть но и закрыть после использования. Исключение может выбросить open (например, если файла нет на диске или нет прав на его чтение).
<pre>
Traceback (most recent call last):
  File "fopen.py", line 5, in <module>
    f = open (filename, 'r')
IOError: [Errno 2] No such file or directory: 'file.txt'
</module>
Если файл открыт — читаем его через f.read(). Этот вызов тоже может выбросить исключение, но файл закрывать всё равно нужно. Поэтому необходим блок finally: f.close() должен быть вызван даже если f.read() сломался. 

Исключения из обоих мест попадут в except OSError, где можно будет что-то сделать с ошибкой.
Питон делает явный выбор в пользу исключений перед возвратом кода ошибки в своём ядре и стандартной библиотеке. 

<pre>
Типы исключений
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      </pre>
Самый базовый класс — BaseException. Он и его простые потомки (SystemExit, KeyboardInterrupt,GeneratorExit) не предназначены для перехвата обыкновенным программистом — только Питон и редкие библиотеки должны работать с этими типами. Нарушение правила ведет, например, к тому что программу невозможно корректно завершить.
Также не нужно перехватывать все исключения:
<pre>
try:
    ...
except:
    ...
работает как

try:
    ...
except BaseException:
    ...

Всё, что может быть нужно программисту — это Exception и унаследованные от него классы.

лучше ловить как можно более конкретные классы исключений

import os

filename = 'file.txt'
try:
    f = open (filename, 'r')
    try:
        print f.read()
    finally:
        f.close()
except (os.error, IOError) as ex:
    print "Cannot process file", filename, ": Error is", ex
</pre>
нструкция finally служит для реализации завершающих действий, сопутствующих операциям, выполняемым в блоке try. Например:
<pre>
f = open(‘foo’,’r’)
try:
    # Выполнить некоторые действия

finally:
    f.close()
    # Файл будет закрыт, независимо от того, что произойдет
</pre>
Блок finally не используется для обработки ошибок. Он используется для реализации действий, которые должны выполняться всегда, независимо от того, возникла ошибка или нет. Если в блоке try исключений не возникло, блок finally будет выполнен сразу же вcлед за ним. Если возникло исключение, управление сначала будет передано первой инструкции в блоке finally, а затем это исключение будет возбуждено повторно, чтобы обеспечить возможность его обработки в другом обработчике.
<pre>
def fetcher(obj, index):
	return obj[index]

x = 'spam'
fetcher(x, 3)           # Like x[3] 'm'

try:
    fetcher(x, 3)
finally:
    print 'after fetch'


fetcher(x, 3)
print 'after fetch'

# KeyboardInterrupt.

while True:
    try:
        x = int(input("Введите, пожалуйста, число: "))
        break
    except ValueError:
        print("Ой!  Это некорректное число.  Попробуйте ещё раз...")
</pre>
# Оператор try работает следующим образом:
В начале исполняется блок try (операторы между ключевыми словами try и except).<br>
Если при этом не появляется исключений, блок except не выполняется и оператор try заканчивает работу.<br>
Если во время выполнения блока try было возбуждено какое-либо исключение, оставшаяся часть блока не выполняется. <br>Затем, если тип этого исключения совпадает с исключением, указанным после ключевого слова except, выполняется блок except, а по его завершению выполнение продолжается сразу после оператора try-except.<br>
Если порождается исключение, не совпадающее по типу с указанным в блоке except — оно передаётся внешним операторам try; если ни одного обработчика не найдено, исключение считается необработанным (unhandled exception), и выполнение полностью останавливается и выводится сообщение.
<br>
Оператор try может иметь более одного блока except
<pre>
except (RuntimeError, TypeError, NameError):
    pass


# необязательный блок else

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('не могу открыть', arg)
    else:
        print(arg, 'содержит', len(f.readlines()), 'строк')
        f.close()
# Исключения, определённые пользователем

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print('Поймано моё исключение со значением:', e.value)

Поймано моё исключение со значением: 4

raise MyError('ой!')
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
__main__.MyError: 'ой!'

</stdin>
При создании модуля, который может породить различные ошибки, обычной практикой будет создание базового класса для исключений, определённых в этом модуле, и подклассов для различных ошибочных состояний:
<pre>
class Error(Exception):
    """Базовый класс для всех исключений в этом модуле."""
    pass
 
class InputError(Error):
    """Исключение порождается при ошибках при вводе.
     Атрибуты:
        expression -- выражение на вводе, в котором обнаружена ошибка
        message -- описание ошибки
    """
     def __init__(self, expression, message):
        self.expression = expression
        self.message = message
 class TransitionError(Error):
    """Порождается, когда операция пытается выполнить неразрешённый переход
    из одного состояния в другое.
     Attributes:
        previous -- состояние в начале перехода
        next -- новое состояние, попытка принять которое была принята 
        message -- описание, по какой причине такой переход невозможен
    """
     def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
</pre>

# Семейство OSError

До Python 3.3 существовало много разных типов таких исключений: os.error, socket.error, IOError,WindowsError, select.error и т.д.
Это приводило к тому, что приходилось указывать несколько типов обрабатываемых исключений одновременно:
<pre>
try:
    do_something()
except (os.error, IOError) as ex:
    pass
</pre>
исключения операционной системы часто никак не проявляют себя при разработке. 
Проблема решена в PEP 3151: пишите OSError и не ошибетесь (прочие имена оставлены для обратной совместимости и облегчения портирования кода на новую версию).

У OSError есть атрибут errno, который содержит код ошибки.

Открываем файл, получаем OSError в ответ. Раньше мы должны были анализировать ex.errno чтобы понять, отчего произошла ошибка: может файла нет на диске, а может нет прав на запись — это разные коды ошибок (ENOENT если файла нет и EACCES или EPERM если нет прав).
Приходилось строить конструкцию вроде следующей:
<pre>
try:
    f = open(filename)
except OSError as ex:
    if ex.errno == errno.ENOENT:
       handle_file_not_found(filename)
    elif ex.errno in (errno.EACCES, errno.EPERM):
       handle_no_perm(filename)
    else:
       raise  # обязательно выбрасывать не обработанные коды ошибки

Теперь иерархия расширилась. Полный список наследников OSError:
OSError
 +-- BlockingIOError
 +-- ChildProcessError
 +-- ConnectionError
 |    +-- BrokenPipeError
 |    +-- ConnectionAbortedError
 |    +-- ConnectionRefusedError
 |    +-- ConnectionResetError
 +-- FileExistsError
 +-- FileNotFoundError
 +-- InterruptedError
 +-- IsADirectoryError
 +-- NotADirectoryError
 +-- PermissionError
 +-- ProcessLookupError
 +-- TimeoutError

Наш пример можем переписать как:
try:
    f = open(filename)
except FileNotFound as ex:
    handle_file_not_found(filename)
except PermissionError as ex:
    handle_no_perm(filename)
</pre>

# декоратор

Для того, чтобы понять, как работают декораторы, в первую очередь следует осознать, что в Python'е функции — это тоже объекты.
<pre>
def shout(word="да"): 
    return word.capitalize()+"!" 
 print shout() # выведет: 'Да!' 
 
# Так как функция - это объект - связать её с переменнной, 

scream = shout 
 
print scream() # выведет: 'Да!' 

# мы можем удалить "shout", и функция всё ещё будет доступна через переменную "scream" 
 
del shout 
try: 
    print shout() 
except NameError, e: 
    print e     #выведет: "name 'shout' is not defined" 
 
print scream() # выведет: 'Да!'

# функция в Python'e может быть определена… внутри другой функции!

def talk(): 
    # Внутри определения функции "talk" мы можем определить другую... 
    def whisper(word="да"): 
        return word.lower()+"..."; 
    # ... и сразу же её использовать! 
    print whisper() 

# Теперь, КАЖДЫЙ РАЗ при вызове "talk", внутри неё определяется а затем 
# и вызывается функция "whisper". 

talk() # выведет: "да..." 

# Но вне функции "talk" НЕ существует никакой функции "whisper": 

try: 
    print whisper() 
except NameError, e: 
    print e 
    #выведет : "name 'whisper' is not defined"

# Ссылки на функции

# одна функция может вернуть другую функцию!

def getTalk(type="shout"): 
    # Мы определяем функции прямо здесь 
    def shout(word="да"): 
        return word.capitalize()+"!" 
 
    def whisper(word="да") : 
        return word.lower()+"..."; 

    # Затем возвращаем необходимую 
    if type == "shout": 
        #мы НЕ используем "()", нам нужно не вызвать функцию, 
        # а вернуть объект функции 
        return shout 
    else: 
        return whisper 


Возьмём функцию и свяжем её с переменной 

talk = getTalk() 

"talk" теперь - объект "function": 

выведет: function shout at 0xb7ea817c>  Который можно вызывать, как и функцию, определённую "обычным образом": 

print talk() 

можно вызвать её напрямую из возвращаемого значения: 

print getTalk("whisper")() # выведет: да...

мы можем и передавать её другой функции, как параметр:

def doSomethingBefore(func): 
    print "Я делаю что-то ещё, перед тем как вызвать функцию, которую ты мне передал" 
    print func() 
 doSomethingBefore(scream) 

выведет: 
# Я делаю что-то ещё, перед тем как вызвать функцию, которую ты мне передал 
# Да!
</pre>
декораторы — это, по сути, просто своеобразные «обёртки», которые дают нам возможность делать что-либо до и после того, что сделает декорируемая функция, не изменяя её.

Создадим свой декоратор «вручную»

# Декоратор - это функция, ожидающая ДРУГУЮ функцию в качестве параметра 
<pre>
def my_shiny_new_decorator(a_function_to_decorate): 
    # Внутри себя декоратор определяет функцию-"обёртку". 
    # Она будет (что бы вы думали?..) обёрнута вокруг декорируемой, 
    # получая возможность исполнять произвольный код до и после неё. 

    def the_wrapper_around_the_original_function(): 
        # Поместим здесь код, который мы хотим запускать ДО вызова 
        # оригинальной функции 
        print "Я - код, который отработает до вызова функции" 
 
        # ВЫЗОВЕМ саму декорируемую функцию 
        a_function_to_decorate() 

        # А здесь поместим код, который мы хотим запускать ПОСЛЕ вызова оригинальной функции 
        print "А я - код, срабатывающий после" 

   # На данный момент функция "a_function_to_decorate" НЕ ВЫЗЫВАЛАСЬ НИ РАЗУ 
   # Теперь, вернём функцию-обёртку, которая содержит в себе 
    # декорируемую функцию, и код, который необходимо выполнить до и после. 
    # Всё просто! 
    return the_wrapper_around_the_original_function 

# Представим теперь, что у нас есть функция, которую мы не планируем больше трогать. 
def a_stand_alone_function(): 
    print "Я простая одинокая функция, ты ведь не посмеешь меня изменять?.." 
 
a_stand_alone_function() 
# выведет: Я простая одинокая функция, ты ведь не посмеешь меня изменять?.. 
# Однако, чтобы изменить её поведение, мы можем декорировать её, то есть 
# Просто передать декоратору, который обернет исходную функцию в любой код, 
# который нам потребуется, и вернёт новую, готовую к использованию функцию: 
 
a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function) 
a_stand_alone_function_decorated() 
#выведет: 
# Я - код, который отработает до вызова функции 
# Я простая одинокая функция, ты ведь не посмеешь меня изменять?.. 
# А я - код, срабатывающий после

теперь мы бы хотели, чтобы каждый раз, во время вызова a_stand_alone_function, вместо неё вызывалась a_stand_alone_function_decorated. просто перезапишем a_stand_alone_function функцией, которую нам вернул my_shiny_new_decorator:

a_stand_alone_function = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function()

#выведет:
# Я - код, который отработает до вызова функции
# Я простая одинокая функция, ты ведь не посмеешь меня изменять?..
# А я - код, срабатывающий после

это ровно тоже самое, что делают @декораторы

Разрушаем ореол таинственности вокруг декораторов

Вот так можно было записать предыдущий пример, используя синтаксис декораторов:
@my_shiny_new_decorator 
def another_stand_alone_function(): 
    print "Оставь меня в покое" 
 
another_stand_alone_function() 
#выведет: 
# Я - код, который отработает до вызова функции 
# Оставь меня в покое 
# А я - код, срабатывающий после

@decorator — просто синтаксический сахар для конструкций вида:
another_stand_alone_function = my_shiny_new_decorator(another_stand_alone_function)

Декораторы — это просто pythonic-реализация паттерна проектирования «Декоратор». 

def makebold(fn): 
    def wrapped(): 
        return "<b>" + fn() + "</b>" 
    return wrapped 
 
def makeitalic(fn): 
    def wrapped(): 
        return "<i>" + fn() + "</i>" 
    return wrapped 
 
@makebold 
@makeitalic 
def hello(): 
    return "hello habr" 
 
print hello() ## выведет <b><i&gt;hello habr</i></b>


Конечно, можно вкладывать декораторы друг в друга, например так:
def bread(func): 
    def wrapper(): 
        print "</------\>" 
        func() 
        print "<\______/>" 
    return wrapper 
 
def ingredients(func): 
    def wrapper(): 
        print "#помидоры#" 
        func() 
        print "~салат~" 
    return wrapper 
 
def sandwich(food="--ветчина--"): 
    print food 
 
sandwich() 
#выведет: --ветчина-- 
sandwich = bread(ingredients(sandwich)) 
sandwich() 
#выведет: 
# </------\> 
# #помидоры# 
# --ветчина-- 
# ~салат~ 
# <\______/>
И используя синтаксис декораторов:

@bread 
@ingredients 
def sandwich(food="--ветчина--"): 
    print food 
 
sandwich() 
#выведет: 
# </------\> 
# #помидоры# 
# --ветчина-- 
# ~салат~ 
# <\______/> 

Следует помнить о том, что порядок декорирования ВАЖЕН:
@ingredients 
@bread 
def sandwich(food="--ветчина--"): 
    print food 
 
sandwich() 
#выведет: 
# #помидоры# 
# </------\> 
# --ветчина-- 
# <\______/> 
# ~салат~
</pre>