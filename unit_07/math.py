import math
import string
# Локальные функции
# функция, которая вычисляет площадь треугольника по формуле Герона: 
def heron(a, b, c): 
	s=(a+b+c)/2 
	return math.sqrt(s * (s - a) * (s - b) * (s - c)) 

print(heron(100,100,100))

# функция, которая подсчитывает количество алфавитных символов в строке; по умолчанию подразумеваются алфавитные символы из набора ASCII: 
def letter_count(text, letters=string.ascii_letters): 
	letters = frozenset(letters) 
	count = 0 
	for char in text: 
		if char in letters: 
			count += 1 
	return count 
text = 'функция, которая подсчитывает количество алфавитных символов в строке; по умолчанию подразумеваются алфавитные символы из набора ASCII: '

print(letter_count(text))

# String constants
# string.ascii_letters
# The concatenation of the ascii_lowercase and ascii_uppercase constants described below. This value is not locale-dependent.
print(letter_count(text,string.ascii_letters))
# string.ascii_lowercase
# The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. This value is not locale-dependent and will not change.
print(letter_count(text,string.ascii_lowercase))
# string.ascii_uppercase
# The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. This value is not locale-dependent and will not change.
print(letter_count(text,string.ascii_uppercase))
# string.digits
# The string '0123456789'.
print(letter_count(text,string.digits))
# string.hexdigits
# The string '0123456789abcdefABCDEF'.
print(letter_count(text,string.hexdigits))
# string.letters
# The concatenation of the strings lowercase and uppercase described below. The specific value is locale-dependent, and will be updated when locale.setlocale() is called.
# print(letter_count(text,string.letters))
# string.lowercase
# A string containing all the characters that are considered lowercase letters. On most systems this is the string 'abcdefghijklmnopqrstuvwxyz'. The specific value is locale-dependent, and will be updated when locale.setlocale() is called.
# print(letter_count(text,string.lowercase))
# string.octdigits
# The string '01234567'.
print(letter_count(text,string.octdigits))
# string.punctuation
# String of ASCII characters which are considered punctuation characters in the C locale.
print(letter_count(text,string.punctuation))
# string.printable
# String of characters which are considered printable. This is a combination of digits, letters, punctuation, and whitespace.
print(letter_count(text,string.printable))

# string.uppercase
# A string containing all the characters that are considered uppercase letters. On most systems this is the string 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. The specific value is locale-dependent, and will be updated when locale.setlocale() is called.
# print(letter_count(text,string.uppercase))
# string.whitespace
# A string containing all characters that are considered whitespace. On most systems this includes the characters space, tab, linefeed, return, formfeed, and vertical tab.
print(letter_count(text,string.whitespace))

# короткая функция, возвращающая заданную строку, если ее длина меньше или равна заданной длине, и усеченную версию строки с добавлением в конец значения параметра indicator - в противном случае
def shorten(text, length=25, indicator="..."): 
	if len(text) > length: 
		text = text[:length - len(indicator)] + indicator 
	return text 

print(shorten("The Road")) # вернет: 'The Road' 
print(shorten(length=7, text="The Road")) # вернет: 'The ..." 
print(shorten("The Road", indicator="&", length=7)) # вернет: 'The Ro&' 
print(shorten("The Road", 7, "&")) # вернет: 'The Ro&* 

# Значения по умолчанию создаются на этапе выполнения инструкции def 
# (то есть в момент создания функции), а не в момент ее вызова. 
# Для неизменяемых аргументов, таких как строки или числа, это не имеет никакого значения, 
# но в использовании изменяемых аргументов кроется труднозаметная ловушка. 

def append_if_even(x, lst=[]): # ОШИБКА! 
	if x % 2 == 0: 
		lst.append(x) 
	return lst 

print(append_if_even(22))
lst = [2,4,6,7]
print(append_if_even(22,lst))

# каждый раз, когда функция вызывается без второго аргумента, будет создаваться новый пустой
def append_if_evenm(x, lst=None): 
	if lst is None: 
		lst = [] 
	if x % 2 == 0: 
		lst.append(x) 
	return lst 

print(append_if_evenm(22,lst))	

# Примеры вложенных областей видимости:
X = 99    # Имя в глобальной области видимости: не используется

def f1():
    X = 88        # Локальное имя в объемлющей функции
    def f2():
        print(X)  # Обращение к переменной во вложенной функции
    f2()

f1() # Выведет 88: локальная переменная в объемлющей функции

# Объемлющая функция - функция которая содержит в себе вложенную функцию.


def f1():
    X = 88
    def f2():
        print(X)   # Сохраняет значение X в объемлющей области видимости
    return f2      # Возвращает f2, но не вызывает ее

action = f1()      # Создает и возвращает функцию
action()           # Вызов этой функции: выведет 88

# Фабричные функции(замыкание):

def maker(N):
    def action(X):      # Создать и вернуть функцию
        return X ** N   # Функция action запоминает значение N в объемлющей
    return action        # области видимости

# Если снова вызвать внешнюю функцию, мы получим новую вложенную
# функцию уже  с  другой  информацией о состоянии.

f = maker(2)                # Запишет 2 в N
print(f)
print(f(3))
print(f(4))

g = maker(3)       # Функция g хранит число 3, а f – число 2
print(g(3))
print(f(4))
