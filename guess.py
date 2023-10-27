#!/usr/bin/env python3

import random as ran
print(ran.randint(1,25))

#this defines the range in which the random number may lay
x = ran.randint(1,25)

#number of trials set to zero
n=0
maxn=5
#while loop to be executed n times

while n <= maxn:
    guess = input("Guess a number:   or press q if you want to quit the game")
    if guess == "q":
        print("The game was qot.")
        break
    else:
        guessint = int(guess)
        if guessint == x:
            print('\033[92m'+"'\033[92m'Yeah champ, you got it in",n+1,"ties."'\033[92m')
            break
        elif guessint < x:
            n = n+1
            print('\033[95m'+ "Sorry champ, you need to try again because you were too low. You have",maxn-n , "tries left."'\033[0m')
        elif guessint > x:
            n = n+1
            print('\033[94m'+"Sorry champ, you need to try again because you were too low. You have",maxn-n , "tries left."'\033[0m')
        else:
            print("Maybe you should provide me a number otherwise the game wont be fun!")

