#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = ''
color = input("What is my favorite color? ")
while (color != 'red'):
    
    color = color.lower().strip()
    if (color == 'red'):
        print('Correct!')
    elif (color == 'pink'):
        print('Close!')
    else:
        print('Sorry, try again.')
#10-17 are indented because they are contained within the while loop
#If line 10 was before line 9 it would only ask for the color input once causing the while loop to run forever unless red was the first input
