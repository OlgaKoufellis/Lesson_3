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
# c0 = int(input('Please enter any non-negative and non-zero integer: '))
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
# hat_list[2] = int(input('please enter a number: '))
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


# def person_func(self,short_info):
    #     if short_info :
    #         return str(self.full_name + ', ' + self.country + ', ' + self.city)
    #         # return self.full_name, self.country, self.city
    #     else:
    #         return self.full_name, self.date_of_birth, self.country, self.city, self.address, self.phone_num



############

# def my_function():
#     global var
#     var = 2
#     print("Do I know that variable?", var)
#
#
# var = 1
# my_function()
# print(var)


#####

# def my_function(n):
#     print("I got", n)
#     n += 1
#     print("I have", n)
#
#
# var = 1
# my_function(var)
# print(var)


###########################

# def my_function(my_list_1):
#     print("Print #1:", my_list_1)
#     print("Print #2:", my_list_2)
#     my_list_1 = [0, 1]
#     print("Print #3:", my_list_1)
#     print("Print #4:", my_list_2)
#
#
# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Print #5:", my_list_2)

############################

# def is_a_triangle(a, b, c):
#     if a + b <= c:
#         return False
#     if b + c <= a:
#         return False
#     if c + a <= b:
#         return False
#     return True
#
# print(is_a_triangle(1, 1, 1))   # True
# print(is_a_triangle(1, 1, 3))    #False
#
#
#
#
#
# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b
#
# print(is_a_triangle(1, 1, 1))  # True
# print(is_a_triangle(1, 1, 3))  # False

#####################################
#
# def factorial_function(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
#
#     product = 1
#     for i in range(2, n + 1):
#         product *= i
#     return product
#
#
# for n in range(1, 6):  # testing
#     print(n, factorial_function(n))



#########################
#
# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
#
#     elem_1 = elem_2 = 1
#     the_sum = 0
#     for i in range(3, n + 1):
#         the_sum = elem_1 + elem_2
#         elem_1, elem_2 = elem_2, the_sum
#     return the_sum
#
#
# for n in range(1, 10):  # testing
#     print(n, "->", fib(n))



#######################
# def factorial_function(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
#     return n * factorial_function(n - 1)
#
# for n in range(1, 10):  # testing
#     print(n, "->", factorial_function(n))



########### TUPLE ########### КОРТЕЖ ##########
# a = 2., .9
# my_tuple = (1, 10, 100, 1000)
# my_tuple1 = (1,)
# print(my_tuple +  my_tuple1)
# # my_tuple = my_tuple1
# print(my_tuple)

###############Словари ############# DICTIONARY ##################
#
# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
# #dictionary = dict(cat = "chat", dog = "chien", horse = "cheval")
# phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
# empty_dictionary = {}
#
# print(dictionary)
# print(phone_numbers)
# print(empty_dictionary)
#
#
# ####
# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
# words = ['cat', 'lion', 'horse']
#
# for word in words:
#     if word in dictionary:
#         print(word, "->", dictionary[word])
#     else:
#         print(word, "is not in dictionary")
#
#
#
# ####### 1 #### метод перебора справочников
#
# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
#
# for key in dictionary.keys():
#     print(key, "->", dictionary[key])
#
# ####### 2 #### метод перебора справочников
#
# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
#
# for english, french in dictionary.items():
#     print(english, "->", french)
#
# ####### 3 #### метод перебора справочников
#
# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
#
# for french in dictionary.values():
#     print(french)

######### modifying and adding values ##############
# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
#
# dictionary['cat'] = 'minou'
# # print(dictionary)
#
#
# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
#
# dictionary['swan'] = 'cygne'
# dictionary.update({"duck": "canard"})
# print(dictionary)

########### Removing a key ############

# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
#
# del dictionary['dog']
# print(dictionary)

############# TUPLE + DICTIONARY ###############

# school_class = {}
#
# while True:
#     name = input("Enter the student's name: ")
#     if name == '':
#         break
#
#     score = int(input("Enter the student's score (0-10): "))
#     if score not in range(0, 11):
#         break
#
#     if name in school_class:
#         school_class[name] += (score,)
#     else:
#         school_class[name] = (score,)
#
# for name in sorted(school_class.keys()):
#     adding = 0
#     counter = 0
#     for score in school_class[name]:
#         adding += score
#         counter += 1
#     print(name, ":", adding / counter)


##############   to convert an iterable to a list #################

# my_tuple = (1, 2, "string") #TUPLE
# print(my_tuple)

# my_list = [2, 4, 6]
# print(my_list)    # outputs: [2, 4, 6]
# print(type(my_list))    # outputs: <class 'list'>
# tup = tuple(my_list)
# print(tup)    # outputs: (2, 4, 6)
# print(type(tup))    # outputs: <class 'tuple'>


# tup = 1, 2, 3,
# my_list = list(tup)
# print(type(my_list))    # outputs: <class 'list'>
# print(my_list)


################ popitem ############ remove the last element by using the popitem() method ###########

# pol_eng_dictionary = {"kwiat": "flower"}
#
# pol_eng_dictionary.update({"gleba": "soil"})
# print(pol_eng_dictionary)    # outputs: {'kwiat': 'flower', 'gleba': 'soil'}
#
# pol_eng_dictionary.popitem()
# print(pol_eng_dictionary)    # outputs: {'kwiat': 'flower'}

############### in

# pol_eng_dictionary = {
#     "zamek": "castle",
#     "woda": "water",
#     "gleba": "soil"
#     }
#
# if "zamek" in pol_eng_dictionary:
#     print("Yes")
# else:
#     print("No")

############### clear ##############
#
# pol_eng_dictionary = {
#     "zamek": "castle",
#     "woda": "water",
#     "gleba": "soil"
#     }
#
# print(len(pol_eng_dictionary))    # outputs: 3
# del pol_eng_dictionary["zamek"]    # remove an item
# print(len(pol_eng_dictionary))    # outputs: 2
#
# pol_eng_dictionary.clear()   # removes all the items
# print(len(pol_eng_dictionary))    # outputs: 0
#
# del pol_eng_dictionary    # removes the dictionary

################# copy

# pol_eng_dictionary = {
#     "zamek": "castle",
#     "woda": "water",
#     "gleba": "soil"
#     }
#
# # copy_dictionary = pol_eng_dictionary
# # print(copy_dictionary)
# copy_dictionary = pol_eng_dictionary.copy()
# print(copy_dictionary)
#

############


#
# tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
# duplicates = tup.count(2)# Write your code here.
#
# print(duplicates)    # outputs: 4
#
#
# d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
# d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
# d3 = {}
#
# # d3 = d1
# # d3.update(d2)
#
# for item in (d1, d2):
#     d3.update(item)
# print(d3)
#
#
#
#
# my_list = ["car", "Ford", "flower", "Tulip"]
# t = tuple(my_list) # Write your code here.
# print(t)
#
#
#
#
# colors = (("green", "#008000"), ("blue", "#0000FF"))
# colors_dictionary = dict(colors)# Write your code here.
# print(colors_dictionary)
#
#
# #####################
# '''try:
# 	# It's a place where
# 	# you can do something
#     # without asking for permission.
# except:
# 	# It's a spot dedicated to
#     # solemnly begging for forgiveness.
# '''
#
# try:
#     value = int(input('Enter a natural number: '))
#     print('The reciprocal of', value, 'is', 1/value)
# except:
#     print('I do not know what to do.')
#
#
#
# try:
#     value = int(input('Enter a natural number: '))
#     print('The reciprocal of', value, 'is', 1/value)
# except ValueError:
#     print('I do not know what to do.')
# except ZeroDivisionError:
#     print('Division by zero is not allowed in our Universe.')
#
#
#
# try:
#     value = int(input('Enter a natural number: '))
#     print('The reciprocal of', value, 'is', 1/value)
# except ValueError:
#     print('I do not know what to do.')
# except ZeroDivisionError:
#     print('Division by zero is not allowed in our Universe.')
# except:
#     print('Something strange has happened here... Sorry!')
#
#
#
#
# try:
#     temperature = float(input('Enter current temperature:'))
#     if temperature > 0:
#         print("Above zero")
#     elif temperature < 0:
#         print("Below zero")
#     else:
#         print("Zero")
# except ValueError:
#     print('I do not know what to do.')

# tup = (1,) +(1,)
# tup = tup + tup
# print(len(tup))
#
#
#
## def f(x, y):
##     if x == y:
##         return x
# #    return f(x, y -1)
# #
# #print(f(0 ,3))
# #
# #
# #z = 0
# #y = 10
# #x = y < z and z > y or y < z and z > y
# #print(x)
# #
# #print = (1 ,2, 4 , 8)
# #tup = tup[-2:-1]
# #tup = tup[-1]
# #print(tup)
#
# #def fun(a,b):
#  #   return b ** a
# #
# #print(fun(b = 2, 2))

########## import ###########

# import math
# def sin(x):
#     if 2 * x == pi:
#         return 0.99999999
#     else:
#         return None
# pi = 3.14
# print(sin(pi/2))
# print(math.sin(math.pi/2))
#
# #######
#
# from math import pi as PI, sin as sine
#
# print(sine(PI/2))


#########
# from my_module import *
#
# result = my_function(my_data)



# import math
# dir(math)


# #
# from random import randint
# for i in range(2):
#     print(randint(1,2), end=' ')


#
# from random import randrange, randint
# print(randrange(1), end=' ')
# print(randrange(0, 1), end=' ')
# print(randrange(0, 1, 1), end=' ')
# print(randint(0, 1))



# from random import choice, sample
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(choice(my_list))
# print(sample(my_list, 5))
# print(sample(my_list, 10))



'''It's a function named in a very suggestive way - choice:

choice(sequence)
sample(sequence, elements_to_choose)
The first variant chooses a "random" element from the input sequence and returns it.

The second one builds a list (a sample) consisting of the elements_to_choose element "drawn" from the input sequence.'''




'''
Selected functions from the platform module: continued
The machine function

Sometimes, you may just want to know the generic name of the processor which runs your OS together with Python and your code - a function named machine() will tell you that. As previously, the function returns a string.

Again, we ran the sample program on three different platforms:

Intel x86 + Windows ® Vista (32 bit):

x86
output

Intel x86 + Gentoo Linux (64 bit):

x86_64
output

Raspberry PI2 + Raspbian Linux (32 bit):

armv7l
output


'''
# from platform import machine
# print(machine())


''''
The processor() function returns a string filled with the real processor name (if possible).
Once again, we ran the sample program on three different platforms:

Intel x86 + Windows ® Vista (32 bit):
x86
output

Intel x86 + Gentoo Linux (64 bit):
Intel(R) Core(TM) i3-2330M CPU @ 2.20GHz
output

Raspberry PI2 + Raspbian Linux (32 bit):
armv7l
output

Test this on your local machine.
'''

# from platform import processor
# print(processor())




'''
The system function
A function named system() returns the generic OS name as a string.
Our example platforms presented themselves like this:

Intel x86 + Windows ® Vista (32 bit):
Windows
output

Intel x86 + Gentoo Linux (64 bit):
Linux
output

Raspberry PI2 + Raspbian Linux (32 bit):
Linux
output


'''

# from platform import system
# print(system())



'''
The version function
The OS version is provided as a string by the version() function.
Run the code and check its output. This is what we got:

Intel x86 + Windows ® Vista (32 bit):
6.0.6002
output

Intel x86 + Gentoo Linux (64 bit):
#1 SMP PREEMPT Fri Jul 21 22:44:37 CEST 2017
output

Raspberry PI2 + Raspbian Linux (32 bit):
#1 SMP Debian 4.4.6-1+rpi14 (2016-05-05)

'''

# from platform import version
# print(version())


'''
The python_implementation and the python_version_tuple functions
If you need to know what version of Python is running your code, you can check it using a number of dedicated functions
 - here are two of them:
python_implementation() → returns a string denoting the Python implementation 
(expect CPython here, unless you decide to use any non-canonical Python branch)
python_version_tuple() → returns a three-element tuple filled with:
the major part of Python's version;
the minor part;
the patch level number.
'''

# from platform import python_implementation, python_version_tuple
# print(python_implementation())
# for atr in python_version_tuple():
#     print(atr)



#
# import platform
# print(len(platform.python_version_tuple()))

# import math
#
# result = math.e !=math.pow(2,4)
# print(int(result))






'''
Operations on strings: ord()
If you want to know a specific character's ASCII/UNICODE code point value, 
you can use a function named ord() (as in ordinal).
The function needs a one-character string as its argument - 
breaching this requirement causes a TypeError exception, and returns a number representing the argument's code point.
'''
# Demonstrating the ord() function.
# char_1 = 'a'
# char_2 = ' '  # space
# print(ord(char_1))
# print(ord(char_2))
#

# Demonstrating the chr() function.

# print(chr(97))
# print(chr(945))
#
# for ch in "abc":
#     print(chr(ord(ch) + 1), end='')

# Indexing strings.

# the_string = 'silly walks'
# for ix in range(len(the_string)):
#     print(the_string[ix], end=' ')
# print()


# Iterating through a string.

# the_string = 'islly walks'
# for character in the_string:
#     print(character, end=' ')
# print()
#
#
# # Slices
#
# alpha = "abdefg"
# print(alpha[1:3])   #bd
# print(alpha[3:])    #efg
# print(alpha[:3])    #abd
# print(alpha[3:-2])  #e
# print(alpha[-3:4])  #e
# print(alpha[::2])   #adf
# print(alpha[1::2])  #beg
#
#
#
# # The in and not in operators
#
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# print("f" in alphabet)
# print("F" in alphabet)
# print("1" in alphabet)
# print("ghi" in alphabet)
# print("Xyz" in alphabet)
# print("f" not in alphabet)
# print("F" not in alphabet)
# print("1" not in alphabet)
# print("ghi" not in alphabet)
# print("Xyz" not in alphabet)
#
#
#
# #Operations on strings: continued
#
# alphabet = "bcdefghijklmnopqrstuvwxy"
# alphabet = "a" + alphabet
# alphabet = alphabet + "z"
# print(alphabet)
#
#
#
# # Demonstrating min() - Example 1:
# print(min("aAbByYzZ"))
#
#
# # Demonstrating min() - Examples 2 & 3:
# t = 'The Knights Who Say "Ni!"'
# print('[' + min(t) + ']')
# t = [0, 1, 2]
# print(min(t))
#
#
# # Demonstrating max() - Example 1:
# print(max("aAbByYzZ"))
#
#
# # Demonstrating max() - Examples 2 & 3:
# t = 'The Knights Who Say "Ni!"'
# print('[' + max(t) + ']')
# t = [0, 1, 2]
# print(max(t))
#
# # Demonstrating the index() method:
# print("aAbByYzZaA".index("b"))
# print("aAbByYzZaA".index("Z"))
# print("aAbByYzZaA".index("A"))
#
#
# # Demonstrating the list() function:
# print(list("abcabc"))
#
# # Demonstrating the count() method:
# print("abcabc".count("b"))
# print('abcabc'.count("d"))
#
#
# # Demonstrating the center() method:
# print('[' + 'alpha'.center(10) + ']')
# print('[' + 'alpha'.center(6, '@') + ']')
# print('[' + 'Beta'.center(9, '!') + ']')
# print('[' + 'Beta'.center(4) + ']')
# print('[' + 'Beta'.center(6) + ']')
#
# # Demonstrating the endswith() method:
# if "epsilon".endswith("on"):
#     print("yes")
# else:
#     print("no")
#
#
#
# #The find() method
#
# # # Demonstrating the find() method:
# # print("Eta".find("ta"))
# # print("Eta".find("mma"))
#
# # t = 'theta'
# # print(t.find('heta'))
# # print(t.find('et'))
# # print(t.find('the'))
# # print(t.find('h'))
#
# #The isalnum() method
# # Demonstrating the isalnum() method:
# print('lambda30'.isalnum())
# print('lambda'.isalnum())
# print('30'.isalnum())
# print('@'.isalnum())
# print('lambda_30'.isalnum())
# print(''.isalnum())
# t = 'Six lambdas'
# print(t.isalnum())
# t = 'ΑβΓδ'
# print(t.isalnum())
# t = '20E1'
# print(t.isalnum())
#
#
# # Example 1: Demonstrating the isapha() method:
# print("Moooo".isalpha())
# print('Mu40'.isalpha())
#
# # Example 2: Demonstrating the isdigit() method:
# print('2018'.isdigit())
# print("Year2019".isdigit())
#
# # Example 1: Demonstrating the isapha() method:
# print("Moooo".isalpha())
# print('Mu40'.isalpha())
#
# # Example 2: Demonstrating the isdigit() method:
# print('2018'.isdigit())
# print("Year2019".isdigit())
#
# #The join() method
# '''The join() method is rather complicated, so let us guide you step by step thorough it:
# as its name suggests, the method performs a join - it expects one argument as a list;
# it must be assured that all the list's elements are strings - the method will raise a TypeError exception otherwise;
# all the list's elements will be joined into one string but...
# ...the string from which the method has been invoked is used as a separator, put among the strings;
# the newly created string is returned as a result.'''
#
# print(",".join(["omicron", "pi", "rho"]))
# print("@".join(["omicron", "pi", "rho"]))
# print("*".join(["omicron", "pi", "rho"]))
# print(".".join(["omicron", "pi", "rho"]))
#
# ###The lower() method
# # Demonstrating the lower() method:
# print("SiGmA=60".lower())
#
#
# # The lstrip() method - удаляет символы в начале выражения
# # Demonstrating the lstrip() method:
# print("[" + " tau ".lstrip( ) + "]")
# print("www.tau ".lstrip("w."))
# print("pythoninstitute.org".lstrip(".org"))
#
#
# #The replace() method
#
# print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
# print("This is it!".replace("is", "are"))
# print("Apple juice".replace("juice", ""))
# # Demonstrating the replace() method:
# print("This is it!".replace("is", "are", 1))
# print("This is it!".replace("is", "are", 2))
#
# # The rfind() method
# # Demonstrating the rfind() method:
# print("tau tau tau".rfind("ta"))
# print("tau tau tau".rfind("ta", 9))
# print("tau tau tau".rfind("ta", 3, 9))
# '''В первом случае, вы считаете с 9 символа до конца, 9 символ это 'a', а там дальше уже конец, так что -1
# ( что значит нет такого символа 'ta')
# Во втором случае Вы считаете с 3 символа (пробел, и далее за ним, 4 символ это уже "ta"
# (так как вы считаете с 3 до 9, последний "ta" обрезает до "t" а значит это не "ta"
# '''


#The split() method
#The split() method does what it says - it splits the string and builds a list of all detected substrings.
# Demonstrating the split() method:
# print("phi       chi\npsi".split())
# print("phi  прорпорп     chi\npsi".split())
#
#
# def mysplit(strng):
#     str_lst = strng.split()
#     return str_lst
# print(mysplit("To be or not to be, that is the question"))
# print(mysplit("To be or not to be,that is the question"))
# print(mysplit("   "))
# print(mysplit(" abc "))
# print(mysplit(""))

##The startswith() method
#The startswith() method is a mirror reflection of endswith() -
#it checks if a given string starts with the specified substring.
# Demonstrating the startswith() method:
# print("omega".startswith("meg"))
# print("omega".startswith("om"))
#
# print()

#The strip() method

# Demonstrating the strip() method:
# print("[" + "   aleph   ".strip() + "]")

#
# Demonstrating the SWAPCASE() method:
# print("I know that I know nothing.".swapcase())
# print()

# Demonstrating the TITLE() method:
# print("I know that I know nothing. Part 1.".title())
# print()

# Demonstrating the UPPER() method:
# print("I know that I know nothing. Part 2.".upper())
#

'''
1. Some of the methods offered by strings are:

capitalize() – changes all string letters to capitals;
center() – centers the string inside the field of a known length;
count() – counts the occurrences of a given character;
join() – joins all items of a tuple/list into one string;
lower() – converts all the string's letters into lower-case letters;
lstrip() – removes the white characters from the beginning of the string;
replace() – replaces a given substring with another;
rfind() – finds a substring starting from the end of the string;
rstrip() – removes the trailing white spaces from the end of the string;
split() – splits the string into a substring using a given delimiter;
strip() – removes the leading and trailing white spaces;
swapcase() – swaps the letters' cases (lower to upper and vice versa)
title() – makes the first letter in each word upper-case;
upper() – converts all the string's letter into upper-case letters.

2. String content can be determined using the following methods (all of them return Boolean values):

endswith() – does the string end with a given substring?
isalnum() – does the string consist only of letters and digits?
isalpha() – does the string consist only of letters?
islower() – does the string consists only of lower-case letters?
isspace() – does the string consists only of white spaces?
isupper() – does the string consists only of upper-case letters?
startswith() – does the string begin with a given substring?

'''


# Comparing strings

'''
==  # string == number is always False
!=   #string != number is always True;
>
>=  #string >= number always raises an exception
<
<=
'''
#
# print('alpha' == 'alpha') #True
# print('alpha' != 'Alpha') #True
# print('alpha' < 'alphabet') #True
# print('beta' > 'Beta') #True


# # Demonstrating the sorted() function:
# first_greek = ['omega', 'alpha', 'pi', 'gamma']
# first_greek_2 = sorted(first_greek)
# print(first_greek)
# print(first_greek_2)
# print()
#
# # Demonstrating the sort() method:
# second_greek = ['omega', 'alpha', 'pi', 'gamma']
# print(second_greek)
# second_greek.sort()
# print(second_greek)

'''
Strings vs. numbers
There are two additional issues that should be discussed here: 
how to convert a number (an integer or a float) into a string, and vice versa. 
It may be necessary to perform such a transformation. Moreover, it's a routine way to process input/output data.
The number-string conversion is simple, as it is always possible. It's done by a function named str().
'''

# Demonstrating the sorted() function:
# first_greek = ['omega', 'alpha', 'pi', 'gamma']
# first_greek_2 = sorted(first_greek)
# print(first_greek)
# print(first_greek_2)
# print()
#
# # Demonstrating the sort() method:
# second_greek = ['omega', 'alpha', 'pi', 'gamma']
# print(second_greek)
# second_greek.sort()
# print(second_greek)

#
# s1 = 'Where are the snows of yesteryear?'
# s2 = s1.split()
# s3 = sorted(s2)
# print(s3[1])
#
#
# s1 = '1 9 3 5 4 6'
# s2 = s1.split()
# s3 = sorted(s2)
# print(s3[1])


'''##############'''
# s1 = '12.8'
# i = int(s1)
# s2 = str(i)
# f = float(s2)
# print(s1 == s2)


'''##############'''
# # Caesar cipher.   запрограммировать слово что бы оно показывало другие буквы
# text = input("Enter your message: ")
# cipher = ''                 # prepare a string for an encrypted message (empty for now)
# for char in text:           # start the iteration through the message;
#     if not char.isalpha():  # if the current character is not alphabetic...
#         continue            # ...ignore it;
#     char = char.upper()   #convert the letter to upper-case (it's preferable to do it blindly, rather than check whether it's needed or not)
#     code = ord(char) + 1  #  get the code of the letter and increment it by one
#     if code > ord('Z'):   #if the resulting code has "left" the Latin alphabet (if it's greater than the Z code)...
#         code = ord('A')   #...change it to the A code;
#     cipher += chr(code)   # append the received character to the end of the encrypted message;
# print(cipher)  # print the cipher
# cha = ''
# for ch in cipher:
#     ch = ch.lower()
#     code1 = ord(ch) - 1
#     if code1 < ord('A'):
#         code1 = ord('Z')
#     cha += chr(code1)
# print(cha)


'''##############'''


# # Caesar cipher - decrypting a message.
# cipher = input('Enter your cryptogram: ')
# text = ''
# for char in cipher:
#     if not char.isalpha():
#         continue
#     char = char.upper()
#     code = ord(char) - 1
#     if code < ord('A'):
#         code = ord('Z')
#     text += chr(code)
# print(text)
'''##############'''

# Numbers Processor.  посчитать кол-во введеных

# line = input("Enter a line of numbers - separate them with spaces: ")
# strings = line.split()  #split the line receiving a list of substrings;
# total = ''
# try:
#     for substr in strings:      #iterate through the list...
#         total += float(substr)  #..and try to convert all its elements into float numbers; if it works, increase the sum;
#     print("The total is:", total)   #everything is good so far, so print the sum;
# except:
#     print(substr, "is not a number.")


'''##############'''

# IBAN Validator.
#
# iban = input("Enter IBAN, please: ")
# iban = iban.replace(' ','')
#
# if not iban.isalnum():
#     print("You have entered invalid characters.")
# elif len(iban) < 15:
#     print("IBAN entered is too short.")
# elif len(iban) > 31:
#     print("IBAN entered is too long.")
# else:
#     iban = (iban[4:] + iban[0:4]).upper()
#     iban2 = ''
#     for ch in iban:
#         if ch.isdigit():
#             iban2 += ch
#         else:
#             iban2 += str(10 + ord(ch) - ord('A'))
#     iban = int(iban2)
#     if iban % 97 == 1:
#         print("IBAN entered is valid.")
#     else:
#         print("IBAN entered is invalid.")

'''##############'''
# user_text = input('Please, enter your text here:') #abcxyzABCxyz 123
# split_user_text = user_text.split()
# shifted_value = input('Please, enter a shift value (an integer number from the range 1..25): ') #2
# new_user_text = ''
# # if not user_text.isalnum() and not user_text.isspace():
# #     print("You have entered invalid characters.")
# if len(user_text) <= 0:
#     print("you forgot to write a text")
# else:
#     for l in user_text:
#         if l.isalpha():
#             if l.isupper():
#                 code = ord(l) - int(shifted_value)  # 59
#                 if code < ord('A'):  # 59<65
#                     code = ord('Z') +1 - (ord('A') - code)  # 90  - 1 - 6
#             else:
#                 code = ord(l) - int(shifted_value)  # 59
#                 if code < ord('a'):
#                     code = ord('z') + 1 - (ord('a') - code)
#
#             new_user_text += chr(code)
#         if l.isspace():
#             new_user_text += ' '
#         if l.isnumeric():
#             new_user_text = new_user_text + l
# print(new_user_text)


'''##############'''

# user_text = input('Please, enter your text here:') #abcxyzABCxyz 123
# split_user_text = user_text.split()
# shifted_value = input('Please, enter a shift value (an integer number from the range 1..25): ') #2
# new_user_text = ''
# # if not user_text.isalnum() and not user_text.isspace():
# #     print("You have entered invalid characters.")
# if len(user_text) <= 0:
#     print("you forgot to write a text")
# else:
#     for l in user_text:
#         if l.isalpha():
#             if l.isupper():
#                 code = ord(l) + int(shifted_value)  # 109
#                 if code > ord('Z'):  # 109>90
#                     code = ord('A') - 1 + (code - ord('Z'))  # 65 -1  - 19
#             else:
#                 code = ord(l) + int(shifted_value)  # 59
#                 if code > ord('z'):
#                     code = ord('a') - 1 + (code - ord('z'))
#
#             new_user_text += chr(code)
#         if l.isspace():
#             new_user_text += ' '
#         if l.isnumeric():
#             new_user_text = new_user_text + l
# print(new_user_text)
#
'''##############'''
# ### Палиндром
# a = 'Eleven animals I slam in a net'
# a = a.replace(' ','')
# a = a.lower()
# b = a[::-1]
# if a == b:
#     print('Polindrom')
# else:
#     print(False)
# print(a)
# print(b)

'''##############'''
# user_text = input('Please, enter your text here:')
# user_text2 = input('Please, enter your text here:')
# user_text = sorted(user_text)
# user_text2 = sorted(user_text2)
# text = 0
# if len(user_text) == len(user_text2):
#     for i in range(len(user_text)):
#         if user_text[i] == user_text2[i]:
#             text += 1
#             if text == len(user_text):
#                 print('Anagrams')
#         else:
#             print('not anagrams')
#             break
# else:
#     print('not anagrams')


'''##############'''
# user_text = input('Please, enter your text here:')
# user_text2 = input('Please, enter your text here:')
# user_text = sorted(user_text)
# user_text2 = sorted(user_text2)
# if len(user_text) == len(user_text2):
#     for i in range(len(user_text)):
#         if user_text[i] == user_text2[i]:
#             t=0
#         else:
#             t=1
#             break
# if t == 1:
#     print('not anagrams')
# else:
#     print('Anagrams')


'''##############'''

# text = 'Dabucoonosort'
# text2 = 'donut'
# text= text.upper()
# text2 = text2.upper()
# text = list(text)
# text2 = list(text2)
# new_var = text[:]
# for i in range(len(text2)):
#     if text2[i] in text:
#         text.remove(text2[i])
#         continue
#     else:
#         print('no')
# if len(text) + len(list(text2)) == len(new_var):
#     print('yes')

'''##############'''

# numbers = {
#     "one_1"" = 1,
#     "two_2" = 2,
#     "three_3" = 3,
#     "four_4" = 4,
#     "five_5" = 5,
#     'six_6' = 6,
#     'seven_7' = 7,
#     'eight_8' = 8,
#     'nine_9' = 9
# }
'''##############'''
# one = '295743861'
# res = [int(i) for i in str(one)]
# print(res)
# two = '431865927'.split('\n')
# three = '876192543'.split('\n')
# four = '387459216'.split('\n')
# five = '612387495'.split('\n')
# six = '549216738'.split('\n')
# seven = '763524189'.split('\n')
# eight = '928671354'.split('\n')
# nine = '154938672'.split('\n')
# set_one = set(one)
# if len(one) == len(set_one):
#     print('yes')
# else:
#     print('no')


# try:
#     import math
#     x = float(input("Enter x: "))
#     y = math.sqrt(x)
#     print("The square root of", x, "equals to", y)
# except ValueError:
#         print('Something strange has happened here... Sorry!')



'''##############'''


# try:
#     print("1")
#     x = 1 / 0
#     print("2")   # оборвет
# except:
#     print("Oh dear, something went wrong...")
# print("3")

'''############'''

# print('Let\'s try to do this')



# def bad_fun(n):
#     try:
#         return 1 / n
#     except ArithmeticError:
#         print("Arithmetic Problem!")
#     return None
# bad_fun(0)
# print("THE END.")
#
#
'''##############'''
#
# def bad_fun(n):
#     return 1 / n
# try:
#     bad_fun(0)
# except ArithmeticError:
#     print("What happened? An exception was raised!")
#
# print("THE END.")

# ######except  try   raise #################
# def bad_fun(n):
#     raise ZeroDivisionError
# try:
#     bad_fun(0)
# except ArithmeticError:
#     print("What happened? An error?")
# print("THE END.")


'''##############'''

# def bad_fun(n):
#     try:
#         return n / 0
#     except:
#         print("I did it again!")
#         raise
# try:
#     bad_fun(0)
# except ArithmeticError:
#     print("I see!")
#
# print("THE END.")


#


'''##############'''
# This code cannot be terminated
# by pressing Ctrl-C.   sleeeeeep

# from time import sleep
# seconds = 0
# while True:
#     try:
#         print(seconds)
#         seconds += 1
#         sleep(1)
#     except KeyboardInterrupt:
#         print("Don't do that!")

'''##############'''
###########################
# try:
#     import math
#     import time
#     import abracadabra
# except:
#     print('One of your imports has failed.')


'''##############'''
# print(ord('c')- ord('a'))
#
# print(chr(ord('z') - 2))
#
# print(3 * 'abc' + 'qwe')
#
# x = '\''
# print(len(x))
#
# print(float("1,3"))

'''##############'''
# try:
#     print("5"/0)
# except ZeroDivisionError:
#     print('0')
# except:
#     print('sone')
#
#
# print('Mike'> "Mikey")


'''''''#############'''
# stack = []
# def push(val):
#     stack.append(val)
# def pop():
#     val = stack[-1]
#     del stack[-1]
#     return val
# push(3)
# push(2)
# push(1)
# print(pop())
# print(pop())
# print(pop())



''''############'''

# class Stack:  # Defining the Stack class.
#     def __init__(self):  # Defining the constructor function.
#         print("Hi!")
#
# stack_object = Stack()  # Instantiating the object.

'''###############'''

# class Stack:
#     def __init__(self):
#         self.__stack_list = []
#
# stack_object = Stack()
# print(len(stack_object.__stack_list))

'''###############'''

# class Stack:
#     def __init__(self):
#         self.__stack_list = []
#
#     def push(self, val):
#         self.__stack_list.append(val)
#
#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val
#
#
# stack_object = Stack()
#
# stack_object.push(3)
# stack_object.push(2)
# stack_object.push(1)
#
# print(stack_object.pop())
# print(stack_object.pop())
# print(stack_object.pop())

'''###########################################'''

# class Stack:
#     def __init__(self):
#         self.__stack_list = []
#
#
#     def push(self, val):
#         self.__stack_list.append(val)
#
#
#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val
#
#
# stack_object = Stack()
#
# stack_object.push(90)
# stack_object.push(2)
# stack_object.push(1)
# stack_object.push(11)
#
# print(stack_object.pop())
# print(stack_object.pop())
# print(stack_object.pop())

'''#############################################'''

# class Stack:
#     def __init__(self):
#         self.__stack_list = []
#
#     def push(self, val):
#         self.__stack_list.append(val)
#
#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val
#
#
# stack_object_1 = Stack()
# stack_object_2 = Stack()
#
# stack_object_1.push(3)
# stack_object_2.push(stack_object_1.pop())
#
# print(stack_object_2.pop())

'''#############################################'''

# class Stack:
#     def __init__(self):
#         self.__stack_list = []
#
#     def push(self, val):
#         self.__stack_list.append(val)
#
#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val
#
#
# little_stack = Stack()
# another_stack = Stack()
# funny_stack = Stack()
#
# little_stack.push(1)
# another_stack.push(little_stack.pop() + 1)
# funny_stack.push(another_stack.pop() - 2)
#
# print(funny_stack.pop())

'''##############################################'''

# class Stack:
#     def __init__(self):
#         self.__stackList = []
#
#     def push(self, val):
#         self.__stackList.append(val)
#
#     def pop(self):
#         val = self.__stackList[-1]
#         del self.__stackList[-1]
#         return val
#
#
# class AddingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__sum = 0
#
#     def push(self, val):
#         self.__sum += val

'''###############################################'''

# class Stack:
#     def __init__(self):
#         self.__stack_list = []
#
#     def push(self, val):
#         self.__stack_list.append(val)
#
#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val
#
#
# class AddingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__sum = 0
#
#     def get_sum(self):
#         return self.__sum
#
#     def push(self, val):
#         self.__sum += val
#         Stack.push(self, val)
#
#     def pop(self):
#         val = Stack.pop(self)
#         self.__sum -= val
#         return val
#
# stack_object = AddingStack()
#
# for i in range(5):
#     stack_object.push(i)
# print(stack_object.get_sum())
#
# for i in range(5):
#     print(stack_object.pop())

'''###############################################'''
# class A:
#     X = 0
#     def __init__(self, v = 0):
#         self.Y = v
#         A.X += v
#
# a = A()
# b = A(1)
# c = A(2)
# print(c.x)


'''#################'''
# class A:
#     def a(self):
#         print('a')
#
# class B:
#     def a(self):
#         print('b')
#
# class C:
#     def c(self):
#         self.a
#
# o = C()
# o.c()

# class A:
#     def __init__(self, v=1):
#         self.v = v
#
#     def set(self,v):
#         self.v = v
#         return v
#
# a = A()
# print((a.set(a.v + 1)))

# print(hasattr(A,'A'))

#
# class A:
#     def __str__(self):
#         return 'a'
#
# class B(A):
#     def __str__(self):
#         return 'b'
#
# class C(B):
#     pass
#
# o = C()
# print(o)
'''##################'''

# class Fib:
#     def __init__(self, nn):
#         self.__n = nn
#         self.__i = 0
#         self.__p1 = self.__p2 = 1
#
#     def __iter__(self):
#         print("Fib iter")
#         return self
#
#     def __next__(self):
#         self.__i += 1
#         if self.__i > self.__n:
#             raise StopIteration
#         if self.__i in [1, 2]:
#             return 1
#         ret = self.__p1 + self.__p2
#         self.__p1, self.__p2 = self.__p2, ret
#         return ret
#
# class Class:
#     def __init__(self, n):
#         self.__iter = Fib(n)
#
#     def __iter__(self):
#         print("Class iter")
#         return self.__iter;
#
#
# object = Class(8)
#
# for i in object:
#     print(i)


'''#################### Fibonacci number ###########################'''

# class Fib:
#     def __init__(self, nn):
#         self.__n = nn
#         self.__i = 0
#         self.__p1 = self.__p2 = 1
#
#     def __iter__(self):
#         print("Fib iter")
#         return self
#
#     def __next__(self):
#         self.__i += 1
#         if self.__i > self.__n:
#             raise StopIteration
#         if self.__i in [1, 2]:
#             return 1
#         ret = self.__p1 + self.__p2
#         self.__p1, self.__p2 = self.__p2, ret
#         return ret
#
# class Class:
#     def __init__(self, n):
#         self.__iter = Fib(n)
#
#     def __iter__(self):
#         print("Class iter")
#         return self.__iter
#
# object = Class(8)
#
# for i in object:
#     print(i)


'''##########################'''

# class Fib:
#     def __init__(self, nn):
#         print("__init__")
#         self.__n = nn
#         self.__i = 0
#         self.__p1 = self.__p2 = 1
#
#     def __iter__(self):
#         print("__iter__")
#         return self
#
#     def __next__(self):
#         print("__next__")
#         self.__i += 1
#         if self.__i > self.__n:
#             raise StopIteration
#         if self.__i in [1, 2]:
#             return 1
#         ret = self.__p1 + self.__p2
#         self.__p1, self.__p2 = self.__p2, ret
#         return ret
#
# for i in Fib(10):
#     print(i)


'''###############Generators - where to find them: continued
The previous example shows you a solution where the iterator object is a part of a more complex class.
################################'''

# class Fib:
#     def __init__(self, nn):
#         self.__n = nn
#         self.__i = 0
#         self.__p1 = self.__p2 = 1
#
#     def __iter__(self):
#         print("Fib iter")
#         return self
#
#     def __next__(self):
#         self.__i += 1
#         if self.__i > self.__n:
#             raise StopIteration
#         if self.__i in [1, 2]:
#             return 1
#         ret = self.__p1 + self.__p2
#         self.__p1, self.__p2 = self.__p2, ret
#         return ret
#
# class Class:
#
#     def __init__(self, n):
#         self.__iter = Fib(n)
#
#     def __iter__(self):
#         print("Class iter")
#         return self.__iter;
#
# object = Class(8)
# for i in object:
#     print(i)

''''########### yield ############'''
# def fun(n):
#     for i in range(n):
#         yield i
#
#
# for v in fun(5):
#     print(v)

''''###########  ############'''
# the_list = []
#
# for x in range(10):
#     the_list.append(1 if x % 2 == 0 else 0)
#
# print(the_list)


''''###########  ############'''

# the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
# the_generator = (1 if x % 2 == 0 else 0 for x in range(10))
#
# for v in the_list:
#     print(v, end=" ")
# print()
#
# for v in the_generator:
#     print(v, end=" ")
# print()

''''###########         ############'''

# the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
#
# print(the_list)


''''########### The lambda function
The lambda function is a concept borrowed from mathematics, more specifically, 
from a part called the Lambda calculus, but these two phenomena are not the same.
Mathematicians use the Lambda calculus in many formal systems connected with logic, 
recursion, or theorem provability. 
Programmers use the lambda function to simplify the code, to make it clearer and easier to understand.
A lambda function is a function without a name (you can also call it an anonymous function). 
Of course, such a statement immediately raises the question: how do you use anything that 
cannot be identified? ############'''

# two = lambda: 2
# sqr = lambda x: x * x
# pwr = lambda x, y: x ** y
#
# for a in range(-2, 3):
#     print(sqr(a), end=" ")
#     print(pwr(a, two()))

'''#######################################################'''
# def print_function(args, fun):
#     for x in args:
#         print('f(', x,')=', fun(x), sep='')
# def poly(x):
#     return 2 * x**2 - 4 * x + 2
# print_function([x for x in range(-2, 3)], poly)


'''##################### Lambdas and the map() function ##################################'''
# list_1 = [x for x in range(5)]
# print(list_1)
# list_2 = list(map(lambda x: 2 ** x, list_1))
# print(list_2)
# for x in map(lambda x: x * x, list_2):
#     print(x, end=' ')
# print()


# list_1 = [x for x in range(5)]

# def func(x):
#     a = x ** x
#     return a
#
# list_2 = list(map(func, list_1))
# print(list_2)
#
# list_2 = list(map(lambda x: x ** x, list_1))
# print(list_2)

# list_3 = [5, 6, 7, 8, 9]
# list_2 = list(map(lambda x: 2 ** x, list_3))
# print(list_2)
#
# for x in map(lambda x: 2 ** x, list_1):
#     print(list(x))
# print()

# def even_fn(x):
#   if x % 2 == 0:
#     return True
#   return False
#
# print(list(map(even_fn, [1, 3, 2, 5, 20, 21])))

'''##########################################################################'''
# from random import seed, randint
# seed()
# data = [randint(-10,10) for x in range(5)]
# filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))
# print(data)
# print(filtered)
#
# from random import randint
# data = [randint(-10,10) for x in range(5)]
# filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))
# print(data)
# print(filtered)


'''########################################################'''
# def outer(par):
#     loc = par
#
#     def inner():
#         return loc
#     return inner()
#
# var = 1
# fun = outer(var)
# print(fun)


'''############################################################'''

# def make_closure(par): # par = 2
#     loc = par #loc = 2
#
#     def power(p):
#         return p ** loc
#     return power
#
# a = make_closure(2)
# b = make_closure(3)
#
# for p in range(5):
#     print(p, a(p), b(p))

'''############################################################'''

# class Vowels:
#     def __init__(self):
#         self.vow = "aeiouy "  # Yes, we know that y is not always considered a vowel.
#         self.pos = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.pos == len(self.vow):
#             raise StopIteration
#         self.pos += 1
#         return self.vow[self.pos - 1]
#
#
# vowels = Vowels()
# for v in vowels:
#     print(v, end=' ')


'''##################################################################'''
# any_list = [1, 2, 3, 4]
# even_list = list(map(lambda x: x | 1, any_list)) # Complete the line here.1 3 3 5
# print(even_list)
#
# #0011011
# # 1011100
# # |
# # 1011111

'''############################################################'''
# def replace_spaces(replacement='*'):
#     def new_replacement(text):
#         return text.replace(' ', replacement)
#     return new_replacement
#
#
# stars = replace_spaces()
# print(stars("And Now for Something Completely Different"))

# try:
#     raise Exception
# except BaseException:
#     print("a")
# except Exception:
#     print("b")
# except:
#     print('c')

class A:
    A = 1
    def __init__(self):
        self.a = O
print(hasattr(A,"a"))


numbers =[i * i for i in range(5)]
foo = list(filter(lambda x:x%2,numbers))
print(foo)

x = "\\\\"
print(len(x))

class Class:
    def __init__(self,val = 0):
        pass

object = Class(1,2)