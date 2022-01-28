'''
Задание 1
Пользователь вводит с клавиатуры два числа (начало и конец диапазона).
Требуется проанализировать все числа в этом диапазоне по следующему правилу:
если число кратно 7, его надо выводить на экран.
'''
num1 = int(input('Please, enter the first number: '))
num2 = int(input('Please, enter the second number: '))
if num1 < num2:
    for i in range(num1,num2 + 1):
        if i / 7 != i // 7:
         continue
        else:
            print(i)
elif num1 > num2:
    for i in range(num1,num2 - 1, -1):
        if i / 7 != i // 7:
         continue
        else:
            print(i)


2 вариант
num1 = int(input('Please, enter the first number: '))
num2 = int(input('Please, enter the second number: '))
if num1 < num2:
    for i in range(num1, num2 + 1):
        if i % 7 == 0:
            print(i)
        else:
            continue
elif num1 > num2:
    for i in range(num1, num2 - 1, -1):
        if i % 7 == 0:
            print(i)
        else:
            continue



'''
Задание 2 Пользователь вводит с клавиатуры два числа (начало и конец диапазона).
Требуется проанализировать все числа в этом диапазоне. Нужно вывести на экран:
1. Все числа диапазона;
2. Все числа диапазона в убывающем порядке;
3. Все числа, кратные 7;
4. Количество чисел, кратных 5.
'''

# #Вариант I
num1 = int(input('Please, enter the first number: '))
num2 = int(input('Please, enter the second number: '))
num0 = 0
count = 0
while num1 == num2:
    num1 = int(input('Please, enter the first number: '))
    num2 = int(input('Please, enter the second number: '))
if num1 < num2:
    print('1)', end='')
    for i in range(num1,num2 +1):
        if i == num2:
            print(i)
        else:
            print(i, end=', ')
    print('2)', end='')
    for i in range(num2,num1 -1, - 1) :
        if i == num1:
            print(i)
        else:
            print(i, end=', ')
    print('3)', end='')
    for i in range(num1,num2 +1):
        if i / 7 != i // 7:
            continue
        else:
            print(i, end=', ')
    for i in range(num1, num2 + 1):
        if i / 5 != i // 5:
            continue
        else:
            count += 1
    print('\n4)',count)
elif num1 > num2:
    print('1)', end='')
    for i in range(num1,num2 -1, -1):
        if i == num2:
            print(i)
        else:
            print(i, end=', ')
    print('2)', end='')
    for i in range(num2,num1 +1,) :
        if i == num1:
            print(i)
        else:
            print(i, end=', ')
    print('3)', end='')
    for i in range(num1,num2 -1, -1):
        if i / 7 != i // 7:
            continue
        else:
            print(i, end=', ')
    for i in range(num1, num2 - 1, -1):
        if i / 5 != i // 5:
            continue
        else:
            count += 1
    print('\n4)',count)

#Вариант II

num1 = int(input('Please, enter the first number: '))
num2 = int(input('Please, enter the second number: '))
num0 = 0
count = 0
while num1 == num2:
    num1 = int(input('Please, enter the first number: '))
    num2 = int(input('Please, enter the second number: '))
if num1 < num2:
    print('1)', end='')
    for i in range(num1,num2 +1):
        if i == num2:
            print(i)
        else:
            print(i, end=', ')
    print('2)', end='')
    for i in range(num2,num1 -1, - 1) :
        if i == num1:
            print(i)
        else:
            print(i, end=', ')
    print('3)', end='')
    for i in range(num1,num2 +1):
        if i % 7 == 0:
            print(i, end=', ')
        else:
            continue
    for i in range(num1, num2 + 1):
        if i % 5 == 0:
            count += 1
        else:
            continue
    print('\n4)',count)
elif num1 > num2:
    print('1)', end='')
    for i in range(num1,num2 -1, -1):
        if i == num2:
            print(i)
        else:
            print(i, end=', ')
    print('2)', end='')
    for i in range(num2, num1 + 1,) :
        if i == num1:
            print(i)
        else:
            print(i, end=', ')
    print('3)', end='')
    for i in range(num1, num2 - 1, -1):
        if i % 7 == 0:
            print(i, end=', ')
        else:
            continue
    for i in range(num1, num2 - 1, -1):
        if i % 5 == 0:
            count += 1
        else:
            continue
    print('\n4)',count)
'''
Задание 3
Пользователь вводит с клавиатуры два числа (начало и конец диапазона).
Требуется проанализировать все числа в этом диапазоне.
Вывод на экран должен проходить по правилам, указанным ниже.
Если число кратно 3 (делится на 3 без остатка) нужно вывести слово Fizz.
 Если число кратно 5 нужно выве- сти слово Buzz.
 Если число кратно 3 и 5 нужно вывести Fizz Buzz.
 Если число не кратно не 3 и 5 нужно вывести само число.
'''

num1 = int(input('Please, enter the first number: '))
num2 = int(input('Please, enter the second number: '))
if num1 < num2:
    for i in range(num1, num2 + 1):
        if i % 3 == 0:
            if i % 5 == 0:
                print('Fizz Buzz')
            else:
                print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
elif num1 > num2:
    for i in range(num1, num2 - 1, -1):
        if i % 3 == 0:
            if i % 5 == 0:
                print('Fizz Buzz')
            else:
                print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

