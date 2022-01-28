'''
Задание 1
Пользователь вводит с клавиатуры два числа (начало и конец диапазона).
Требуется проанализировать все числа в этом диапазоне по следующему правилу:
если число кратно 7, его надо выводить на экран.
'''
# num1 = int(input('Please, enter the first number: '))
# num2 = int(input('Please, enter the second number: '))
# for i in range(num1,num2 + 1):
#     if i / 7 != i // 7:
#         continue
#     else:
#         print(i)

'''
Задание 2 Пользователь вводит с клавиатуры два числа (начало и конец диапазона). 
Требуется проанализировать все числа в этом диапазоне. Нужно вывести на экран:
1. Все числа диапазона;
2. Все числа диапазона в убывающем порядке;
3. Все числа, кратные 7;
4. Количество чисел, кратных 5.
'''
num1 = int(input('Please, enter the first number: '))
num2 = int(input('Please, enter the second number: '))
num0 = 0
count = 0
print('1)', end='')
for i in range(num1,num2 +1):
    if i == num2:
        print(i)
    else:
        print(i, end=', ')
print('3)', end='')
for i in range(num1,num2 +1):
    if i / 7 != i // 7:
        continue
    else:
        print(i, end=', ')
for i in range(num1, num2 + 1):
    if i / 5 != i // 5:
        continue
    else:
        count += 1
print('\n4)',count)
if num2 > num1:
    num0 = num1
    num1 = num2
    num2 = num0
    for i in range(num2,num1 + 1) :
        if i == num1:
            print(i)
        else:
            print(i, end=', ')