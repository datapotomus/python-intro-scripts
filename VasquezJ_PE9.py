# Program selects a random number between 1 and 100 and prompts the user to guess it. 
# The program will provide hints and continue until the correct number is guessed.

import random
rand_num = random.randint (1,100)
try:
    print('\nPlease guess a number between 1 and 100: ', end='')
    guess = int(input())


    while True:
        if guess < rand_num:
            print('\nGuess is too low! Try again: ', end='')
            guess = int(input())
        elif guess > rand_num:
            print('\nGuess is too high! Try again: ', end='')
            guess = int(input())
        else:
            break

    if guess == rand_num:
        print('\nCongratulations, you guessed the number!')

except ValueError:
    print('**Please enter a valid number**\n')

