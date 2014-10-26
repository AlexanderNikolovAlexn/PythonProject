# implementation of card game - Memory

import simplegui
import random

listcards = range(8)
listcards.extend(listcards)
random.shuffle(listcards)
cardexposed = []
for i in range(16):
    cardexposed.append(False)
previndex1 = 0;
previndex2 = 0;
state = 0;
turns = 0;

# helper function to initialize globals
def new_game():
    global listcards, cardexposed, state, turnsprevindex1, previndex2
    listcards = range(8)
    listcards.extend(listcards)
    print listcards
    random.shuffle(listcards)
    print listcards
    cardexposed = []
    for i in range(16):
        cardexposed.append(False)
    previndex1 = 0;
    previndex2 = 0;
    state = 0;
    turns = 0;
    label.set_text("Turns = " + str(turns))
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, turns, previndex1, previndex2
    card = pos[0]/50
    if cardexposed[card] == False:
        cardexposed[card] = True
        if state == 0:
            state = 1
            previndex1 = card
        elif state == 1:
            turns += 1
            state = 2
            previndex2 = card        
        else:
            if listcards[previndex1] != listcards[previndex2]:
                cardexposed[previndex1] = False
                cardexposed[previndex2] = False
            state = 1
            previndex1 = card
    label.set_text("Turns = " + str(turns))
            
# cards are logically 50x100 pixels in size    
def draw(canvas):
    location = [0, 75]
    j = 0;
    show = ''
    for i in range(16):
        if cardexposed[i] == True:
            show = str(listcards[i])
        else:
            show = ''
        canvas.draw_text(show, location, 80, 'Red')
        location[0] += 50
        canvas.draw_line((location[0], 0), (location[0], 100), 3, 'Green')
        j +=1

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = " + str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric