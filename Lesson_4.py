age = 18 # PEP 8 CISCO
if age < 18: #True
    print('Child')
if age >= 18:
    print('Adult')

age = 18 # PEP 8 CISCO
if age <= 18: #True
    print('Child')
if age >= 18:
    print('Adult')

age = 18
if age <= 18:
    print('Child')
else:
    print('Adult')

age = 13 # PEP 8 CISCO
if age <= 18: #True
    print('Child')
else:
    print('Adult')




weight = 120
if weight <= 150:
    print(weight)
else:
    print('Attention!!!!')


age = -20
if age < 0:
    print('ERROR')  #else if
elif age <= 18:
    print('Child')
else:
    print('Adult')

name = 'Olga'
besty = 'Mariya'
age = 36
drink = 'milk shake'
print("Hello! Me name is ", name, ".", "I have a best friend, her name is ", besty, ".", "She is", age,
      "years old and her favorite drink is a", drink)

age = 18  # PEP 8 CISCO
if age < 18:  # True
    print('Child')
if age >= 18:
    print('Adult')

age = 18  # PEP 8 CISCO
if age <= 18:  # True
    print('Child')
if age >= 18:
    print('Adult')

age = 18
if age <= 18:
    print('Child')
else:
    print('Adult')

age = 13  # PEP 8 CISCO
if age <= 18:  # True
    print('Child')
else:
    print('Adult')

weight = 120
# если вес мень 150 выводит вес если вес больше 150 выводит привышено значение

weight = 120
if weight <= 150:
    print(weight)
else:
    print('Attention!!!!')

age = -20
if age < 0:
    print('ERROR')  # else if
elif age <= 18:
    print('Child')
else:
    print('Adult')

age = 13
if age < 0:
    print('ERROR')  # else if
elif age < 18:
    print('Child')
elif age < 13:
    print('Teen')
else:
    print('Adult')
print('TRIS')

age = 1100
if age < 0:
    print('ERROR')  # else if
elif age < 13:
    print('Child')
elif age < 18:
    print('Teen')
elif age < 135:
    print('Adult')
else:
    print('you are dead')

weight = 25
if weight < 0:
    print('you does not EXIST')
elif weight <= 30:
    print("you are super light,like a flower")
elif weight <= 60:
    print('your weight is perfect!!!')
elif weight <= 150:
    print('OMG!!!')

weight = 120
if type(weight) != type(1):
    print('yNo txt allowed')
if weight < 0:
    print('you does not EXIST')
elif weight <= 30:
    print("you are super light,like a flower")
elif weight <= 60:
    print('your weight is perfect!!!')
elif weight <= 150:
    print('OMG!!!')

weight = 120
if type(weight) == type(1):
    print('Text type')
elif type(weight) == type(1.0):
    print("Float type")
if weight < 0:
    print('you does not EXIST')
elif weight <= 30:
    print("you are super light,like a flower")
elif weight <= 60:
    print('your weight is perfect!!!')
elif weight <= 150:
    print('OMG!!!')

gender = 'male'
age = 13
if gender == "male":
    if age < 18:
        print('A boy')
    else:
        print('A man')
elif gender == 'femail':
    if age < 18:
        print('A girl')
    else:
        print('A woman')
else:
    if age < 18:
        print('A child')
    else:
        print('An adult')

gender = 'male'
age = 13
if gender == "male":
    if age < 18:
        print('A boy')
    else:
        print('A man')
elif gender == 'femail':
    if age < 18:
        print('A girl')
    else:
        print('A woman')
else:
    if age < 18:
        print('A child')
    else:
        print('An adult')

number1 = 1
command = '-'
number2 = 2
if command == "+":
    print(number1, command, number2, "=", number1 + number2)
elif command == '-':
    print(number1, command, number2, "=", number1 - number2)
elif command == '*':
    print(number1, command, number2, "=", number1 * number2)
elif command == '/':
    print(number1, command, number2, "=", number1 / number2)
else:
    print('incorrect command!')

number1 = 1
command = '+'
number2 = 2
if command == "+":
    print(number1, command, number2, "=", number1 + number2)
elif command == '-':
    print(number1, command, number2, "=", number1 - number2)
elif command == '*':
    print(number1, command, number2, "=", number1 * number2)
elif command == '/':
    if number2 != 0:
        print(number1, command, number2, "=", number1 / number2)
    else:
        print('Zero division')
else:
    print('incorrect command!')

# #CTRL + ALT + L


number1 = 1
command = '+'
number2 = 2
if type(number1) == type(1):
    if type(number2) == type(1):
        if command == '+':
            print(number1, command, number2, '=', number1 + number2)
        elif command == '-':
            print(number1, command, number2, '=', number1 - number2)
        elif command == '*':
            print(number1, command, number2, '=', number1 * number2)
        elif command == '/':
            if number2 != 0:
                print(number1, command, number2, '=', number1 / number2)  # PEP 8 Ctrl + Alt + L
            else:
                print('Zero division')
        else:
            print('Incorrect command')

number1 = 1
command = '+'
number2 = 2
if type(number1) == type(1):
    if type(number2) == type(1):
        if command == '+':
            print(number1, command, number2, '=', number1 + number2)
        elif command == '-':
            print(number1, command, number2, '=', number1 - number2)
        elif command == '*':
            print(number1, command, number2, '=', number1 * number2)
        elif command == '/':
            if number2 != 0:
                print(number1, command, number2, '=', number1 / number2)  # PEP 8 Ctrl + Alt + L
            else:
                print('Zero division')
        else:
            print('Incorrect command')

num1 = 54
command = '+'
num2 = 2
if type(num1) == type(1):
    if type(num2) == type(1):
        if command == '+':
            print(f"{num1} {command} {num2} = {num1 + num2}")
        elif command == '-':
            print(f"{num1} {command} {num2} = {num1 - num2}")
        elif command == '*':
            print(f"{num1} {command} {num2} = {num1 * num2}")
        elif command == '/':
            if num2 != 0:
                print(f"{num1} {command} {num2} = {num1 / num2}")
            else:
                print("Zero division")
        else:
            print("Error1")
    else:
        print("Error2")
else:
    print("Error3")

num1 = input("Enter number 1:")
command = input("Enter command:")
num2 = input("Enter number 2:")
if type(num1) == type(1):
    if type(num2) == type(1):
        if command == '+':
            print(f"{num1} {command} {num2} = {num1 + num2}")
        elif command == '-':
            print(f"{num1} {command} {num2} = {num1 - num2}")
        elif command == '*':
            print(f"{num1} {command} {num2} = {num1 * num2}")
        elif command == '/':
            if num2 != 0:
                print(f"{num1} {command} {num2} = {num1 / num2}")
            else:
                print("Zero division")
        else:
            print("Error")
    else:
        print("Error")
else:
    print("Error")

age = 13
if age < 0:
    print('ERROR')  #else if
elif age < 18:
    print('Child')
elif age < 13:
    print('Teen')
else:
    print('Adult')
print('TRIS')




age = 1100
if age < 0:
    print('ERROR')  #else if
elif age < 13:
    print('Child')
elif age < 18:
    print('Teen')
elif age < 135:
    print('Adult')
else:
    print('you are dead')


weight = 25
if weight <0:
    print('you does not EXIST')
elif weight <= 30:
    print("you are super light,like a flower")
elif weight <=60:
    print('your weight is perfect!!!')
elif weight <=150:
    print('OMG!!!')



weight = 120
if type(weight) != type(1):
    print('yNo txt allowed')
if weight <0:
    print('you does not EXIST')
elif weight <= 30:
    print("you are super light,like a flower")
elif weight <=60:
    print('your weight is perfect!!!')
elif weight <=150:
    print('OMG!!!')


weight = 120
if type(weight) == type(1):
    print('Text type')
elif type(weight) ==type(1.0):
    print("Float type")
if weight <0:
    print('you does not EXIST')
elif weight <= 30:
    print("you are super light,like a flower")
elif weight <=60:
    print('your weight is perfect!!!')
elif weight <=150:
    print('oooops')
