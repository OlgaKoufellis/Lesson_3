# and not or
# вывести 3 переменных если вске они равны.
#a =2
#b =3
#c =4
#    if a== b == c:
#        print(3)
#    elif(a == b):
#        print(2)
#   elif(b == c):
#        print(2)
#   elif(a == c):
#        print(2)
#    else:
#        print(0)
#
#a =2
#b =3
#c =4
#    if a>= b >= c:
#        print(a)
#      if b >= c:
#        print(b)
#        print(c)
#    else:
#        print(b)
#       print(b)


x = 0
y = 0
if x > 0:
    if y > 0:
      print('1')
    elif y < 0:
      print('4')
    elif y == 0:
      print('0')
elif x < 0:
      if y < 0:
       print('3')
      elif y > 0:
        print('2')
      elif y == 0:
        print('0')
elif x == 0:
    if y < 0:
        print('0')
    elif y > 0:
        print('0')
    elif y == 0:
        print('00')

#AND  - запинается на лжи
T and T >> True
T and F >> False
f and t >> False
f and f >> False
a and b and c
#OR -  запинается на правде
T or T >> True
T or F >> False
f or t >> False
f or f >> False
a or b or c
(a and b) or (c and d) or (e and f)

a =2
b =3
c =4
   if a== b and b == c:
        print(3)
    elif a == b or b == c or a == c:
        print(2)
    else:
        print(0)

[19:29] Буйлук Андрей
x = 4
y = 0
if x > 0 and y > 0:
    print('I')
elif x > 0 and y < 0:
    print('IV')
elif x < 0 and y < 0:
    print('III')
elif x < 0 and y > 0:
    print('II')
# elif x != 0 and y == 0:
#     print('On Axis X')
elif x > 0 and y == 0:
    print('On Axis X+')
elif x < 0 and y == 0:
    print('On Axis X-')
# elif x == 0 and y != 0:
#     print('On Axis Y')
elif y > 0 and x == 0:
    print('On Axis Y+')
elif y < 0 and x == 0:
    print('On Axis Y-')
elif y == 0 and x == 0:
    print('ZERO')

...адание 1
Пользователь вводит с клавиатуры число. Необходимо проверить его на четность и нечетность. Если число
четное требуется вывести на экран число и надпись Even
number. Если число нечетное выведите на экран число и
надпись Odd number...
print(a)

number = int(input("Enter number : "))
if number == 0:
    print('Zero')
elif number % 2 == 0:
    print('Even')
elif number % 2 != 0:
    print('Odd')
else:
    print('error')

#Задание 2
#Пользователь вводит с клавиатуры число. Необходимо проверить его на кратность 7. Если число кратно
#требуется вывести на экран число и надпись Number is
#multiple 7. Если число не кратно выведите на экран число
#и надпись Number is not multiple 7.
number = int(input("Enter number : "))
if number == 0:
    print("0")
elif number % 7 == 0:
    print('Number is multiple 7 :' , number)
elif number % 7 != 0:
    print(number , 'number is not multiple 7')
else:
    print('error')

a = 5
b = 4
c = 3
d = 2
e = 1
if a >= b :
    if b >= c:
        if c >= d:
            if d >= e :

if a >= b and b >= c and  c >= d and d >= e :
    ssh - keygen - t
    rsa - b
    4096 - C
