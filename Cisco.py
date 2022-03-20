''' 3.1.1.10 LAB: Comparison operators and conditional execution'''
# while True:
#     string = str(input('Please enter a string:'))
#     if string == 'Spathiphyllum':
#         print('Yes - Spathiphyllum is the best plant ever!')
#         break
#     elif string == 'spathiphyllum':
#         print('No, I want a big Spathiphyllum!')
#     else:
#         print('Spathiphyllum! Not', string, '!')


# 2 task
# while True:
#     income = float(input("Enter the annual income: "))
#     tax = float(0)
#     if income <= 85528:
#         tax = (income * 18 / 100) - 556.02
#     else:
#         tax = 14839.02 + ((income - 85528) * 32 / 100)
#     if tax <= 0:
#         print("The tax is: 0.0 thalers")
#
#     else:
#         tax = round(tax, 0)
#         print("The tax is:", tax, "thalers")
#



#3 task

# year = int(input("Enter a year: "))
# if year <= 1580:
#     print('Not within the Gregorian calendar period')
# if year % 4 != 0 or year % 400 != 0:
#     print('It\'s common year')
# elif year % 100 != 0:
#     print('It\'s leap year')
# else:
#     print('It\'s leap year')

#4 task
# secret_number = 777
# print(
#     """
#     +================================+
#     | Welcome to my game, muggle!    |
#     | Enter an integer number        |
#     | and guess what number I've     |
#     | picked for you.                |
#     | So, what is the secret number? |
#     +================================+
#     """)
# number = int(input('Please eneter a number:'))
# while True:
#     if number != secret_number:
#         print('Ha ha! You\'re stuck in my loop!')
#         number = int(input('Please eneter a number:'))
#     elif number == secret_number:
#         print('Well done, muggle! You are free now.')
#         break

#5 task

# power = 1
# for expo in range(16):
#     print("2 to the power of", expo, "is", power)
#     power *= 2
#
# import time
# sleep = 'Mississipi'
# for count in range(1,7):
#     if count != 6:
#         print(count,sleep )
#     else:
#         print('Ready or not, here I come!')

# 6 task

# word = str(input('please eneter a word:'))
# while word != 'chupacabra':
#     word = str(input('please eneter a word:'))
#     if word == 'chupacabra':
#         break
#     else:
#         continue

# 7 task

# user_word = input('Please, enter a word: ')
# user_word = user_word.upper()
# for letter in user_word:
#     if letter == 'A':
#         continue
#     elif letter == 'E':
#         continue
#     elif letter == 'I':
#         continue
#     elif letter == 'U':
#         continue
#     elif letter == 'O':
#         continue
#     else:
#         print(letter)

#8 task

# user_word = input('Please, enter a word: ')
# user_word = user_word.upper()
# for letter in user_word:
#     if letter == 'A':
#         continue
#     elif letter == 'E':
#         continue
#     elif letter == 'I':
#         continue
#     elif letter == 'U':
#         continue
#     elif letter == 'O':
#         continue
#     else:
#         print(letter, end='')

# 9
#
# blocks = int(input("Enter the number of blocks: "))
# y = blocks
# i = 0
# height = 0
# while y != 0 and y > 0:
#         i = i + 1
#         y = y - i
#         if y <= -1:
#             break
#         height = height + 1
#         print(y)
# print("The height of the pyramid:", height)


# 10
# c0 = int(input('Plese enter any non-negative and non-zero integer: '))
# step = 0
#
# while c0 != 1:
#     if c0 % 2 == 0:
#         c0 = c0 / 2
#         step = step + 1
#         print(c0)
#     elif c0 % 2 != 0:
#         c0 = 3 * c0 + 1
#         step = step + 1
#         print(c0)
# print('steps are: ', step)


#11 task


# import tkinter as tk
# window = tk.Tk()
# window.geometry(f"500x500")
# window.title("Tic Tac Toe")
# window.config(bg='#2DFF00')
# cell_1 = tk.Label(window, text= '1',
#                   bg='red',
#                   fg='white',
#                   font=('Arial',50,'bold'),
#                   padx=30,
#                   pady=40)
#
# cell_2 = tk.Label(window, text= '2',
#                   bg='red',
#                   fg='white',
#                   font=('Arial',50,'bold'),
#                   padx=30,
#                   pady=40)
#
# cell_3 = tk.Label(window, text= '3',
#                   bg='red',
#                   fg='white',
#                   font=('Arial',50,'bold'),
#                   padx=30,
#                   pady=40)
# cell_1.pack()
# cell_2.pack()
# cell_3.pack()
# window.mainloop()

#

# x = 4
# y = 1
#
# a = x & y
# b = x | y
# c = ~x  # tricky!
# d = x ^ 5
# e = x >> 2
# f = x << 2
#
# print(a, b, c, d, e, f)


# 11 task

# hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
# hat_list[2] = int(input('pleaee enter a number: '))
#
# del hat_list[-1]
#
# print(len(hat_list))
#
#
# print(hat_list)

#12 task
# my_list = []  # Creating an empty list.
#
# for i in range(5):
#     my_list.append(i + 1)
#
# print(my_list)


# my_list = [10, 1, 8, 3, 5]
# total = 0
#
# for i in my_list:
#     total += i
#
# print(total)
#################### first way
# variable_1 = 1
# variable_2 = 2
#
# auxiliary = variable_1
# variable_1 = variable_2
# variable_2 = auxiliary
##################### second way
# variable_1 = 1
# variable_2 = 2
#
# variable_1, variable_2 = variable_2, variable_1

########################## список наоборот
# для переворота списка
# my_list = [10, 1, 8, 3, 5]
# length = len(my_list)
#
# for i in range(length // 2):
#     my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
#
# print(my_list)

########13
#
# my_list = [8, 10, 6, 2, 4]  # list to sort
# swapped = True  # It's a little fake, we need it to enter the while loop.
#
# while swapped:
#     swapped = False  # no swaps so far
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True  # a swap occurred!
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
#
# print(my_list)



# my_list = []
# swapped = True
# num = int(input("How many elements do you want to sort: "))
#
# for i in range(num):
#     val = float(input("Enter a list element: "))
#     my_list.append(val)
#
# while swapped:
#     swapped = False
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
#
# print("\nSorted:")
# print(my_list)

# beatles = []
# print("Step 1:", beatles)
#
# beatles.append('John Lennon')
# beatles.append('Paul McCartney')
# beatles.append('George Harrison')
# print("Step 2:", beatles)
#
#
# for i in ('Stu Sutcliffe', 'Pete Best'):
#     beatles.append(i)
# print("Step 3:", beatles)
#
# del beatles[3:]
# print("Step 4:", beatles)
#
# beatles.insert(0,'Ringo Starr')
# print("Step 5:", beatles)
#
# # testing list legth
# print("The Fab", len(beatles))


#######

# my_list = [0, 3, 12, 8, 2]
#
# print(5 in my_list)
# print(5 not in my_list)
# print(12 in my_list)

# drawn = [5, 11, 9, 42, 3, 49]
# bets = [3, 7, 11, 42, 34, 49]
# hits = 0
#
# for number in bets:
#     if number in drawn:
#         hits += 1
#
# print(hits)
###############
# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# new_list = my_list[:]
# new_list.sort()
# new2_list = []
#
# for i in range(len(new_list)):
#     if new_list[i] == new_list[-1]:
#         if new_list[i] == new_list[i - 1]:
#             break
#         else:
#             new2_list.append(new_list[i])
#     elif new_list[i] == new_list[i + 1]:
#         continue
#     else:
#         new2_list.append(new_list[i])
# print(new2_list)


################
# list1 = [1,2,4,4,1,4,2,6,2,9]
# list2 = []
# for i in range(len(list1)):
#     if list1[i] not in list2:
#         list2.append(list1[i])
# print(list2)

################## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# list_1 = ["A", "B", "C"]
# list_2 = list_1
# list_3 = list_2
#
# del list_1[0]
# del list_2
#
# print(list_3)
################## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# list_1 = ["A", "B", "C"]
# list_2 = list_1
# list_3 = list_2
#
# del list_1[0]
# del list_2[:]
#
# print(list_1)
# print(list_3)

#
# cubed = [num ** 3 for num in range(5)]
# print(cubed)  # outputs: [0, 1, 8, 27, 64]

# my = [0 for i in range(1,3)]
# print(my)

# var = 1
# while var < 10:
#     print('#')
#     var = var << 1

# num = [1,2,3]
# u = num
# del u [1:2]
# print(u)
# print((num))


# t = [[3-i for i in range(3)] for j in range(3)]
# s = 0
# for i in range(3):
#     s += t[i][i]
# print(s)
#
# t =[1,2,3]
# for i in range(len(t)):
#     t.insert(1,t[i])
# print(t)

# t = [[0,1,2,3] for i in range(2)]
# print(t[2][0])

# x = 1
# x = x == x
# print(x)

# blocks = int(input("Enter the number of blocks: "))
#
#

#
# Write your code here.
#



height = 0



# while blocks >= height+1:
#     height = height + 1
#     blocks = blocks - height
#
#
#
# print("The height of the pyramid:", height)

# for i in range(1):
#     print(1)
# else:
#     print(1)
#
#
# t =[1,2,3,4]
# print(t[-3:-2])

# t =[1,2,3]
# a = []
# for v in t:
#     a.insert(0,v)
# print(a)


# i = 0
# while i <= 5:
#     i+=1
#     if i % 2 == 0:
#         break
#     print("#")
#
# t = [0, 2, 3]
# t.insert(0,1)
# del t[1]
# print(t)

#
# t =[1,2,3]
# a = t
# del a[1:2]
# print(t)
# print(a)
#
# print(a)
#
# var = 0
# while var < 6:
#     var +=1
#     if var % 2 == 0:
#         continue
#     print('@')


# my_list = [i for i in range(-1,2)]
# print((my_list))




#####
# def hi():
#     print("hi")
#
# hi()


#######
# def address(street, city, postal_code):
#     print("Your address is:", street, "St.,", city, postal_code)
#
# s = input("Street: ")
# p_c = input("Postal Code: ")
# c = input("City: ")
#
# address(s, c, p_c)


########

# # Ex. 1
# def subtra(a, b):
#     print(a - b)
#
# subtra(5, 2)    # outputs: 3
# subtra(2, 5)    # outputs: -3
#
#
# # Ex. 2
# def subtra(a, b):
#     print(a - b)
#
# subtra(a=5, b=2)    # outputs: 3
# subtra(b=2, a=5)    # outputs: 3
#
# # Ex. 3
# def subtra(a, b):
#     print(a - b)
#
# subtra(5, b=2)    # outputs: 3
# subtra(5, 2)    # outputs: 3


#####

# def subtra(a, b):
#     print(a - b)
#
# subtra(5, b=2)    # outputs: 3
# subtra(a = 9, b = 2)    # Syntax Error


####

# def add_numbers(a, b=2, c=9):
#     print(a + b + c)
#
# add_numbers(2,4,7)


####
# def boring_function():
#     print("'Boredom Mode' ON.")
#     return 123
#
# print("This lesson is interesting!")
# boring_function()
# print("This lesson is boring...")
# print(boring_function())

#######
# value = None
# if value is None:
#     print("Sorry, you don't carry any value")

#######

# def strange_function(n):
#     if(n % 2 == 0):
#         return True
#
# print(strange_function(2))
# print(strange_function(1))
#
# print(strange_function(199))


######

# def list_sum(lst):
#     s = 0
#
#     for elem in lst:
#         s += elem
#
#     return s
#
# print(list_sum([5, 4, 3]))


####

# def strange_list_fun(n):
#     strange_list = []
#
#     for i in range(0, n):
#         strange_list.insert(0, i)
#
#     return strange_list
#
#
# print(strange_list_fun(5))



#####
## def is_year_leap(year):
##     test_data = [1900, 2000, 2016, 1987]
###     test_results = [False, True, True, False]
##      for i in range(len(test_data)):
# 	    year = test_data[i]. #1900
# 	    print(year,"->",end="")
#     result = is_year_leap(year)
#     for j in range(len(test_result)):
# 	if result == test_results[j]:
#         print("OK")
# 	else:
# 	    print("Failed")
#     return(yr)
#
# is_year_leap(test_data)


# test_data = [1900, 2000, 2016, 1987]
# test_results = [False, True, True, False]
# for i in range(len(test_data)):
# 	year = test_data[i]   ###1900
#     test_data[i] = test_results[i]
# 	print(year,"->",end="")
#     # result = 'is_year_leap',year
#     if test_data[i] == test_results[i]:
#         print("OK")
#     else:
# 		print("Failed")


#####123#### function
# def address(street, city, postal_code):
#     print("Your address is:", street, "St.,", city, postal_code)
#
# s = input("Street: ")
# p_c = input("Postal Code: ")
# c = input("City: ")
#
# address(s, c, p_c)

####

# def happy_new_year(wishes=True):
#     print("Three...")
#     print("Two...")
#     print("One...")
#     if not wishes:
#         return
#
#     print("Happy New Year!")
# happy_new_year()

####

# value = None
# if value is None:
#     print("Sorry, you don't carry any value")


#####

# def strange_function(n):
#     if(n % 2 == 0):
#         return True
#
# print(strange_function(4))

####

# def list_sum(lst):
#     s = 0
#
#     for elem in lst:
#         s += elem
#
#     return s
#

# print(list_sum([1, 4, 8]))

###

# def strange_list_fun(n):
#     strange_list = []
#
#     for i in range(0, n):
#         strange_list.insert(0, i)
#
#     return strange_list
#
#
# print(strange_list_fun(5))


#####leap year #####

# def is_year_leap(year):
#     if year % 2 == 0:
#         return True
#
#
#
# test_data = [1900, 2000, 2016, 1987]
# test_results = [False, True, True, False]
# for i in range(len(test_data)):
# 	yr = test_data[i]
# 	print(yr,"->",end="")
# 	result = is_year_leap(yr)
# 	if result == test_results[i]:
# 		print("OK")
# 	else:
# 		print("Failed")


######
# def round_func(a, b):
#     return round(a, b)
#
# lis = [1.98, 2.09, 8.34]
# for i in range(len(lis)):
#     u = round_func(lis[i], 1)
#     u = u*2
#     print(u)
#
# number1 = 2.232342
# u2 = round_func(number1, 2)
# print(u2)




########
# def is_year_leap(year):
#     if year <= 1580:
#         print('Not within the Gregorian calendar period')
#     if year % 4 != 0 or year % 400 != 0:
#         print('It\'s common year')
#         return False
#     elif year % 100 != 0:
#         print('It\'s leap year')
#         return True
#     else:
#         print('It\'s leap year')
#         return True
#
#
# def days_in_month(year, month):
#     res = is_year_leap(year)
#     if res == True:
#         if month == 2:
#             d = 29
#         if month == 1:
#             d = 31
#         if month == 11:
#             d = 30
#     else:
#         if month == 2:
#             d = 28
#         if month == 1:
#             d = 31
#         if month == 11:
#             d = 30
#     return d
#
#
# test_years = [1900, 2000, 2016, 1987]
# test_months = [2, 2, 1, 11]
# test_results = [28, 29, 31, 31]
# for i in range(len(test_years)):
#     yr = test_years[i]
#     mo = test_months[i]
#     print(yr, mo, "->", end="")
#     result = days_in_month(yr, mo)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Failed")
#
#
# import calendar
# print(calendar.monthrange(2022, 4))
#
###### проверка дней и месяцев высокосного года и не высокосного
import calendar
# def days_in_month(year, month):
#     c = calendar.monthrange(year, month)[1]
#     # d = c[1]
#     print(c)
#     return c
#
#
# test_years = [1900, 2000, 2016, 1987]
# test_months = [2, 2, 1, 11]
# test_results = [28, 29, 31, 31]
# for i in range(len(test_years)):
# 	yr = test_years[i]
# 	mo = test_months[i]
# 	print(yr, mo, "->", end="")
# 	result = days_in_month(yr, mo)
# 	if result == test_results[i]:
# 		print("OK")
# 	else:
# 		print("Failed")

################################### YEAR ##############

# def is_year_leap(year):
#     if year <= 1580:
#         print('Not within the Gregorian calendar period')
#     if year % 4 != 0 or year % 400 != 0:
#         print('It\'s common year')
#         return False
#     elif year % 100 != 0:
#         print('It\'s leap year')
#         return True
#     else:
#         print('It\'s leap year')
#         return True
#
# #
# def days_in_month(year, month):
#     res = is_year_leap(year)
#     if res == True:
#         if month == 2:
#             d = 29
#         if month == 1:
#             d = 31
#         if month == 11:
#             d = 30
#     else:
#         if month == 2:
#             d = 28
#         if month == 1:
#             d = 31
#         if month == 11:
#             d = 30
#     return d



# def day_of_year(year, month, day):
#     rez = days_in_month(year,month)
#     if rez >= day:
#         return True
#     else:
#         return None
#
#
# print(day_of_year(2000, 11, 30))
# print(day_of_year(2001, 2, 29))

######### простые числа ############
# def is_prime(num):
#     for j in range(2, num + 1):
#         if num // j == num / j:
#             if num / j != 1:
#                 return False
#         if num / j == 1:
#             return True
#
#
# for i in range(1, 20):
#     if is_prime(i + 1):
#         print(i + 1, end=" ")


######### перевод галонов в литры  ##################
'''
1 American mile = 1.609344 kmetres;
1 American gallon = 3.785411784 litres.

'''
#
# def liters_100km_to_miles_gallon(liters):
#     mile = 1 * 100 / 1.609344
#     # print(mile)
#     gallon = liters * 1 / 3.785411784
#     # print(gallon)
#     return mile / gallon
#
#
#
# def miles_gallon_to_liters_100km(miles):
#     km = miles * 1.609344 / 1
#     litters = 1 * 3.785411784 / 1
#     return litters * 100 / km
#
#
#
# print(liters_100km_to_miles_gallon(3.9))
# print(liters_100km_to_miles_gallon(7.5))
# print(liters_100km_to_miles_gallon(10.))
# print(miles_gallon_to_liters_100km(60.3))
# print(miles_gallon_to_liters_100km(31.4))
# print(miles_gallon_to_liters_100km(23.5))


#########
#
# def even_num_lst(ran):
#     lst = []
#     for num in range(ran):
#         if num % 2 == 0:
#             lst.append(num)
#     return lst
#
# print(even_num_lst(13))


######

# def list_updater(lst):
#     upd_list = []
#     for elem in lst:
#         elem **= 2
#         upd_list.append(elem)
#     return upd_list
#
# foo = [1, 2, 3, 4, 5]
# print(list_updater(foo))


##########


