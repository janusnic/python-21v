# Стандартные модули

import sys

# Пути к  каталогам, в которых Python ищет модули, можно увидеть в значении переменной sys.path
print(sys.path)

# argv Список аргументов командной строки. Обычно sys.argv[0] содержит имя запущенной программы, а остальные параметры передаются из командной строки.
print(sys.argv[0])

# version Версия интерпретатора.
print(sys.version)

# Информация об обрабатываемом исключении.

print(sys.exc_info())

offset = 20
if not sys.platform.startswith('win'):
	offset = 10

print (offset)

# Переменная sys.platform хранит название текущей платформы
offset = 20 if sys.platform.startswith('win') else 10

print (offset)
# Особенно неприятно, что эта строка программного кода работает правильно, когда переменная margin имеет значение True
margin = True
offset = 100 + 10 if margin else 0

print (offset)

# интерпретатор Python воспринимает выражение 100 + 10 как часть expressionl условного выражения
margin = False
offset = 100 + 10 if margin else 0

print (offset)

# Решить эту проблему можно с помощью круглых скобок
margin = False
offset = 100 + (10 if margin else 0)

print (offset)

# Условные выражения могут использоваться для видоизменения сообщений, выводимых для пользователя
count = 4
print ("{0} file{1}".format((count if count != 0 else "no"),
	("s" if count !=1 else "")))