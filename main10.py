#!/usr/bin/env python3
import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!') #Prints "Greetings"
colors = ['red','orange','yellow','green','blue','violet','purple'] #List of all possible favorite colors
play_again = '' #An empty variable for if the user wants to play again or not
best_count = sys.maxsize            # the biggest number

while (play_again != 'n' and play_again != 'no'): #while loop that runs as long as the user doesn't say no to playing again
    match_color = random.choice(colors) #sets a variable to a random color from the color choices list
    count = 0 #The count variable set to 0
    color = '' #Empty color variable
    while (color != match_color): #While loop that runs as long as the guess is not correcf
        color = input("\nWhat is my favorite color? ")  #The prompt and input for guessing a color
        color = color.lower().strip() #Sets guesses to lowercase and removes spaces
        count += 1 #Increases the count variable everytime a guess is made
        if (color == match_color): #If statement to check if color is correct 
            print('Correct!') #Prints if correct
        else:
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) #If incorrect prints this with the guesses so far
    
    print('\nYou guessed it in {} tries!'.format(count)) #Once they guess correctly this prints with the number of tries

    if (count < best_count): #If statement for if that was their fastest guess
        print('This was your best guess so far!') #Prints it was their best game
        best_count = count #Sets the record variable to the current score

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip() #Asks if they want to play again and lowercases and removes spaces

print('Thanks for playing!') #Prints thanks for playing when the user says no to playing again