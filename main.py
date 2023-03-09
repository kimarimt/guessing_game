from art import logo
from random import randint
import os
import time


def clear():
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    print(logo)
    print('I\'m thinking of a number between 1 and 100')
    
    secret_number = randint(1, 100)
    difficulty = input('\'Easy\' or \'Hard\' difficulty: ').lower()
    lives = 10 if difficulty == 'easy' else 5

    clear()
    guess = int(input('Enter guess: '))

    while True:
        if lives == 0:
            print(f'You ran out of lives. The number was {secret_number}')
            clear()
            break

        if guess == secret_number:
            print('You Win!')
            clear()
            break
        elif guess < secret_number:
            print('Too Low!')
        else:
            print('Too High!')

        lives -= 1
        clear()
        guess = int(input('Enter guess: '))


if __name__ == '__main__':
    main()
