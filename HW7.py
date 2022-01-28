# #GUESS MY NUMBER
'''
1.С каждым выиграшем добавляется одна жизнь
2.Идет проверка на ввод числа "guess_number"( не принимает ввод букв и символов)
3.После каждого выиграша показывает :
    - сколько осталось жизней
    - сколько потрачено ходов для угадывания числа (secret_number)
    - спрашивает хотите ли продолжить игру?:
        а) при ответе 'y'(yes) начинает игру с начала
        б) при ответе 'n'(no) заканчивает игру (Game over)

'''

lifes = 15
while  lifes > 0:
 import random #библиотека рандомных чисел
 secret_number = random.randint(1,20)
 guess_number = ''
 count = 0
 while secret_number != guess_number and lifes > 0:
     guess_number = ''
     while type(guess_number) != int:
         try:
             guess_number = int(input('Enter a number :'))
         except ValueError:
             print('Неверный формат')
     lifes = lifes - 1
     count = count + 1
     if lifes >= 2:
        print(f'You have {lifes} lifes')
     else:
        print(f'You have {lifes} life')
     if secret_number < guess_number:
        print("Your number is greater than a secret_number")
     elif secret_number > guess_number:
        print('Your number is less than a secret_number')
 if lifes >= 0 and secret_number == guess_number:
     print('You Win!!!')
     print(f'You have spend :{count} trials')
     lifes += 1
     yes = ''
     while yes != 'y':
        yes = input('Do you want to continue? [y / n] : ')
        if yes == 'y':
            print(f"Great!!! You can do it. You'll have  {lifes} lifes.")
        elif yes == 'n':
            print('So sorry to hear that :(')
            break
     if yes == 'n':
        print('Game over')
        break
 else:
     print('You Lose!!!')