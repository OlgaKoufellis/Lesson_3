'''
 1
'''
# Площадь прямоуголного треуголника
import math
while True:
    try:
        def third_side(a, b):
            c = math.sqrt(a**2 + b ** 2)
            return c

        a = float(input('Please enter first side (cathetus) of your right-angled triangle:'))
        b = float(input('Please enter the second side (cathetus) of your right-angled triangle:'))
        d = float(input('Please enter the third side of your right-angled triangle:'))

        if d == third_side(a,b):
            S = (a * b) / 2
            print(S)
        else:
            print(f'Your triangle is not right-angled triangle!!!, '
                  f'Your third side(hypotenuse) should be equal : {third_side(a,b)}')
    except ValueError:
        print('Sorry , but you did some mistakes, please re-write it again.')

#2
import random

''''''
'''В школе решили набрать три новых математических класса. Так как
занятия по математике у них проходят в одно и то же время, было решено выделить кабинет для каждого 
класса и купить в них новые парты. За каждой партой может сидеть не больше двух учеников.
Известно количество учащихся в каждом из трёх классов. Сколько всего нужно закупить парт чтобы их 
хватило на всех учеников? Программа получает на вход три натуральных числа: количество
учащихся в каждом из трех классов.'''


def Total_number_of_kids(first_class, second_class, third_class):
    Total_number_of_kids = first_class + second_class + third_class
    return Total_number_of_kids

def number_of_desk():
    desks = Total_number_of_kids(first_class, second_class, third_class) / 2
    return round(desks + 0.5)
try:
    first_class = int(input('Please enter your number of kids in the first class:'))
    second_class = int(input('Please enter your number of kids in the second class:'))
    third_class = int(input('Please enter your number of kids in the third class:'))
    print(number_of_desk())
except ValueError:
    print('Oooooops, you have to enter your entire number!!!')
except:
    print('Something strange has happened here... Sorry!')

#3
'''
Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна вывести одно из чисел: 
3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).
'''
try:
    first_num = int(input('Please enter your first number :'))
    second_num = int(input('Please enter your second number :'))
    third_num = int(input('Please enter your third number :'))

    if first_num == second_num == third_num:
        print("3")
    elif first_num == second_num or second_num == third_num or third_num == first_num:
        print("2")
    else:
        print('0')
except ValueError:
        print('Sorry , but you did some mistakes, please re-write it again.')

#4
'''
Дано натуральное число. Требуется определить, является ли год с данным номером високосным. Если год является високосным, то
выведите YES, иначе выведите NO. Напомним, что в соответствии с григорианским календарем, год является високосным, 
если его номер кратен 4, но не кратен 100, а также если он кратен 400
'''

while True:
    try:
        def is_year_leap(year):
            if year <= 1580:
                 print('Not within the Gregorian calendar period')
            elif year / 4 == year // 4:
                if year / 100 != year // 100:
                    return print('Yes')
                elif year == 2000:
                    return print('Yes')
                else:
                    print('No')
            elif year / 400 == year // 400:
                return print('Yes')
            else:
                return print('No')

        year = int(input("Please, enter your year: "))
        is_year_leap(year)

    except ValueError:
            print('Sorry , you did some mistakes, please re-write it again.')

#5
'''
    Дано положительное действительное число X. Выведите его первую цифру после десятичной точки.
'''


while True:
    import math
    try:
        x = float(input('Please, enter positive real number: '))
        a = int(x)
        y = (round(x - a, 999)) * 10
        print(math.floor(y))
    except:
        print('Something went wrong, try again, please')


''' II '''
try:
    x = float(input('Please, enter positive real number: '))
    y = str(x)
    print(y.split('.')[1][0])
except:
    print('Something went wrong, try again, please')


''' III '''
try:
    x = float(input('Please, enter positive real number: '))
    y = str(x)
    a = y.split('.')[1]
    for i in range(len(a)):
        if i == 0:
            print(a[i])
        else:
            break
except:
    print('Something went wrong, try again, please')


#6
''''''
'''
Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!.
По данному натуральному n вычислите значение n!. Пользоваться математической библиотекой math в этой задаче запрещено.
'''


try:
    a = int(input('Please, enter a number:'))
    factorial = 1
    for i in range(1, a+1):
        factorial = i * factorial
    print(a, "!", "=", factorial)
except:
    print('Something went wrong, try again, please')




#7
'''
Дано два числа a и b. Выведите гипотенузу треугольника с заданными катетами.
'''
import math
try:
    def third_side_hypotenuse(a, b):
        c = math.sqrt(a**2 + b ** 2)
        return c

    a = float(input('Please enter first side (cathetus) of your right-angled triangle:'))
    b = float(input('Please enter the second side (cathetus) of your right-angled triangle:'))

    print(f'Your third side(hypotenuse) of your right_angled triangle equal: {third_side_hypotenuse(a,b)}')

except ValueError:
    print('Sorry , but you did some mistakes, please re-write it again.')

#8
'''
Дано N чисел: сначала вводится число N, затем вводится ровно N целых
чисел. Подсчитайте количество нулей среди введенных чисел и
выведите это количество. Вам нужно подсчитать количество чисел,
равных нулю, а не количество цифр.
# '''
import math
from random import randint

num = random.randint(1, 10)
print(num)
c = []
count = 0
new = '0'

try:
    for i in range(num):
        a = int(input('Please, enter your number:'))
        c.append(a)

    for x in c:
        new = str(x)
        for i in range(len(new)):
            if new[i] == '0':
                count += 1

    print(count)
except:
    print('Sorry , but you did some mistakes, please re-write it again.')




#9
'''
Дана строка, состоящая ровно из двух слов, разделенных пробелом.
Переставьте эти слова местами. Результат запишите в строку и
выведите получившуюся строку.
При решении этой задачи не стоит пользоваться циклами и инструкцией if.
'''
words = str(input("please, enter two words:")) # hello world
new_word = words.split()

try:
    a = new_word[2]
    print('sorry,you entered more then two words')
except:
    print(new_word[1], new_word[0])

#10
'''
Дана строка. Найдите в этой строке второе вхождение буквы
f ,и выведите индекс этого вхождения. Если буква
f  в данной строке встречается только один раз, выведите число -1
, а если не встречается ни разу, выведите число -2.
'''
words = str(input("please, enter two words:"))
num = 0
if words.count('f') == 1:
    print(-1)
elif words.count('f') > 1:
    for i in range(len(words)):
        if words[i] == "f":
            num += 1
            if num == 2:
                print("the index of the second 'f' is:", [i])
else:
    print(-2)

#11
'''
Дана строка, состоящая ровно из двух слов, разделенных пробелом.
Переставьте эти слова местами. Результат запишите в строку и
выведите получившуюся строку.
При решении этой задачи не стоит пользоваться циклами и инструкцией if.
'''

words = str(input("please, enter two words:"))
new_word = words.split()

try:
    a = new_word[2]
    print('sorry,you entered more then two words')
except:
    print(new_word[1], new_word[0])
#12
'''
12.Программа получает на вход последовательность целых
неотрицательных чисел, каждое число записано в отдельной строке.
Последовательность завершается числом 0, при считывании которого
программа должна закончить свою работу и вывести количество
членов последовательности (не считая завершающего числа 0). Числа,
следующие за числом 0, считывать не нужно.
'''

import math
from random import randint
count = 0
for i in range(7):
    num = random.randint(0, 10)
    if num == 0:
        break
    else:
        c = (num,'\n')
        count += 1
        print(num)
print("the number of numbers are:", count)



#13
'''
.Последовательность состоит из натуральных чисел и завершается
числом 0. Определите, сколько элементов этой последовательности
больше предыдущего элемента.
'''
try:
    number_1 = int(input("Please, enter your first number :"))
    count = 0
    number_a = number_1
    while number_1 != 0:
        next_number = int(input("Please, enter your number again:"))
        if next_number != 0 and number_a < next_number:
            count += 1
            number_a = next_number
        elif next_number == 0:
            break
        else:
            number_a = next_number
            continue
    print(count)
except:
    print("Sorry, there is a problem, lets try to re-write your numbers")


#14
'''
.Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т.д.). 
Если элементов нечетное число, то последний элемент остается на своем месте.
'''

list_1 = list(input("Please, write your list of numbers:"))
new_list = []
print(list_1)
for i in range(len(list_1)):
    if i == 0:
        continue
    elif i % 2 == 0:
        if i == list_1.index(list_1[-1]):
            new_list.append(list_1[i])
        elif i == list_1.index(list_1[-2]):
            new_list.append(list_1[i+1])
        else:
            continue
    elif i % 2 != 0:
        if i == list_1.index(list_1[-1]):
            new_list.append(list_1[i - 1])
        else:
            new_list.append(list_1[i])
            new_list.append(list_1[i-1])
    elif i == list_1[-1]:
        new_list.append(list_1[i])
print(new_list)


#15
'''
Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.
'''

list_1 = [1, 2, 3, 4, 4, 5, 5, 5, 6, 7, 7,35]
New_list = len(set(list_1))
print(f'различных элементов: {New_list}')







