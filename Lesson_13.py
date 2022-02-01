# #str методы строк
# #итерируемый тип данных
# h = "Hello World"
# print(h)  #строка итерированные строки данных
# print(h[0])
# h = h + '?'
# print(h)
# print(h[0])
# print(h[1])
# print(h[2])
# print(h[3])

a ='Andreichenko Olga Vyacheslavovna'
a = a.upper()
print(a[0],a[1], a[2], a[3],a[4], a[19]) #Andrey
print(a[6],a[7], a[8],a[8], a[24], a[23]) #cheese
print(a[6],a[7], a[0], a[5], a[3]) #chair


'''
Задание 1
Пользователь вводит с клавиатуры строку. Произведите поворот строк и полученный результат выведите
на экран.
'''
# s = 'hello World!'
# print(len(s))
# for i in range(len(s)):
#     print(s[i])

# s = 'hello World!'
# rs = ''
# print(len(s))
# for i in range(len(s)):
#     rs = s[i] + rs
# print(rs)


# s = 'Hello World!'
# for i in range(1,len(s)+1):
#     print(s[-i])

'''
Задание 2
Пользователь вводит с клавиатуры строку. Посчитайте количество букв, 
цифр в строке. Выведите оба
количества на экран.

'''
#
# letters = 'abcdefghijklmnopqrstuvxyz'
# numbers = '0123456789'
# s = 'hello123'
# count_numbers = 0
# count_letter = 0
# for i in range(len(s)):
#     print(s[i])
#     a = s[i]
#     for l in range(len(letters)):
#         if a == letters[l]:
#             count_letter = count_letter + 1
#     for n in range(len(numbers)):
#         if a == numbers[n]:
#             count_numbers = count_numbers + 1
# print(count_numbers,count_letter)
#


# number = '9'
# print(number.isnumeric())
# print(number.isalpha())

# s = 'hello123'
# count_numbers = 0
# count_letters = 0
# for i in range(len(s)):
#     print(s[i])
#     a = s[i]
#     if a.isnumeric():
#         count_letters = count_letters + 1
#     if a.isalpha():
#         count_numbers = count_numbers + 1
# print(count_numbers,count_letters)



# s = 'hello123'
# count_numbers = 0
# count_letters = 0
# for i in range(len(s)):
#     print(s[i])
#     a = s[i]
#     if a.isalpha():
#         count_letters = count_letters + 1
#     if a.isnumeric():
#         count_numbers = count_numbers + 1
# print(count_numbers,count_letters)

'''
Задание 3
Пользователь вводит с клавиатуры строку и символ
для поиска. Посчитайте сколько раз в строке встречается
искомый символ. Полученное число выведите на экран.
'''
# s = 'Abrakadabra'
# symbol = 'a'
# count = 0
# for i in range(len(s)):
#     if symbol == s[i]:
#         count = count + 1
# print(count)
#
# print(s.count(symbol))


# s = 'Abrakadabra'
# symbol = 'ra'
# print(s.count(symbol))