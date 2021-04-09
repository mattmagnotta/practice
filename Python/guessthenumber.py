import random
import sys


def main():
    greeter()
    game()

def greeter():

    print('welcome to guess the fucking number')
    name = input('whats your slave name')
    print(f'alright, {name} lets get to fucking buisness ')



def game():
    choice_amount = list(range(10))
    random_number = random.choice(choice_amount)
    game_in_session = True
    user_guess_amount = 0
    while game_in_session:
        user_guess_amount += 1
        user_guess = int(input('enter a number between 1-10:'))


        if user_guess < random_number:
            print('higher')

        elif user_guess > random_number:
                print('lower')

        elif user_guess == random_number:
                game_in_session = False
                print('winner winner chicken dinner')
                print(f'you took {user_guess_amount} guessess')

if __name__ == '__main__':
    main()
