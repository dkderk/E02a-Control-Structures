#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
print(color)
#This is different than main01 because it sets the users input to the variable color and prints it back out to the user
#It does what I expected