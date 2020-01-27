#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
if (color.lower().strip() == 'red'):
    print('Correct!')
else:
    print('Sorry, try again.')
#Line 9 now also removes spaces at the beggining and end of the input with .strip()
#The only way I can think of is spelling it differently