#Камень Ножницы Бумага
#Rock Paper Scissors
import random
game = True
global_player1_score = 0
global_player2_score = 0
game_type = 'pve'#pve
question = ''
while game:
    #Variables
    player1_choice = ''
    player2_choice = ''
    player1_score = 0
    player2_score = 0
    player1_name = str(input("Enter your name player 1 : "))
    player2_name = 'Unknown'
    if game_type == 'pvp':
        player2_name = str(input("Enter your name player 2 : "))
    elif game_type == 'pve':
        player2_name = 'Bot'
    rounds = 3

    #Start of game
    for i in range(1, rounds+1):
        player1_choice = ''
        player2_choice = ''
        #Enter data
        while player1_choice != 'r' and player1_choice != 'p' and player1_choice != 's' and player1_choice != 'l' and player1_choice != 'k':
            player1_choice = str(input(f"Enter your choice {player1_name}: [r],[p],[s],[l],[k] : "))
        while player2_choice != 'r' and player2_choice != 'p' and player2_choice != 's' and player2_choice != 'l' and player2_choice != 'k':
            if game_type == 'pvp':
                player2_choice = str(input(f"Enter your choice {player2_name}: [r],[p],[s],[l],[k]: "))
            elif game_type == 'pve':
                player2_choice = random.choice('krpsl')#Выбирает 1 символ l - lizard, k - Spock
        #Compare data
        if player1_choice == player2_choice:
            print('Draw round')
        elif player1_choice == 'r':
            if player2_choice == 's':
                print(f'{player1_name} win the round!')
                player1_score = player1_score + 1
            elif player2_choice == 'l':
                print(f'{player1_name} win the round!')
                player1_score = player1_score + 1
            elif player2_choice == 'k':
                print(f'{player2_name} win the round!')
                player2_score = player2_score + 1
            elif player2_choice == 'p':
                print(f'{player2_name} win the round!')
                player2_score = player2_score + 1
        elif player1_choice == 'p':
            if player2_choice == 'r':
                print(f'{player1_name} win the round!')
                player1_score = player1_score + 1
            elif player2_choice == 'l':
                print(f'{player2_name} win the round!')
                player2_score = player2_score + 1
            elif player2_choice == 'k':
                print(f'{player1_name} win the round!')
                player1_score = player1_score + 1
            elif player2_choice == 's':
                print(f'{player2_name} win the round!')
                player2_score = player2_score + 1
        elif player1_choice == 's':
            if player2_choice == 'p':
                print(f'{player1_name} win the round!')
                player1_score = player1_score + 1
            elif player2_choice == 'l':
                print(f'{player1_name} win the round!')
                player1_score = player1_score + 1
            elif player2_choice == 'k':
                print(f'{player2_name} win the round!')
                player2_score = player2_score + 1
            elif player2_choice == 'r':
                print(f'{player2_name} win the round!')
                player2_score = player2_score + 1
        elif player1_choice == 'l':
            if player2_choice == 'p':
                print(f'{player1_name} win the round!')
                player1_score = player1_score + 1
            elif player2_choice == 's':
                print(f'{player2_name} win the round!')
                player2_score = player2_score + 1
            elif player2_choice == 'k':
                print(f'{player1_name} win the round!')
                player1_score = player1_score + 1
            elif player2_choice == 'r':
                print(f'{player2_name} win the round!')
                player2_score = player2_score + 1


        question = ''
        while question != 'y':
            question = input('Do you want to continue?: [y/n]:')
            if question == 'y':
                print(f"Great!!! Let's play.")
            elif question == 'n':
                print('So sorry to hear that :(')
                break
        if question == 'n':
            break

    #Compare score
    if player1_score > player2_score:
        print(f'{player1_name} win the game!')
        global_player1_score = global_player1_score + 1
        if question == 'n':
            break
    elif player2_score > player1_score:
        print(f'{player2_name} win the game!')
        global_player2_score = global_player2_score + 1
        if question == 'n':
            break
    else:
        print('Draw game!')
        if question == 'n':
            break
    game = bool(input("If you want continue press any key : "))
