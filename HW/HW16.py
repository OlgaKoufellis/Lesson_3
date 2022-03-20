'''
Задание 1
Напишите функцию, вычисляющую произведение элементов списка целых.
Список передаётся в качестве параметра. Полученный результат возвращается из функции.
'''

# def multiply(lis):
#     res = 1
#     for i in range(len(lis)):
#         res = res * lis[i]
#     return res
#
# lis = [1, 6, 9 ,2 ]
# print(multiply(lis))



'''
Задание 2 
Напишите функцию для нахождения минимума в списке целых. 
Список передаётся в качестве параметра. Полученный результат возвращается из функции.
'''
# def multiply(lis):
#     minim = lis[0]
#     for i in range(len(lis)):
#         if minim > lis[i]:
#            minim = lis[i]
#     return minim
#
# lis = [9, 6, 1 ,2 ]
# print(multiply(lis))



'''
Задание 3 
Напишите функцию, определяющую количество простых чисел в списке целых. 
Список передаётся в качестве параметра. Полученный результат возвращается из функции.

'''

# def is_prime(num):
#     for j in range(2, num + 1):
#         if num // j == num / j:
#             if num / j != 1:
#                 return False
#         if num / j == 1:
#             return True
#
# count = 0
# num = [1, 5, 8, 3, 7, 13]
# for i in range(len(num)):
#     if is_prime(num[i]):
#         count += 1
#         print(num[i], end=" ")
# print()
# print(count)


'''
Задание 4 
Напишите функцию, удаляющую из списка целых некоторое заданное число. 
Из функции нужно вернуть количество удаленных элементов.
'''
### I ####
# def multiply(lis, delete):
#     count = 0
#     new_lis = []
#     for i in range(len(lis)):
#         if lis[i] != delete:
#             new_lis.append(lis[i])
#         else:
#             count += 1
#     print(new_lis)
#     return count
#
# lis = [1, 6, 9 ,2 , 6 ]
# delete = 6
# print(multiply(lis, delete))

#### II ####

# def multiply(lis, delete):
#     count = 0
#     while True :
#         try:
#             lis.remove(delete)
#             count += 1
#         except:
#             print(lis)
#             return count
#
# lis = [1, 6, 9 ,2 , 6 , 6]
# delete = 6
# print(multiply(lis, delete))


'''
Задание 5 
Напишите функцию, которая получает два списка в качестве параметра и возвращает список, 
содержащий элементы обоих списков.
'''

#
# def list_list(lis, lis2):
#     lis3 = []
#     for i in range(len(lis)):
#         for j in range(len(lis2)):
#             if lis[i] == lis2[j]:
#                 if lis[i] not in lis3:
#                     lis3.append(lis[i])
#     # lis3 = set(lis3)
#
#     return lis3
#
# lis = [2,4,6,9,2, 4]
# lis2 = [12,4,26,9,12]
# print(list_list(lis, lis2))

'''
Задание 6 
Напишите функцию, высчитывающую степень каждого элемента списка целых. 
Значение для степени передаётся в качестве параметра, список тоже передаётся в качестве параметра. 
Функция возвращает новый список, содержащий полученные результаты.
'''

def list_updater(foo, power):
    upd_list = []
    for elem in foo:
        elem **= power
        upd_list.append(elem)
    return upd_list

foo = [1, 2, 3, 4, 5]
print(list_updater(foo, 2))
