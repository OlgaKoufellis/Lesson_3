# list (списокб массив) б тип хранения в памяти
#
# l = [1,2,3,3.3 , True, False ]
# l = []
# l =list()
# fruits = ['Apple', 'Pear','Peach', 'Mellon','Watermelon','Grape', 'Avocado']
# print(fruits[-1]) #avocado
# print(fruits[0])# apple
# print(fruits[0:4]) #'Apple', 'Pear','Peach', 'Mellon'
# print(fruits[3])#mellon
# fruits[0] = 'Pineapple'
# print(fruits)

# fruits = ['Apple', 'Pear','Peach', 'Mellon','Watermelon','Grape', 'Avocado']
# fruits[4] = 'Plum'
# fruits[-2] = 'Strawberry'
# print(fruits)

#функции списков
colors = ['Red', 'Green', 'Blue', 'Yellow']
print(colors)
colors.append('Orange')# добавляет что-тоо в список add to the end of list
print(colors)
log = colors.pop(1)
print(log)
print(colors)


# colors = colors[::1]
# print(colors)
# colors.append('Pink')
# print(colors)
# colors = colors[::-1]
# print(colors)
# colors.pop(0)# Delet from th eposition of list
# print(colors.pop(0))
# print(colors)
# colors.insert(2,'Purple')# add to the possition of list
# print(colors)
# colors.pop(0)# Delet from th eposition of list
# print(colors.pop(0))


# colors.remove('Red') - удаляет по содержимому первое вхождение
# print(colors)
# print('Pinky' in colors)
# new_colors = colors
# print(colors)
# colors.append('Light_blue')
# print(new_colors)

# real_colors = colors[:]
# print(colors)
# colors.append('beige')
# print(real_colors)
# real_colors.pop(0)
# real_colors.pop(0)
# print(colors)
# print(real_colors)





'''
Задание 1
В списке целых, заполненном случайными числами
вычислить:
■ Сумму отрицательных чисел;
■ Сумму четных чисел;
■ Сумму нечетных чисел;
■ Произведение элементов с индексами кратными 3;
■ Произведение элементов между минимальным и
максимальным элементом;
■ Сумму элементов, находящихся между первым и последним положительными элементами.
'''
numbers = [-2, 1, 2, 3, 4, 5,-7, 99, 33, -23, 0, 45, 9, -1]
sum_neg = 0
sum_even = 0
sum_odd = 0
for number in numbers:
    if number < 0:
        sum_neg = sum_neg + number
    if number % 2 == 0 and number != 0:
        sum_even = sum_even +number
    elif number % 2 != 0 and number != 0:
        sum_odd = sum_odd + number
print(sum_neg, sum_even, sum_odd)
#print(0%2)  # при проверкетна четность будет считаться сетным
multiply_3 = 1
multiply_min_max = 1
minimum = numbers[0]
maximum = numbers[0]
for index in range(len(numbers)):
    if i % 3 == 0 and index != 0:
        mult = multiply_3 * numbers[index]
    if minimum > numbers[index]:
        minimum = numbers[index]
    if maximum < numbers[index]:
        maximum = numbers[index]
for number in range(len(numbers)):
    if i % 3 == 0 and index != 0:
        mult = multiply_3 * numbers[index]


# list список (массив) *двусвязанный список (тип хранения в памяти)
# #итерируемый тип данных\ изменяемый тип данных\ индексируемый

# l = [1,2,3.3,True,False,'FFF']
# l = []
# l = list()
# fruits = ['Apple','Pear','Peach','Mellon','Watermellon','Grape']
# print(fruits[0])#'Apple'
# print(fruits[3])#'Mellon'
# print(fruits[-1])#'Grape'
# print(fruits[0:3])#['Apple', 'Pear', 'Peach']
# print(fruits[0:3])
# fruits[0] = 'Pineapple'
# print(fruits)
# fruits[5] = 'Pomelo'
# fruits[4] = 'Orange'
# print(fruits)

colors = ['Red', 'Green', 'Blue']
print(colors)
colors.append('Orange')  # Add to the end of list
# Append to start of list
# colors = ['Red','Green','Blue']
# print(colors)
# colors = colors[::-1]
# print(colors)
# colors.append('Yellow')
# print(colors)
# colors = colors[::-1]
# print(colors)
# print(colors)
colors.insert(2, 'Yellow')  # Add to the position of list
# print(colors)
# colors.pop()#Delete from the end of list
# print(colors)
# colors.pop(0)#Delete from the position of list
# print(colors.pop(0))
# print(colors)
# del colors len(color)
# colors.remove('Green')#Delete by the name
# print(colors)
# print('Purle' in colors)
# print(len(colors))
new_colors = colors
# print(colors)
# print(new_colors)
# colors.append('Pink')
# print(colors)
# print(new_colors)
# new_colors.append('Cyan')
# print(colors)
# print(new_colors)
# real_colors = colors[:]
# print(colors)
# print(real_colors)
# real_colors.pop(0)
# colors.pop()
# print(colors)
# print(real_colors)
# real_colors.pop(0)
# real_colors.pop(0)
# print(colors)
# print(real_colors)

'''Задание 1
В списке целых, заполненном случайными числами
вычислить:
■ Сумму отрицательных чисел;
■ Сумму четных чисел;
■ Сумму нечетных чисел;
■ Произведение элементов с индексами кратными 3;
■ Произведение элементов между минимальным и
максимальным элементом;
* Сумму элементов, находящихся между первым и 
последним положительными элементами.'''
numbers = [1, 2, 3, 4, -5, 6, 35, -1, -4, 9, 20, 21, 15]
sum_neg = 0
sum_even = 0
sum_odd = 0
for number in numbers:
    if number < 0:
        sum_neg = sum_neg + number
    if number % 2 == 0 and number != 0:
        sum_even = sum_even + number
    elif number % 2 != 0 and number != 0:
        sum_odd = sum_odd + number
print(sum_neg,sum_odd,sum_even)
# print(0%2)#0 при проверке на чётность, будет считаться чётном
mult_3 = 1
mult_min_max = 1
minimum = numbers[0]
minimum_index = 0
maximum = numbers[0]
maximum_index = 0
for index in range(len(numbers)):
    if index % 3 == 0 and index != 0:
        mult_3 = mult_3 * numbers[index]
    if minimum < numbers[index]:
        minimum = numbers[index]
        minimum_index = index
    if maximum > numbers[index]:
        maximum = numbers[index]
        maximum_index = index
mult_numbers = []
# numbers = [100, 2, 3, 4, -5, 6, 35, -1, -4, 9, 20, 21, 15]
# print(numbers[4:0+1:-1])
#               0        4       6
if maximum_index < minimum_index:
    mult_numbers = numbers[maximum_index:minimum_index+1]
else:
    mult_numbers = numbers[minimum_index:maximum_index+1]

for number in mult_numbers:
    mult_min_max = mult_min_max * number
print(mult_min_max)





# colors.  - смотрим все методы списов





numbers = [1, 2, 3, 4, -5, 6, 5, -1, -4, 9, 20, 21, 15]
sum_neg = 0
sum_even = 0
sum_odd = 0
for number in numbers:
    if number < 0:
        sum_neg = sum_neg + number
    if number % 2 == 0 and number != 0:
        sum_even = sum_even + number
    elif number % 2 != 0 and number != 0:
        sum_odd = sum_odd + number
print(sum_neg, sum_odd, sum_even)





