'''
Задание 1
Напишите функцию, вычисляющую произведение элементов списка целых.
Список передаётся в качестве параметра. Полученный результат возвращается из функции.
'''
def lis(list):
    result = 1
    for i in list:
        result = result * i
    print(result)
    return result



list = [1, 4, 9, 5]
print(lis(list))


'''
Задание 2
 Напишите функцию для нахождения минимума в списке целых. 
 Список передаётся в качестве параметра. Полученный результат возвращается из функции.
'''

def lis(list):
    return min(list)


list = [1, 4, 9, 5]
print(lis(list))


'''
Задание 3 
Напишите функцию, определяющую количество простых чисел в списке целых.
 Список передаётся в качестве параметра. Полученный результат возвращается из функции.
'''


####### оставлю тут свой код ))))

def simple_number(number):
    new_list = []
    count = 0
    for i in number:
        for j in range(2, i + 1):
            if i // j == i / j:
                if i /j != 1:
                    break
            if i / j == 1:
                new_list.append(i)
                count += 1
    print(new_list)
    return count

random_numbers = [10, 4, 9, 5, 7, 1, 15, 89,99]
print(simple_number(random_numbers))





''''
Задание 4
 Напишите функцию, удаляющую из списка целых некоторое заданное число.
  Из функции нужно вернуть количество удаленных элементов.
'''
######## 1
def delete_a_number():

    list_of_numbers = [10, 4, 9, 5, 7, 1, 15, 89, 99, 99]
    list_of_numbers.remove(delete)
    list_of_numbers.remove(delete2)
    print('updated list_of_numbers:', list_of_numbers)
    return('Deleted:', delete, delete2)


delete = 15
delete2 = 99
print(delete_a_number())

######### 2
def delete_a_number(delete):
    list_of_numbers = [10, 4, 9, 5, 7, 1, 15, 89, 99, 99]
    count = 0
    for delete in list_delete:

        while True:
            if delete in list_of_numbers:
                index = list_of_numbers.index(delete)
                list_of_numbers.remove(list_of_numbers[index])
                count += 1
            else:
                break
    print('updated list_of_numbers:', list_of_numbers)
    return('Deleted:', count)


list_delete = [15, 99]
print(delete_a_number(list_delete))


'''
Задание 5
Напишите функцию, которая получает два списка в качестве параметра 
и возвращает список, содержащий элементы обоих списков.
'''
def list_list(list_of_numbers_2):

    new_list = list_of_numbers_1[:]
    for num in list_of_numbers_2:
        new_list.append(num)

    return new_list

list_of_numbers_1 = [10, 4, 9, 5, 7, 1, 15, 89,99]
list_of_numbers_2 = [11, 7, 19, 4, 8, 11, 15, 57, 2]
print(list_list(list_of_numbers_2))






'''
Задание 6 
Напишите функцию, высчитывающую степень каждого элемента списка целых. 
Значение для степени передаётся в качестве параметра, список тоже передаётся в качестве параметра.
Функция возвращает новый список, содержащий полученные результаты.
'''

def count_power_of(list_of_numbers_1):
    new_list = []

    n = ''
    for i in list_of_numbers_1:
        n = i ** num
        new_list.append(n)
    return new_list

list_of_numbers_1 = [10, 4, 9, 5, 7, 1, 15, 89,99]
num = 2
print(count_power_of(list_of_numbers_1))