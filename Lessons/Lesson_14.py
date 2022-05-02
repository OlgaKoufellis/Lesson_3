'''Задание 4   ***
Пользователь вводит с клавиатуры строку и слово
для поиска. Посчитайте сколько раз в строке встречается
искомое слово. Полученное число выведите на экран. (без использования метода count)
'''


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
#




# s = 'Abrakadabra'
# symbol = 'ra'
# print(s.count(symbol))
'''Задание 5
Пользователь вводит с клавиатуры строку, слово для
поиска, слово для замены. Произведите в строке замену
одного слова на другое. Полученную строку отобразите
на экране.
* Без использования метода replace'''

s = '1chairghdcdfchaircdchfchair'
symbol = 'chair'
new_symbol = '*CHAIR*'
first_symbol = symbol[0]
new_line = ''
i = 0
while i != len(s):
    if s[i] == first_symbol:
        if symbol == s[i:i + len(symbol)]:
            new_line = new_line + new_symbol
            i = i + len(symbol)
        else:
            new_line += s[i]
            i += 1
    else:
        new_line += s[i]
        i += 1
print(new_line)


# s = 'Abrakadabra'
# symbol = 'ra'
# new_symbol = 'RA'
# print(s.replace(symbol,new_symbol))
#
# print(s)
#
#
# s = 'Hello123'
# print(a.isalnum) # проверяет на наличие символов
#

'''Задание 1
Есть некоторый текст. Реализуйте следующую функциональность:
■ Изменить текст таким образом, чтобы каждое предложение начиналось
с большой буквы;
■ Посчитайте сколько раз цифры встречаются в тексте;
■ Посчитайте сколько раз знаки препинания встречаются в тексте;
■ Посчитайте количество восклицательных знаков в
тексте.'''

# symbols = '.,?!'
# numbers = '0123456789'
# t = 'some interesting, text and else. what i am doing. how do you do? i am fine! thank you.'
# count_numbers = 0
# count_symbols = 0
# count = 0
# for i in range(len(t)):
#     a = t[i]
#     for l in range(len(symbols)):
#         if a == symbols[l]:
#             count_symbols = count_symbols + 1
#     for n in range(len(
#
#     )):
#         if a == numbers[n]:
#             count_numbers = count_numbers + 1
#     if t[i] == '!':
#         count += 1
# print(count_numbers,count_symbols, count)

#
#
# t = 'some interesting, text and else. what i am doing. how do you do? i am fine! thank you.'
# t = t.capitalize()
# symbols = '!.?'
# for i in range(2, len(t)):
#     for s in range(len(symbols)):
#         # print(t[i - 2:i])
#         if t[i - 2:i] == (symbols[s] + ' '):
#             # print('y')
#             t = t[:i] + t[i].upper() + t[i + 1:]
# print(t)
# s = 'Hello World!'
# print(s[0:5])#Hello
# print(s[-6:-1])#World
# print(s[-6:])#World!
# print(s[:5])#Hello
# print(s[::-1])#!dlroW olleH





