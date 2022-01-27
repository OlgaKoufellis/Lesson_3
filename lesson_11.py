'''Практическое задание:(сделайте как можно больше за 30 минут)Напишите программу, которая получает длины двух
катетов в прямоугольном треугольнике и выводит его площадь. Каждое число записано в отдельной строке.
'''
# length1 = int(input('Please eneter the first length: '))
# length2 = int(input('Please eneter the second length: '))
# cathetus = length1 + length2
# print('The length of two cathetus is :', cathetus )
# S = length1 * length2
# print('S of the rectangle is: ', S)




'''
В школе решили набрать три новых математических класса. Так как занятия по математике у них проходят 
в одно и то же время, было решено выделить кабинет для каждого класса и купить в них новые парты. 
За каждой партой может сидеть не больше двух учеников. Известно количество учащихся в каждом из трёх классов. 
Сколько всего нужно закупить парт чтобы их хватило на всех учеников? Программа получает на вход три натуральных
 числа: количество учащихся в каждом из трех классов.Даны три целых числа. Определите, сколько среди них совпадающих. 
 '''
first_class = int(input('Please eneter the first quantity of kids: '))
second_class = int(input('Please eneter the second quantity of kids: '))
third_class = int(input('Please eneter the third quantity of kids: '))
tables = (first_class + second_class + third_class)/2
if first_class == second_class:
    if second_class == third_class:
        print('Quantity of kids are the same in first_class, second_class and third_class:', first_class)
    else:
        print('Quantity of kids are the same in first_class and second_class:', first_class)
elif first_class == third_class:
    print('Quantity of kids are the same in first_class and third_class:', first_class)
elif second_class == third_class:
    print('Quantity of kids are the same in second_class and third_class:', second_class)
print('We need :', tables, 'tables for 3 classes.')





'''
 Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 
 0 (если все числа различны).'''
a = int(input('Please eneter a number1: '))
b = int(input('Please eneter a number2: '))
c = int(input('Please eneter a number3: '))
if a == b and b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)


'''
 Дано натуральное число. Требуется определить, является ли год с данным номером високосным. 
 Если год является високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии с 
 григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100, 
 а также если он кратен 400.
 '''
a = input('Please enter a number:')



#Камень, ножницы, бумага:
#Rock Paper Scissors

player1_score = 0
player2_score = 0
player1_choice = ''
player2_choice = ''
round = 3
#start of game:
for i in range(1, round + 1):
    #Enter data
    player1_choice = str(input("Enter your choice player 1 , please: [r], [s], [p] :"))
    player2_choice = str(input("Enter your choice player 2 , please: [r], [s], [p] :"))
    #Compare data
    if player1_choice == 'r' :
       if player1_choice == 's'
           print('Player 1 win the round!')
           player1_score = player1_score + 1
       elif player2_choice == 'p'
           print('Player 2 win the round!')
           player2_score = player2_score + 1
       else:
          print('Draw round')
if player1_score > player2_score:
    print('Player 1 win the game!')
elif player2_score > player1_score:
    print('Player 1 win the game!')
else:
    print('Draw game!')



# if player1_choice == player2_choice:
#     print('Draw round')
# elif player1_choice == 'r':
#     if player2_choice == 's':
#         print('Player 1 win the round!')
#         player1_score = player1_score + 1
#     else:
#         print('Player 2 win the round!')
#         player2_score = player2_score + 1








