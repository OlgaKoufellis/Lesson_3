'''
Модуль 4.
Строки. Списки.
Часть 3


Задание 1
 Два списка целых заполняются случайными числами. Необходимо:
■ Сформировать третий список, содержащий элементы обоих списков;
■ Сформировать третий список, содержащий элементы обоих списков без повторений;
■ Сформировать третий список, содержащий элементы общие для двух списков;
■ Сформировать третий список, содержащий только уникальные элементы каждого из списков;
■ Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков.

'''

a = [1, 4, 7, 9, -7, 54, 12, -1, 0, 21]
b = [-1, 7, 8, -19, 7, 4, 22, -31, 12, 2]
c = a[:]
for i in b:
    c.append(i)
print(c)
s = list(set(c))
print(s) # 2 и 4 задание
c = list(set(a) & set(b))
print(c)
c = [min(a), max(a), min (b), max(b)]
print(c)






