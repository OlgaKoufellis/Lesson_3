# print('Olga ' * 10)
#
# print('Olga\n' * 10)
#
# print('Olga')
# print('Olga')
# print('Olga')
# print('Olga')
# print('Olga')
# print('Olga')
# print('Olga')
# print('Olga')
# print('Olga')

#Циклы (Loops) : While ,For

# while True:  #if true loops
#     print('Andrii')
#
# flag = True
# while flag:
#     print('Something')
#     flag = False

# i = 0
# while i < 10:
#     print("Andrey")
#     i = i + 1 # инкримент i += 1
#     i = i - 1 # декримент i -= 1
#     i = i * 1 # i *= 1
#     i = i / 1 # i /= 1
#     i = (i/i) * i

# i = 0
# while i < 10:
#     i = i - 1
#     print("Andrey")

#
# i = 0
# while i < 10:
#     word = ''
#     i += 1
#     word = word + str(i)
#     print(word)
#
# i = 0
# word = ''
# while i < 10:
#     i += 1
#     word = word + str(i)
#     print(word)

'''Задача 1
Пользователь вводит с клавиатуры два числа/ Нужно показать все числа в порядке убывания
# '''
# a = 0
# b = 10
# while a <= b:
#     print(a)
#     a += 1
#
# # числа в порядке убывания
# a = 10
# b = 0
# while a >= b:
#     print(a)
#     a -= 1

'''
адание 2
Пользователь вводит с клавиатуры два числа. Нужно
показать все нечетные числа в указанном диапазоне.
'''
# a = 0
# b = 10
# while a <= b:
#     if a%2!=0:
#      print(a)
#     a = a + 1

'''
адание 3
Пользователь вводит с клавиатуры два числа. Нужно
показать все четные числа в указанном диапазоне.
# 
# '''
# a = 0
# b = 10
# while a <= b:
#     if a % 2 == 0:
#      print(a)
#     a = a + 1
#
# # flake8 >linter > PEP8
#
# '''Задание 5
# Пользователь вводит с клавиатуры два числа. Нужно показать все нечетные числа в указанном диапазоне.
# Если границы диапазона указаны неправильно требуется
# произвести нормализацию границ. Например, пользователь ввел 33 и 13, требуется нормализация после которой
# начало диапазона станет равно 13, а конец 33.
# '''
#
# a = 13
# b = 33
# if a > b:
#     temp_number = a
#     a = b
#     b = temp_number
# while a <= b:
#     if a % 2 != 0:
#         print(a)
#     a = a + 1
#
# a = 33
# b = 13
# if a > b:
#     a,b = b, a
# while a <= b:
#     if a % 2 == 1:
#         print(a)
#     a += 1

'''
Задание 1
Пользователь вводит с клавиатуры два числа. Нужно
посчитать сумму чисел в указанном диапазоне, а также
среднеарифметическое.
'''
# a = int(input("Please fill in the first number: ")) # 0
# b = int(input("Please fill in the second number: ")) # 36
# sum = 0
# count = 0
# while a <= b:
#     count = count + 1
#     sum = sum + a
#     a += 1
# print(sum, sum/count)

# a = 0
# b = 36
# sum = 0
# count = 0
# while a <= b:
#     count = count + 1
#     sum = sum + a
#     a += 1
# print(sum, sum/count)


'''
Пользователь ввводит с клавиатуры числою Требуется подсчитать факториал числаю Например если введено 3, 
факториал числа 1;2;3 = 6.
Формула для расчета факториалаЖ т! = 1*2*3...*n, где n - число для расчета факториала

'''
# a = 1
# b = 7
# s = 1
# while a <= b:
#    s *= a
#    a += 1
# print(s)

'''Задание 3
Пользователь вводит с клавиатуры длину линии.
Нужно отобразить на экране горизонтальную линию
из *, указанной длины.
Например, если было введено 7, тогда вывод на экран
будет такой: *******.
'''
#
# a = int(input("Enter your number: "))
# while a > 0:
#     print('*',end='')
#     a = a - 1
# print()
#
#
#
# a = int(input("Input first number"))
# s = ''
# while a > 0:
#     s = s + '*'
#     a = a - 1
#     print(s)
#
# '''
# Задание 4
# Пользователь вводит с клавиатуры длину линии и
# символ для заполнения линии. Нужно отобразить на
# экране горизонтальную линию из введенного символа,
# указанной длины.
# Например, если было введено 5 и &, тогда вывод на
# экран будет такой: &&&&&.
# '''
#
#
#
# #[20:20] Батюк Андрей Викторович
# a = int(input("Input lenght of the line value: "))
# b = str(input("Input symbol of the line: "))
# while a > 0:
#  print(b,end='')
# a = a - 1
#
#
# #[20:21] Черняк Александр Игоревич
# l = 15
# s = "&"
# while l > 0:
#     print("$" * l, end="")
#     l = l-1
#
#
# a = 10
# s = ''
# l = '&'
# while a > 0:
#     s = s + 1
#     a = a - 1
# print(s)
#
# #GUESS MY NUMBER
# import random #библиотека рандомных чисел
# secret_number = random.randint(1,20)
# guess_number = 0
# lifes = 5
# while secret_number != guess_number and lifes > 0:
#     guess_number = int(input('Enter :'))
#     lifes = lifes - 1
#     print(f'You have {Lifes} lifes')
#     if secret_number < guess_number:
#         print("Your number is greater than a secret_number")
#     elif secret_number > guess_number:
#         print('Your number is less than a secret_number')
# if lifes > 0:
#     print('You Win!!!')
# else:
#     print('You Lose!!!')
#
# # GAME
# import random #библиотека рандомных чисел
# game = True
# while game:
#  secret_number = random.randint(1,20)
#  guess_number = 0
#  lifes = 5
#  money = 0
#  while secret_number != guess_number and lifes > 0:
#     guess_number = int(input('Enter :'))
#     lifes = lifes - 1
#     print(f'You have {Lifes} lifes')
#     if secret_number < guess_number:
#         print("Your number is greater than a secret_number")
#     elif secret_number > guess_number:
#         print('Your number is less than a secret_number')
#  if lifes > 0:
#     print('You Win!!!')
#     money = money + 5
#  else:
#     print('You Lose!!!')
# Print(f'You have {money}')
#
#
# work = True
# while work :
#     number1 = int(input('Enter number1: '))
#     command = str(input('Enter operation: '))
#     number2 = int(input('Enter number1: '))
#     if command == '+':
#         print(f'{number1} {command} {number2} = {number1 + number2}')
#     # while command == '+':
#     #     print(f'{number1} {command} {number2} = {number1 + number2}')
#     #     command = ''
#     elif command == '-':
#         print(f'{number1} {command} {number2} = {number1 - number2}')
#     elif command == '*':
#         print(f'{number1} {command} {number2} = {number1 * number2}')
#     elif command == '/':
#         print(f'{number1} {command} {number2} = {number1 / number2}')
#     work = str(input('Please, press any key to continue: '))

'''Задание 1
Показать таблицу умножения для числа, введенного
пользователем. Например, если пользователь вводит
число 7, нужно показать:
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
'''
a = 7
number = 0
while number <= 10:
 print (f'{a} * {number} = {a * number}')
 number += 1


# https://github.com/builuk1/builuk1-QA03