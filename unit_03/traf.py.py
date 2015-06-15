#!/usr/bin/env python
#coding: utf8

# 1 считываем из файла строки и делим их на пары IP-адрес
raw = [x.split(" ")  for x in open("log.txt")]

# 2 заполняем словарь
rmp = {}
for ip, traffic in raw:
        if ip in rmp:
                rmp[ip] += int(traffic)
        else:
                rmp[ip] = int(traffic)

# 3 переводим в список и сортируем
lst = rmp.items()
lst.sort(key = lambda (key, val): key)
# 4 получаем результат
print "\n".join(["%s\t%d" % (host, traff) for host, traff in lst])