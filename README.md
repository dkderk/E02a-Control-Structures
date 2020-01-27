All answers are also commented in the python files

Main01.py:
This code prints "Greetings" to the user and then asks them to input their favorite color

The program doesn't do anything with their answer

Main02.py
This is different than main01 because it sets the users input to the variable color and prints it back out to the user

It does what I expected

Main03.py
This program checks to see if the user guesses it's favorite color correct. 

If they guess "Red" its prints correct, otherwise it prints try again

"Red" has to be spelled and capitalized that way or it doesnt work

Main04.py
This tries to solve the capitalization issue by making "red" another valid way to get Correct as a response

There are still problems with all other possible capitalizations

Main05.py
Line 9 should take the users input and make it all lowercase to solve the capitalization issue

Adding spaces before or after the word makes it print try again

Main06.py
Line 9 now also removes spaces at the beggining and end of the input with .strip()

The only way I can think of is spelling it differently

Main07.py
The only real difference in this program is now guessing pink will have it tell you you're close

Which is what line 12 does 

Main08.py
10-17 are indented because they are contained within the while loop

If line 10 was before line 9 it would only ask for the color input once causing the while loop to run forever unless red was the first input

Main09.py
Count is a variable that increases by 1 each time the user makes a guess and goes through the while loop

Line 21 formats the print statement to tell the user the count value, AKA how many guesses it took them

Main011.py
This is a function called choose_color that chooses a random color until it gets a color that is different from the last color

