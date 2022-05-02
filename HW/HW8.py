''''
Задание 1
Пользователь вводит с клавиатуры два числа.
Нужно посчитать отдельно сумму четных, нечетных и чисел, кратных 9 в указанном диапазоне,
 а также среднеарифметическое каждой группы.
'''

num1 = int(input('Please, enter the first number: '))
num2 = int(input('Please, enter the second number: '))
count = 0
count2 = 0
count3 = 0
even = 0
odd = 0
multiple9 = 0
for i in range(num1, num2 + 1):
    if i % 2 == 0:
        if i % 9 == 0:
            count3 += 1
            multiple9 = multiple9 + i
            count += 1
            even = even + i
            i += 1
        else:
            count += 1
            even = even + i
            i += 1
    elif i % 2 != 0:
        if i % 9 == 0:
            count3 += 1
            multiple9 = multiple9 + i
            count2 += 1
            odd = odd + i
            i += 1
        else:
            count2 += 1
            odd = odd + i
            i += 1
print(f'{even}- is even ,\n{odd}- is odd ,\n{multiple9}- is multiple to 9')
if count3 != 0:
    print(f'{even/ count}, {odd/ count2} , {multiple9 / count3}')
else:
    print(f'average of even group is :{even / count}, \naverage of odd group is :{odd / count2}, \naverage of multiple to 9 group is :0.0')


2
num1 = int(input('Please, enter the first number: '))
num2 = int(input('Please, enter the second number: '))
count = 0
count2 = 0
count3 = 0
even = 0
odd = 0
multiple9 = 0
for i in range(num1, num2 + 1):
    if i % 9 == 0:
        count3 += 1
        multiple9 = multiple9 + i
    if i % 2 == 0:
        count += 1
        even = even + i
        i += 1
    elif i % 2 != 0:
        count2 += 1
        odd = odd + i
        i += 1
print(f'{even}- is even ,\n{odd}- is odd ,\n{multiple9}- is multiple to 9')
if count3 != 0:
    print(f'{even/ count}, {odd/ count2} , {multiple9 / count3}')
else:
    print(f'average of even group is :{even / count}, \naverage of odd group is :{odd / count2}, \naverage of multiple to 9 group is :0.0')


'''
Задание 2 
Пользователь вводит с клавиатуры длину линии и символ для заполнения линии.
Нужно отобразить на экране вертикальную линию из введенного символа, указанной длины.
Например, если было введено 5 и символ %, тогда вывод на экран будет такой:
% % % % %
'''
length = 0
symbol = '*'
while True:
    try:
        length = int(input('Please, enter a length: '))
        symbol = str(input('Please, enter the symbol: '))
        break
    except ValueError:
        print('Неверный формат')
for i in range(length):
    print(symbol, end=' ')

'''
Задание 3 
Пользователь вводит с клавиатуры числа. Если число больше нуля нужно вывести надпись «Number is positive»,
если меньше нуля «Number is negative», если равно нулю «Number is equal to zero». 
Когда пользователь вводит число 7 программа прекращает свою работу и выводит на экран надпись «Good bye!»
'''

while num1 != 7:
    num1 = int(input('Please, enter the first number: '))
    if num1 > 0:
        print('Number is positive')
    if num1 < 0:
        print('Number is negative')
    if num1 == 0:
        print('Number is equal to zero')
    if num1 == 7:
        print('Good bye!')

#  2
while True:
    num1 = int(input('Please, enter the first number: '))
    if num1 > 0:
        print('Number is positive')
    if num1 < 0:
        print('Number is negative')
    if num1 == 0:
        print('Number is equal to zero')
    if num1 == 7:
        print('Good bye!')
        break

'''
Задание 4 
Пользователь вводит с клавиатуры числа. 
Программа должна подсчитывать сумму, максимум и минимум, введенных чисел.
Когда пользователь вводит число 7 программа прекращает свою работу и выводит на экран надпись «Good bye!»
'''
max = ''
min = ''
sum = 0
count = 0
while True:
    num1 = int(input('Please, enter a number: '))
    if count == 0:
        count += 1
        min = num1
        max = num1
        sum = sum + num1
        print( 'Sum is: ',sum, '\nMin is: ', min, '\nMax is:', max, end=' ')
        print()
    elif num1 == 7:
        print('Good bye!')
        break
    elif count > 0:
        if num1 > min:
            count += 1
            max = num1
            sum = sum + num1
            print('Sum is: ',sum, '\nMin is: ', min, '\nMax is:', max, end=' ')
            print()
        if num1 < min:
            count += 1
            min = num1
            sum = sum + num1
            print('Sum is: ',sum, '\nMin is: ', min, '\nMax is:', max, end=' ')
            print()



# II
max = -9**9999999
min = 9**999999999
sum = 0
while True:
    num1 = int(input('Please, enter a number: '))
    if num1 > max:
        max = num1
    if num1 < min:
        min = num1
    sum = sum + num1
    print('Sum is: ', sum, '\nMin is: ', min, '\nMax is:', max, end=' ')
    print()
    if num1 == 7:
        print('Good bye!')
        break