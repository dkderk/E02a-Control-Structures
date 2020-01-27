#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
if (color == 'Red'):
    print('Correct!')
else:
    print('Sorry, try again.')
#This program checks to see if the user guesses it's favorite color correct. 
#If they guess "Red" its prints correct, otherwise it prints try again
#"Red" has to be spelled and capitalized that way or it doesnt work