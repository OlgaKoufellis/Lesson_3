# #Задание 1
# # Пользователь вводит с клавиатуры номер дня недели (1-7).
# # Необходимо вывести на экран названия дня недели.
# # Например, если 1, то на экране надпись понедельник, 2 — вторник и т.д.
#
number = input('Please write a day of the week in number from 1 to 7:')
if number  == '1':
 print('Monday')
elif number == '2':
 print('Tuesday')
elif number == '3':
 print('Wednesday')
elif number == '4':
 print('Thursday')
elif number == '5':
 print('Friday')
elif number == '6':
 print('Saturday')
elif number == '7':
 print('Sunday')
else:
 print('ERROR')
#
#
# #Задание 2
# # Пользователь вводит с клавиатуры номер месяца (1-12).
# # Необходимо вывести на экран название месяца.
# # Например, если 1, то на экране надпись январь, 2 — февраль и т.д.
number = input('Please write a number of MONTH (from 1 to 12):')
if number == '1':
 print('January')
elif number == '2':
 print('February')
elif number == '3':
 print('March')
elif number == '4':
 print('April')
elif number == '5':
 print('May')
elif number == '6':
 print('June')
elif number == '7':
 print('July')
elif number == '8':
 print('August')
elif number == '9':
 print('September')
elif number == '10':
 print('October')
elif number == '11':
 print('November')
elif number == '12':
 print('December')
else:
 print('ERROR')
#
# #Задание 3
# # Пользователь вводит с клавиатуры число. Если число больше нуля нужно вывести надпись «Number is positive»,
# # если меньше нуля «Number is negative», если равно нулю «Number is equal to zero»
a_number = input('Please fill in the number :')
if a_number > '0':
 print('Number is positive')
elif a_number < '0':
 print('Number is negative')
elif a_number == '0':
 print('Number is equal to zero')
else:
 print('ERROR')

#Задание 4
# Пользователь вводит два числа. Определить, равны ли эти числа, и, если нет,
# вывести их на экран в порядке возрастания.

Number_1 = input('Please fill in the first number:')
Number_2 = input('Please fill in the second number:')
try:
 Number_1 = int(Number_1)
 Number_2 = int(Number_2)
 if Number_1 == Number_2:
  print('Your numbers are equal :', Number_1 )
 elif Number_1 > Number_2:
  print(Number_2,'\n',Number_1)
 elif Number_1 < Number_2:
  print(Number_1,'\n',Number_2)
except ValueError:
 print('Oooops...Error')
