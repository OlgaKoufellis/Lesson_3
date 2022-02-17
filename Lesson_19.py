# def simple(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
# l = [1,2,3]
# print(l.pop())
#
# print(l.append(4))
#
# def pop(somelist):
#     return somelist.pop()
#
# def append(somelist, data):
#     return somelist.append(data)
#
# l = [1,2,3]
# print(pop(l))
# print(append(l,4))
# print(l)
#
# #Рекукрсия
#
# # Return > Break
# def somefunction():
#     return 'Something'
#     print('you cant see this in cinsole')
#
# while False:
#     print('you cant see this in cinsole')
# if False:
#     print('you cant see this in cinsole')
#
# def calc(a,b):  # позиционные аргументы
#     return a + b
# print(calc(2,2))


# def calc1(a,b, с=6):  # аргументы по умолчанию
#     return a + b + с
# print(calc1(2,2))
#



#range(start,finish,step)
# def custom_range(start,finish=False,step=False):
#     numbers = []
#     if finish:
#         if start < finish:
#             while start != finish:
#                 numbers.append(start)
#                 if step:
#                     start = start + step
#                 else:
#                     start = start + 1
#         elif start > finish:
#             while start != finish:
#                 numbers.append(start)
#                 if step:
#                     start = start + step
#                 else:
#                     return numbers
#     else:
#         n = 0
#         while n < start:
#             numbers.append(n)
#             n = n + 1
#     return numbers
#
# for i in range(1,12,1):
#     print(i,end=' ')
# print()
# for i in custom_range(1,12,1):
#     print(i, end=' ')



# def custom_range(value_start,value_end = False,step = 1):
#     numbers = []
#     if value_end:
#         if value_start > value_end:
#             while value_start < value_end:
#                 numbers.append[value_end]
#                 if step:
#                     value_start = value_start + step
#                 else:
#                     value_start = value_start + 1
#             else:
#                 while 0 < value_start:
#                     numbers.append[value_start]
#                     value_start = value_start + 1
#             return(numbers)
#
# print(1,range(10))
# print(2, custom_range(10))


# функция рендж без функции рендж
# def custom_range(start,finish=False,step=False):
#     numbers = []
#     if finish:
#         if start < finish:
#             while start != finish:
#                 numbers.append(start)
#                 if step:
#                     start = start + step
#                 else:
#                     start = start + 1
#         elif start > finish:
#             while start != finish:
#                 numbers.append(start)
#                 if step:
#                     start = start + step
#                 else:
#                     return numbers
#     else:
#         n = 0
#         while n < start:
#             numbers.append(n)
#             n = n + 1
#     return numbers
#
# for i in range(1,12,1):
#     print(i,end=' ')
# print()
# for i in custom_range(1,12,1):
#     print(i, end=' ')

#
# def custom_range(start,finish=False,step=False):
#     numbers = []
#     if finish:
#         if start < finish:
#             while start != finish:
#                 numbers.append(start)
#                 if step:
#                     start = start + step
#                 else:
#                     start = start + 1
#         elif start > finish:
#             while start != finish:
#                 numbers.append(start)
#                 if step:
#                     start = start - step
#                 else:
#                     return numbers
#     else:
#         n = 0
#         while n < start:
#             numbers.append(n)
#             n = n + 1
#     return numbers
#
# for i in range(1,12,1):
#     print(i,end=' ')
# print()
# for i in custom_range(12,1,1):
#     print(i, end=' ')




# print(calc1(2,2))
#range(start,finish,step)
# def custom_range(start,finish=False,step=False):
#     numbers = []
#     if finish:
#         if start < finish:
#             while start != finish:
#                 numbers.append(start)
#                 if step:
#                     start = start + step
#                 else:
#                     start = start + 1
#         elif start > finish:
#             while start != finish:
#                 numbers.append(start)
#                 if step:
#                     start = start + step
#                 else:
#                     return numbers
#     else:
#         n = 0
#         while n < start:
#             numbers.append(n)
#             n = n + 1
#     return numbers

'''
Задание 7
Напишите функцию, которая проверяет является
ли шестизначное число «счастливым». Число передаётся в качестве параметра. Если число счастливое нужно
вернуть из функции true, иначе false.
«Счастливое шестизначное число» — это число у которого сумма первых трёх цифр равна сумме трёх вторых
цифр. Например, 123420 – счастливое 1+2+3 = 4+2+0,
а 723422 – несчастливое 7+2+3 != 4+2+2.

* любая длинна числа 
123|456  1234|5|6789
'''
def numbers(number):
    res = len(number) // 2
    count1 = 0
    count2 = 0
    for i in number[:res: +1]:
        count1 = count1 + int(i)
    print('count1: ',  count1)
    for j in number[:res:-1]:
        print(j)
        count2 = count2 + int(j)
    print('count:', count2)
    if count1 == count2:
        print('Lucky!!!)))')
    else:
        print('Unlucky!!!(((')

numbers(str('123456789'))


#
# def numbers(number):
#     number = str(number)
#     if number.isnumeric():
#         number = int(number)
#         n1 = (number)//100000
#         n2 = ((number)//10000)%10
#         n3 = ((number)//1000)%10
#         n4 = ((number)//100)%10
#         n5 = ((number)//10)%10
#         n6 = ((number)//1)%10
#         if n1 + n2 + n3 == n4 + n5 + n6:
#
#             return True
#         else:
#             return False


# result = numbers(123420)
# print(numbers)
# print(result)










# def numbers(number):
#     number = str(number)
#     if number.isnumeric():
#         number = int(number)
#         n1 = (number)//100000
#         n2 = ((number)//10000)%10
#         n3 = ((number)//1000)%10
#         n4 = ((number)//100)%10
#         n5 = ((number)//10)%10
#         n6 = ((number)//1)%10
#         if n1 + n2 + n3 == n4 + n5 + n6:
#             print(True)
#             return True
#         else:
#             print(False)
#             return False
#
#
# numbers(123420)