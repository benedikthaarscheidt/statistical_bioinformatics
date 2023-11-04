#!/usr/bin/env python3
import sys, os, re
def wc (filename):
    # open file in read mode
    file = open(filename, "r")
    #define all the counters for the different 

    #set lines to 1 because apparently the linesum is 1 short
    nlines = 1 
    nwords = 0
    nchars = 0
    nlow   = 0 ; 
    nupp   = 0 ; 
    
    #loop over lines in file
    for line in file:
        
        #for every line increase the counter for lines and the characters in the lines
        nchars = nchars + len(line)+1
        nlines += 1
        #split the lines into words by assuming words are separated by a space - this is default in split function
        words = line.split()

        #for every word in line increase the wordcounter by 1
        for word in words:
            nwords+=1

            #for every character in a word check if the character is alphabetic (otherwise brackets will also be counted) 
            #if alphabetic check if lower and if, increase nlow by 1 and if it is not lower it must be uppercase 
            for char in word:
                if char.isalpha():
                    if char.islower():
                        nlow += 1
                    else:
                        nupp += 1

    #close file again so that we dont have it opened in the backround
    file.close()
    return(tuple((nlines,nwords,nchars,nlow, nupp,filename)))
 # use our Python file for testing
print(wc("haarscheid-wc.py"))


