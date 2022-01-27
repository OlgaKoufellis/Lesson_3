'''
Задание 2
Пользователь вводит с клавиатуры число. Требуется
посчитать факториал числа. Например, если введено 3,
факториал числа 1*2*3 = 6.
Формула для расчета факториала: n! = 1*2*3…*n, где
n — число для расчета факториала.

'''

# number1 = int(input('Please, enter the first number: '))
# n = 1
# for i in range(number1 + 1):
#     if i == 0:
#         continue
#     n = n * i
# print(n)


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
#
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
# length = int(input('Please, enter length: '))
# symbol = input('Please, enter symbol: ')
# for i in range(length):
#     print(symbol, end='')

'''
Задание 3
Пользователь вводит с клавиатуры две границы диапазона и число. Если число не попадает в диапазон,
программа просит пользователя повторно ввести число,
и так до тех пор, пока он не введет число правильно. Программа отображает все числа диапазона, выделяя число
восклицательными знаками. Например:
1 2 3 !4! 5 6 7.
# '''

# num1 = 1
# num2 = 7
# num3 = int(input('Please ,enter a number: '))
# for i in range(num1, num2 + 1):
#     if num3 > num2 or num3 < num1:
#         num3 = int(input('Please ,enter a number: '))
#     elif i < num3:
#         print(i,  end='' )
#     elif  i == num3:
#         print('!', i ,'!', end='')
#     else:
#         print(i , end='')

# num1 = 1
# num2 = 7
# num3 = int(input('Please ,enter a number: '))
# while num3 > num2 or num3 < num1:
#     num3 = int(input('Please ,enter a number: '))
# for i in range(num1, num2 + 1):
#     if i == num3:
#         print('!', i, '!', sep='', end='')
#     else:
#         print(i, sep=' ', end='')

'''
Задание 1
Пользователь вводит с клавиатуры размер стороны
квадрата. Требуется отобразить на экран заполненный
квадрат. Размер стороны равен введённому размеру.
Например, если пользователь ввёл 3 на экране будет
выведено:
***
***
***
'''

# width = 3
# length = 3
# symbol = '*'
# for i in range(width):
#     print(length * '*')
# print()

# width = 3
# length = 3
# symbol = '*'
# for i in range(width):
#     print(length * '  *', sep=' ')
# print()
#
# height = int(input('Please enter height of a square: '))
# length = height
# for i in range(height):
#     print(length * '  *', sep=' ')
# print()

'''
Задание 3
Пользователь вводит с клавиатуры размер стороны
квадрата. Требуется отобразить на экран незаполненный квадрат (отображаются только границы квадрата).
Размер стороны равен введённому размеру.
# '''
height = int(input('Please enter height of a square: '))
lenght = height
symbol = '*'
space = ' '
for i in range(height):
    if i == 0 or i == (height - 1):
        print(lenght *(space * 2 + symbol))
    else:
        print( space +symbol + (((lenght - 2) * (space * 2))) * 2 + symbol)
print()


# width = 5
# height = 5
# symbol = '*'
# s = ' '
# for i in range(height):
#    if  i == 0 or i == (height - 1):
#       print(width * symbol)
#    else:
#       print( symbol + ((width - 2) * s) + symbol)
