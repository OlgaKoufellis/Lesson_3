'''Задание 4
Пользователь вводит с клавиатуры строку и слово
для поиска. Посчитайте сколько раз в строке встречается
искомое слово. Полученное число выведите на экран.
* Без использования метода count'''

# s = 'chairghdcdfchaircdchfchair'
# symbol = 'chair'
# r = symbol[0]
# count = 0
# for i in range(len(s)):
#     if s[i] == r:
#         if symbol == s[i:i + len(symbol)]:
#             count += 1
#         else:
#             continue
# print(count)


'''Задание 5
Пользователь вводит с клавиатуры строку, слово для
поиска, слово для замены. Произведите в строке замену
одного слова на другое. Полученную строку отобразите
на экране.
* Без использования метода replace'''

# s = '1chairghdcdfchaircdchfchair'
# symbol = 'chair'
# new_symbol = '*CHAIR*'
# first_symbol = symbol[0]
# new_line = ''
# i = 0
# while i != len(s):
#     if s[i] == first_symbol:
#         if symbol == s[i:i + len(symbol)]:
#             new_line = new_line + new_symbol
#             i = i + len(symbol)
#         else:
#             new_line += s[i]
#             i += 1
#     else:
#         new_line += s[i]
#         i += 1
# print(new_line)

'''
■ Сумму элементов, находящихся между первым и последним положительными элементами.

'''
# numbers = [-2, 1, 2, 3, 4, 5,-7, 99, 33, -23, 0, 45, 9, -1]
# new_numbers = 0
# for l in range(len(numbers)):
#     if numbers[l] >= 0:
#         new_numbers = new_numbers + numbers[l]
#     else:
#         continue
# print(new_numbers)

numbers = [-2, 10, 2, 3, 4, 5,-7, 99, 33, -23, 0, 45, -9, -1]
# first_positive = 0
# new_numbers = 0
for l in range(len(numbers)):
    if numbers[l] >= 0:
        first_positive = numbers[l]
        index = l
        break
for a in range(len(numbers)):
    if numbers[a] >= 0:
        last_positive = numbers[a]
        index2 = a
print(sum(numbers[index:index2+1]))

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
