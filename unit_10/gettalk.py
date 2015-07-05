# -*- coding:utf-8 -*-

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


# Возьмём функцию и свяжем её с переменной 

talk = getTalk() 

# "talk" теперь - объект "function": 

# выведет: <function shout at 0xb7ea817c>  Который можно вызывать, как и функцию, определённую "обычным образом": 

print talk() 

# можно вызвать её напрямую из возвращаемого значения: 

print getTalk("whisper")() # выведет: да...

# мы можем и передавать её другой функции, как параметр:

def doSomethingBefore(func): 
    print "Я делаю что-то ещё, перед тем как вызвать функцию, которую ты мне передал" 
    print func() 

def shout(word="да"): 
    return word.capitalize()+"!" 
# print shout() # выведет: 'Да!' 
 
# Так как функция - это объект - связать её с переменнной, 

scream = shout 

doSomethingBefore(scream) 

# выведет: 
# Я делаю что-то ещё, перед тем как вызвать функцию, которую ты мне передал 
# Да!

