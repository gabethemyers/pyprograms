import random
import time


rps = ['rock', 'paper', 'scissors']
playerwinsdict = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'scissors'}
cont = 'y'
player_score = 0
computer_score = 0

def validitytest(char):
    if isinstance(char, str) and char in rps:
        return True
    else:
        return False


def win_or_lose(player, computer):
    if player == computer:
        return 0  # its a tie
    elif playerwinsdict[player] == computer:
        return 1  # player wins
    else:
        return 2  # computer wins


player_name = input('What is your name? ')
print('Hello ' + player_name + ', let\'s play rock paper scissors!\n')
time.sleep(1)

while cont == 'y':
    comp_choice = random.choice(rps)
    player_input = input('\nplease enter rock, paper, or scissors; to quit enter "quit": ')
    valid = validitytest(player_input)
    if player_input == 'quit':
        cont = 'n'
    else:
        if valid:
            if win_or_lose(player_input, comp_choice) == 0:
                print('Its a Tie\n')
            elif win_or_lose(player_input, comp_choice) == 1:
                print('You won\n')
                player_score += 1
            elif win_or_lose(player_input, comp_choice) == 2:
                print('Computer won\n')
                computer_score += 1
        if not valid:
            print('\nnot a vaild input\n')
print('Thanks for playing ' + player_name + ', your score was ' + str(player_score) + ' and the computers score was ' + str(computer_score))