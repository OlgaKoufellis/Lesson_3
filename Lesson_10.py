#a = 1
# b = 10
# for i in range(a, b+1):
#     print(i)
#     if i == 5:
#         break
#
# a = 1
# b = 10
# for i in range(a, b+1):
#     if i == 5:
#         break
#     print(i)
#
#
# a = 1
# b = 10
# for i in range(a, b+1):
#     if i == 5:
#         continue
#     print(i)
'''
Задание 3
Пользователь вводит с клавиатуры две границы диапазона и число. Если число не попадает в диапазон,
программа просит пользователя повторно ввести число,
и так до тех пор, пока он не введет число правильно. Программа отображает все числа диапазона, выделяя число
восклицательными знаками. Например:
1 2 3 !4! 5 6 7.
# '''
# a = 1
# b = 7
# guess = 4
# if a <= guess and b <=b :
#    for i in range(a,b +1):
#       if i == guess:
#             print('!', i, '!', sep='', end='')
#       else:
#             print( i, end ='')
#
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
# height = 3
# symbol = '*'
# for i in range(height):
#    print(width * symbol)

# a = int(input("Height ?:"))
# b = int(input("Width ?:"))
# symbol = "*"
# for i in range(a):
#     print(symbol *  b)

'''
Задание 3
Пользователь вводит с клавиатуры размер стороны
квадрата. Требуется отобразить на экран незаполненный квадрат (отображаются только границы квадрата).
Размер стороны равен введённому размеру.
# '''
width = 5
height = 5
symbol = '*'
s = ' '
for i in range(height):
   if  i == 0 or i == (height - 1):
      print(width * symbol)
   else:
      print( symbol + ((width - 2) * s) + symbol)


import random
width = 3
height = 3
for i in range(height):
   sym = random.randint(1,9)
   for j in range(width):
      print(f"{sym}", end=' ')
   print()
