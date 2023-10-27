#!/usr/bin/env python3


nano /Users/benedikthaarscheidt/nano/.nanorc
include /Users/benedikthaarscheidt/nano/.config/nano/R.nanorc


import random as ran
#print(ran.randint(1,25))

#this defines the range in which the random number may lay
x = ran.randint(1,25)
print(x)
#number of trials set to zero
n=0
maxn=5
#while loop to be executed n times
while n < maxn:
    guess = input("Guess a number or press 'q' if you want to quit the game: ")
    if guess == "q":
        print("The game was quit.")
        break
    elif guess.isdigit():  # Check if the input is a valid integer
        guess = int(guess)
        if guess == x:
            print('\033[92m' + f"Yeah champ, you got it in {n + 1} tries." + '\033[0m')
            break
        elif guess < x:
            n = n + 1
            print('\033[95m' + f"Sorry champ, you need to try again because you were too low. You have {maxn - n} tries left." + '\033[0m')
        elif guess > x:
            n = n + 1
            print('\033[94m' + f"Sorry champ, you need to try again because you were too high. You have {maxn - n} tries left." + '\033[0m')
    else:
        print("Maybe you should provide me a number, otherwise, the game won't be fun!")

