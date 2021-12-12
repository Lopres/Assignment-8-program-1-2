#   This python program is a number guessing name between 0-100
#   From the word itself the user will try to guess what number the program is generated.
#   Using clues like (greater than) or (Less than) will make the game easier for the user.
#   This program uses 'while', and 'if' loops.


import random
number = random.randint(0, 100)

# From the word itself the user will try to guess what number the program is generated.
player_name = input("Hello, What's your name?\n ")
number_of_guesses = 0
print('Okay! '+ player_name+', I am a Guessing game, make a guess between 0 and 100. ' )
print('You have 3 tries to guess the number, Go and make your guesses!\n')

#   Using clues like (greater than) or (Less than) will make the game easier for the user.
#   This program uses 'while', and 'if' loops.
while number_of_guesses < 3:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))