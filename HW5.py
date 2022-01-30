'''Задание 1 Пользователь вводит с клавиатуры число в диапазоне от 1 до 100. Если число кратно 3 (делится на 3 без остатка) нужно вывести слово Fizz. Если число кратно 5 нужно вывести слово Buzz. Если число кратно 3 и 5 нужно вывести Fizz Buzz. Если число не кратно не 3 и 5 нужно вывести само число.

Если пользователь ввел значение не в диапазоне от 1 до 100 требуется вывести сообщение об ошибке.
'''


number = int(input('Please fill in the number from 1 to 100: '))
if number % 3 == 0:
    if number % 5 == 0:
        print('FizzBuzz')
    else:
        print("Fizz")
elif number % 5 == 0:
    print('Buzz')
else:
    print(number)


'''Задание 2
Написать программу, которая по выбору пользователя возводит
введенное им число в степень от нулевой до седьмой включительно.'''


a = int(input('Please enter a number: '))
b = 0
while b <= 7:
    print(a ** b)
    b += 1

'''Задание 3
Написать программу подсчета стоимости разговора для разных мобильных операторов.
Пользователь вводит стоимость разговора и выбирает с какого на какой оператор он звонит.
Вывести стоимость на экран.'''

duration = float(input('Please enter, duration in minutes:'))
o1 = input('Please eneter operator 1 (Life, KS, MTC) :')
o2 = input('Please eneter operator 2 (Life, KS, MTC) :')
mins = duration // 1
sec = duration - mins
duration = mins * 60 + sec
if sec >= .6:
    print('Please enter the correct number of duration!!!')
elif o1 == o2:
    price = 0
    print(round((duration * price) / 60, 2) )
elif o1 == 'KS' and o2 == 'MTC':
    price = 1.1
    print(round((duration * price) / 60, 2) )
elif o1 == 'KS' and o2 == 'Life':
    price = 1.5
    print(round((duration * price) / 60, 2) )
elif o1 == 'Life' and o2 == 'MTC':
    price = 2.0
    print(round((duration * price) / 60, 2) )
elif o1 == 'Life' and o2 == 'KS':
    price = 2.2
    print(round((duration * price) / 60, 2) )
elif o1 == 'MTC' and o2 == 'KS':
    price = 1.8
    print(round((duration * price) / 60, 2) )
elif o1 == 'MTC' and o2 == 'Life':
    price = 1.8
    print(round((duration * price) / 60, 2) )
else:
    print('ERROR')

'''
Задание 4
Зарплата менеджера составляет 200$ + процент от продаж, продажи до 500$ — 3%, от 500 до 1000 — 5%,
свыше 1000 — 8%. Пользователь вводит с клавиатуры уровень продаж для трех менеджеров.
Определить их зарплату, определить лучшего менеджера, начислить ему премию 200$, вывести итоги на экран.
'''
salary = 200
m1 = int(input('Please fill in m1'))
m2 = int(input('Please fill in m2'))
m3 = int(input('Please fill in m3'))
if m1 < 500:
    bonus = 3
elif m1 >= 500 and m1 < 1000:
    bonus = 5
else:
    bonus = 8
s1 = (salary + (m1 * bonus) / 100)
print(s1)
if m2 < 500:
    bonus = 3
elif m2 >= 500 and m2 < 1000:
    bonus = 5
else:
    bonus = 8
s2 = (salary + (m2 * bonus) / 100)
print(s2)
if m3 < 500:
    bonus = 3
elif m3 >= 500 and m3 < 1000:
    bonus = 5
else:
    bonus = 8
s3 = (salary + (m3 * bonus) / 100)
print(s3)
s_max = (max (s1 , s2, s3))
print(s_max,'\n', s_max + 200)





