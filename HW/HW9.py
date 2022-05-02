'''
Задание 1
Напишите программу, которая запрашивает два целых числа x и y,
после чего вычисляет и выводит значение x в степени y.

'''
while True:
    x = int(input('Please, enter the first number : '))
    y = int(input('Please, enter the second number : '))
    print(x ** y)


#II
while True:
    x = int(input('Please, enter the first number : '))
    y = int(input('Please, enter the second number : '))
    n = 1
    for i in range(y + 1):
        if i == 0:
            continue
        n = x * n
    print(n)

# III
while True:
    x = int(input('Please, enter the first number : '))
    y = int(input('Please, enter the second number : '))
    n = 1
    for i in range(y):
        n = x * n
    print(n)



'''
Задание 2 
Подсчитать количество целых чисел в диапазоне от 100 до 999 у которых есть две одинаковые цифры.
'''
a = 100
b = 999
count = 0
for i in range(a, b + 1):
    num = str(i)
    n1 = int(num[0])
    n2 = int(num[1])
    n3 = int(num[2])
    if n1 == n2 or n2 == n3 or n1 == n3:
        count += 1
print(count)


'''
Задание 3 
Подсчитать количество целых чисел в диапазоне от 100 до 9999 у которых все цифры разные.
'''
a = 100
b = 9999
count = 0
for i in range(a, b + 1):
    num = str(i)
    n1 = int(num[0])
    n2 = int(num[1])
    n3 = int(num[2])
    if i // 1000 > 0:
        n4 = int(num[3])
    else:
        n4 = 99
    if n1 != n2:
        if n1 != n3:
            if n1 != n4:
                if n2 != n3:
                    if n2 != n4:
                        if n3 != n4:
                            count += 1
print(count)


'''
Задание 4 
Пользователь вводит любое целое число. 
Необходимо из этого целого числа удалить все цифры 3 и 6 и вывести обратно на экран.
'''
while True:
    num = input('Please, enter a number:')
    for i in range(len(num)):
        if num[i] == '6' or num[i] == '3':
            continue
        else:
            print(num[i], end='')
    print()


# II

print(input('Please, enter a number:').replace("3", "").replace("6", ""))





