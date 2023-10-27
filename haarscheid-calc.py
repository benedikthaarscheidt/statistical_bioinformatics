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


def add():
    print("inside addition")
    while True:
        # create two random numbers
        x1=random.randint(10,200)
        x2=random.randint(10,200)
        # formulate a addition question
        print("What is the sum of", x1, "and", x2)
        # use input to get the anwer
        sol = input("Enter your solution here:   ")      
        # compare provided with real solution
        if sol == "q":
            print("You can try your luck next time")
            break
        elif sol.isdigit():
            sol = int(sol)
            xsum = x1+x2
            if sol == xsum:
                print(GREEN+"You are a real Käpsele!"+RSET)
                return "s"
            else:
                print(RED+"This was not correct. The correct solution would have been", xsum, "- Please try again."+RSET)
                return "f"
                
        else:
            print("Your input was't a number. Calculating with letters is no fun.")
            add()

def multi():
    print("inside multi") 
    while True:  
        x1=random.randint(2,14)
        x2=random.randint(2,14)
        #formulate multiplication question
        print("What is the product of", x1, "multiplied by", x2)
        # use input to get the anwer
        sol = input("Enter your solution here:   ")  
        #compare input with real solution
        if sol == "q":
            print("You can try your luck next time")
            break
        elif sol.isdigit():
            sol = int(sol)
            xprod = x1*x2
            if sol == xprod:
                    print(GREEN+"You are a real Käpsele!"+RSET)
                    return "s" 
                    
            else:
                print(RED+"This was not correct. The correct solution would have been", xprod, "- Please try again."+RSET)
                return "f"
        else:
            print("Your input was't a number. Calculating with letters is no fun.")
            break




def menu(n=5):
    x=0
    successcounter=0
    failcounter=0

    while True:
        x += 1
        sel=input("Select: (a)dd, m(multi), (q)uit: ")
        if sel == "q"  : break
        elif sel == "a":
            result = add()
            if result == "s":
                successcounter= successcounter+1
            if result == "f":
                failcounter= failcounter+1
        elif sel == "m":
            mesult = multi()
            if mesult == "s":
                successcounter= successcounter+1
            if mesult == "f":
                failcounter= failcounter+1
        else: print("Wrong choice!")
        if x >= n:
            break
    print("You succeeded", successcounter," and failed", failcounter," times")    
           
def main():
    print(RED,"I am in red?",RSET)
    menu()

if __name__ == "__main__":
    main()