'''
Модуль 4. Строки. Списки. Часть 2
'''

'''
Задание 1:
Пользователь вводит с клавиатуры арифметическое выражение. Например, 23+12.
Необходимо вывести на экран результат выражения. В нашем примере это 35. 
Арифметическое выражение может состоять только из трёх частей: число, операция, число. Возможные операции: +, -,*,/
'''
arithmetic_expression = '236+12'
operation = ['+', '-', '*', '/']
new = ''
for index in operation:
    if arithmetic_expression.count(index) == 1:
        for i in range(len(arithmetic_expression)):
            if arithmetic_expression[i] != index:
                new = new + arithmetic_expression[i]
            if arithmetic_expression[i] == index:
                a = int(new)
                new = ''
        b = int(new)
        if index == '+':
            print(a + b)
        if index == '-':
            print(a - b)
        if index == '/':
            print(a / b)
        if index == '*':
            print(a * b)
    else:
        break


a = '230/12'
my_list = ['+','-','*','/']
suma = 0
for i in my_list:
    if a.count(i) == 1:
        new_list = a.split(i)
        if i == '+':
            suma = int(new_list[0]) + int(new_list[1])
        elif i == '-':
            suma = int(new_list[0]) - int(new_list[1])
        elif i == '*':
            suma = int(new_list[0]) * int(new_list[1])
        elif i == '/':
            suma = int(new_list[0]) / int(new_list[1])
print(round(suma, 2))



'''
Задание 2:
В списке целых, заполненном случайными числами, определить минимальный и максимальный элементы, 
посчитать количество отрицательных элементов, посчитать количество положительных элементов, 
посчитать количество нулей. Результаты вывести на экран.
'''
my_list = [1, 2, 4, -7, 9, 24, -11]
positive_element = 0
negative_element = 0
zero = 0
max_number = my_list[0]
min_number = my_list[0]
for number in my_list:
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number
    if number > 0:
       positive_element = positive_element + 1
    if number < 0:
        negative_element +=1
    if number == 0:
        zero += 1
print('max_number is:', max_number,'\nmin_number is:', min_number, '\npositive_elements : ', positive_element,
      '\nnegative_elements : ', negative_element, '\nzero : ', zero)

