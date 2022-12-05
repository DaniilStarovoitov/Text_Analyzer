"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Daniil Starovoitov
email: daniil.s@seznam.cz
discord: Sweet Procrastination#6256
"""

# greetings
print("""Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""")

# generation 4 digits
import random

def get_hidden_number():
    while True:
        hidden_number = random.randint(1000, 9999)
        if not_duplicates(hidden_number):
            return hidden_number


# check for no duplicates
def not_duplicates(num):
    if len(str(num)) == len(set(str(num))):
        return True
    else:
        return False

# game
def main():
    tries = 10
    hidden_number = get_hidden_number()

    while tries > 0:
        cows = 0
        bulls = 0
        guess_number = int(input('''-----------------------------------------------\nEnter a number: '''))
        if not not_duplicates(guess_number):
            print('-----------------------------------------------\nNo reapeted numbers. Try again.')
            continue
        if guess_number < 1000 or guess_number > 9999:
            print('-----------------------------------------------\nOnly 4 digits. Try again.')
            continue

        hidden_number_list = list(str(hidden_number))
        guess_number_list = list(str(guess_number))

        for h, g in zip(hidden_number_list, guess_number_list):
            if g in hidden_number_list:
                if h == g:
                    bulls += 1
                else:
                    cows += 1
        
        if bulls == 1 and cows == 1:
            print(f'You have {bulls} bull and {cows} cow')
        elif bulls == 1:
            print(f'You have {bulls} bull and {cows} cows')
        elif cows == 1:
            print(f'You have {bulls} bulls and {cows} cow')
        else:
            print(f'You have {bulls} bulls and {cows} cows')
        tries -= 1
        guesses = 10 - tries

        if bulls == 4:
            print(f'Correct, you\'ve guessed the right number\nin {guesses} guesses!')
            break
    else:
        print(f'You lose. Number was {hidden_number}')


main()