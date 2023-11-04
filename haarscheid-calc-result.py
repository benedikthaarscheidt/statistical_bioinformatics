#!/usr/bin/env python3

### File:     haarscheid-calc.py
### Date:     2023-10-27
### Author:   Benedikt Haarscheidt, University of Potsdam
### Homework: Week 2 - Calculator

import sys
import random

### declare ANSI colors red, green, yellow etc...

CYAN    = '\033[96m'
MAGENTA = '\033[95m'
BLUE    = '\033[94m'
YELLOW  = '\033[93m'
GREEN   = '\033[92m'
RED     = '\033[91m'
HEAD    = '\033[95m'
WARN    = '\033[93m'
FAIL    = '\033[91m'
RSET    = '\033[0m'
BOLD    = '\033[1m'
UDLN    = '\033[4m'


def add(user):
    print("inside addition")
    #specify how many rounds you want to play in the add game 
    n = int(input("how many runs do you want to have in this adding game?: "))
    i = 0
    correct = 0
    #we want to play until i (which is increased after entering a number)equals out number m 
    while i<n:
        # create two random numbers
        x1=random.randint(10,200)
        x2=random.randint(10,200)
        # formulate a addition question
        print("What is the sum of", x1, "and", x2)
        # use input to get the anwer
        sol = input("Enter your solution here:   ")      
        # compare provided with real solution
        if sol == "q":
            print("Maybe next time!")
            break
        #check if the input is a number- if, the sum of the random numbers is calculated and the input compared with the actual sum
        elif sol.isdigit():
            sol = int(sol)
            xsum = x1+x2

            if sol == xsum:
                print(GREEN+"You are a real Käpsele!"+RSET)
                #when the input matches the sum, the correct counter is increased 
                correct+=1
                i+=1
            else:
                print(RED+"This was not correct. The correct solution would have been", xsum, "- Please try again."+RSET)
                i+=1
        else:
            print("Your input was't a number. Calculating with letters is no fun.")
    #when i=n the precentage of correctness is passed to the writeResult functionwhich appends the result to the file 
    percentage = correct/n*100   
    writeResult("result.txt", user, percentage, 'a')  
     #when i = n then sil for the average correctness is calculated and returned to the menu  
    sil= correct/n 
    return(sil)

def multi(user):
    print("inside multi") 
    n = int(input("how many runs do you want to have in this multiplication game?: "))
    i=0
    correct=0
    while i<n:  
        x1=random.randint(2,14)
        x2=random.randint(2,14)
        #formulate multiplication question
        print("What is the product of", x1, "multiplied by", x2)
        # use input to get the anwer
        sol = input("Enter your solution here:   ")  
        #compare input with real solution
        if sol == "q":
            print("Maybe next time")
            break
        elif sol.isdigit():
            sol = int(sol)
            xprod = x1*x2
            if sol == xprod:
                    print(GREEN+"You are a real Käpsele!"+RSET)
                    correct +=1
                    i+=1
            else:
                    print(RED+"This was not correct. The correct solution would have been", xprod, "- Please try again."+RSET)
                    i+=1
        else:
            print("Your input was't a number. Calculating with letters is no fun.")
            
    percentage = correct/n*100 
    writeResult("result.txt", user, percentage, 'm')  
    sil= correct/n 
    return(sil)

def writeResult(filename, *args,):
    #opens the files specified in the argument of the function
    with open(filename, "a") as file:
        #takes the undefined number of args and separates them by a tab 
        data = "\t".join(map(str, args))
        #appends the separated args to the file 
        file.write(data + "\n")
    file.close()
    print(file)

#in the main we get z which specifies the total amout of rounds we wanna play. z = a+m
def menu(z):
    user = input("Enter your username here:    ")
    x = 0
    #sets result counter for calculation of the average percentage of correctness to 0 
    result = 0

    while x<z:
        sel=input("Select: (a)dd, m(multi), (q)uit: ")
        if sel == "q"  : break
        if sel == "a":
            #the result is the sum of the number of correct solutions defided by the number of tries (sum of correct/n)
            result = result + add(user)
        elif sel == "m":
            result = result + multi(user)
        else: print("Wrong choice!")
        x+=1
    #calculates the average of all tries  by definding the result by z 
    avrg = result/z*100
    print("Your average procentage was", avrg,"%")
           
def main():
    print(RED, "I am in red?", RSET)
    x = input("How many rounds do you want to play in total: ")
    z = int(x)
    menu(z)

if __name__ == "__main__":
    main()
