# a = 0
# while a < 10:
#     print(a)
#     a += 1
#
# for i in 0,1,2,3,4,5,6,7,8,9:
# #     print(i)
#
# for i in 'Hello World':
#     print(i)
#
# for i in 'Hello World':
#     print(i, end=' ')
#
# for i in range(1, 10):
#     print(i)
#
# for a in  'Olga':
#     print(a)
#
# for a in  'Olga':
#     print(a , end='')
#
# for i in range(10):
#     print(i)
#
# a = 0
# b = 10
# for i in range(a,b,-1):
#     print (i)


'''
Задание 1
Пользователь вводит с клавиатуры два числа. Нужно
показать все числа в указанном диапазоне.
'''

# a = int(input('Please, enter the first number: '))
# b =int(input('Please, enter the second number: '))
# for i in range(a, b): # ( от, до, шаг)
#      print(i)


'''
Задание 2
Пользователь вводит с клавиатуры два числа. Нужно
показать все нечетные числа в указанном диапазоне.
'''
# a = int(input('Please, enter the first number: '))
# b = int(input('Please, enter the second number: '))
# for i in range(a,b ,+1):
#     if i % 2 != 0:
#         print(i)


'''
Задание 3
Пользователь вводит с клавиатуры два числа. Нужно
показать все четные числа в указанном диапазоне.
'''

# a = int(input('Please, enter the first number: '))
# b = int(input('Please, enter the second number: '))
# for i in range(a,b ,+1):
#     if i % 2 == 0:
#         print(i)


'''
Задание 4
Пользователь вводит с клавиатуры два числа. Нужно показать все числа в указанном диапазоне в порядке
убывания.'''
# a = int(input('Please, enter the first number: '))
# b = int(input('Please, enter the second number: '))
# for i in range(b, a, -1, -1):
#         print(i)



'''
Задание 5
Пользователь вводит с клавиатуры два числа. Нужно показать все нечетные числа в указанном диапазоне.
Если границы диапазона указаны неправильно требуется
произвести нормализацию границ. Например, пользователь ввел 33 и 13, требуется нормализация после которой
начало диапазона ст
'''
# a = int(input('Please, enter the first number: '))
# b = int(input('Please, enter the second number: '))
# numm = 0
# if a > b:
#     numm = a
#     a = b
#     b = numm
# for i in range(a, b +1):
#     if i % 2 != 0:
#       print(i)

'''
Задание 1
Пользователь вводит с клавиатуры два числа. Нужно
посчитать сумму чисел в указанном диапазоне, а также
среднеарифметическое.
'''
# a = 2
# b = 6
# sum = 0
# count = 0
# average = 0
# for i in range(a, b +1):
#     count = count + 1
#     sum = sum + i
#     average = sum / count
# print (sum, average)




'''
Задание 2
Пользователь вводит с клавиатуры число. Требуется
посчитать факториал числа. Например, если введено 3,
факториал числа 1*2*3 = 6.
Формула для расчета факториала: n! = 1*2*3…*n, где
n — число для расчета факториала.

'''
number1 = int(input('Please, enter the first number: '))
n = 1
for i in range(number1 + 1):
    if i == 0:
        continue
    n = n * i
print(n)

'''
Задание 3
Пользователь вводит с клавиатуры длину линии.
Нужно отобразить на экране горизонтальную линию
из *, указанной длины.
Например, если было введено 7, тогда вывод на экран
будет такой: *******.
'''
# length = int(input('Please, enter length: '))
# for i in range(length):
#     print('*', end='')

# a= 6
# b= '*'
# for i in (a * b):
#     print(i, end='')


'''
Задание 4
Пользователь вводит с клавиатуры длину линии и
символ для заполнения линии. Нужно отобразить на
экране горизонтальную линию из введенного символа,
указанной длины.
Например, если было введено 5 и &, тогда вывод на
экран будет такой: &&&&&.
'''

length = int(input('Please, enter length: '))
symbol = input('Please, enter symbol: ')
for i in range(length):
    print(symbol, end='')
#
#
#
# a= 1
# b= 10
# while a <= b and a != 5:
#     a = a + 1
#
