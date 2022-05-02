# Задание 1
# Пользователь вводит с клавиатуры три числа.
# В зависимости от выбора пользователя программа выводит
# на экран сумму трёх чисел или произведение трёх чисел.

n1 = int(input('Please fill in the first number:'))
n2 = int(input('Please fill in the second number:'))
n3 = int(input('Please fill in the third number:'))
n4 = input('Please fill in a sign (+,-,/,*):')
if n4 == '+':
 print(n1 + n2 + n3)
elif n4 == '-':
 print(n1 - n2 - n3)
elif n4 == '*':
 print(n1 * n2 * n3)
elif n4 == '/':
  if n2 != 0 and n3 != 0:
    print(n1 / n2 / n3)
  else:
    print('Error')
else :
 print('Please try again')

#Задание 2
# Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя
# программа выводит на экран максимум из трёх, минимум из трёх или среднеарифметическое трёх чисел.
n1 = int(input('Please fill in the first number:'))
n2 = int(input('Please fill in the second number:'))
n3 = int(input('Please fill in the third number:'))
print('Max number is: ', max(n1 , n2, n3))
print('Min number is: ', min(n1 , n2, n3))
print('Average is: ', (n1 + n2 + n3)/3)

#Задание 3
# Пользователь вводит с клавиатуры количество метров.
# В зависимости от выбора пользователя программа переводит метры в мили, дюймы или ярды.
meter = int(input("Enter your count of meters : "))
mile = meter * 0.00062137
inch = meter * 39.3701
yard = meter / 0.9361
print("entered meters are: ", meter,"m" ,"\nmiles are :", mile ,"mi", "\ninches are: ", inch , "in",  "\nyards are:", yard,"yd",)

