#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
if (color.lower() == 'red'):
    print('Correct!')
else:
    print('Sorry, try again.')
#Line 9 should take the users input and make it all lowercase to solve the capitalization issue
#Adding spaces before or after the word makes it print try again
