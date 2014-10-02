# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

num_range = 100
secret_number = 0
num_guesses = 0
# helper function to start and restart the game
def new_game():
    print ""
    print "New game was started! Range is from 0 to", num_range
    global secret_number, num_guesses 
    secret_number = random.randrange(0, num_range)
    if num_range == 100:
        num_guesses = 7
    else:
        num_guesses = 10        
    print "Number of remaining guesses is", num_guesses


# define event handlers for control panel
def range100():
    global num_range
    num_range = 100
    new_game()

def range1000():
    global num_range
    num_range = 1000
    new_game()
    
def input_guess(guess):
    global num_guesses
    input = int(guess)
    print "Guess was", input
    num_guesses = num_guesses - 1
    print "Number of remaining guesses is", num_guesses
    if num_guesses > 0:
        if input > secret_number:
            print "Lower!"
        elif input < secret_number:
            print "Higher!"
        else:
            print "Correct!"
            new_game()
    else:
        if input == secret_number:
            print "Correct!"
        else:
            print "Game over! The number was", secret_number
        new_game()
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()
# always remember to check your completed program against the grading rubric
