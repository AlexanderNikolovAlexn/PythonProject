# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0] # pixels per update (1/60 seconds)

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    if direction == LEFT:
        ball_vel[0] = random.randrange(120, 240)
    elif direction == RIGHT:
        ball_vel[0] = - random.randrange(120, 240)
    ball_vel[1] = random.randrange(60, 180)

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints4
    paddle1_pos = [[0, HEIGHT / 2 - HALF_PAD_HEIGHT], 
                   [0, HEIGHT / 2 + HALF_PAD_HEIGHT]]
    paddle2_pos = [[WIDTH, HEIGHT / 2 - HALF_PAD_HEIGHT],
                   [WIDTH, HEIGHT / 2 + HALF_PAD_HEIGHT]]

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    
    
    # draw paddles
    canvas.draw_line(paddle1_pos[0], paddle1_pos[1], 14, 'Orange')
    canvas.draw_line(paddle2_pos[0], paddle2_pos[1], 14, 'Orange')
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    vel = 20
    if key == simplegui.KEY_MAP["w"]:
        paddle1_pos[0][1] -= vel
        paddle1_pos[1][1] -= vel
        if paddle1_pos[0][1] < 0:
            paddle1_pos[0][1] = 0
            paddle1_pos[1][1] = PAD_HEIGHT
    elif key == simplegui.KEY_MAP["s"]:        
        paddle1_pos[0][1] += vel
        paddle1_pos[1][1] += vel
        if paddle1_pos[1][1] > HEIGHT:
            paddle1_pos[0][1] = HEIGHT - PAD_HEIGHT
            paddle1_pos[1][1] = HEIGHT
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_pos[0][1] += vel
        paddle2_pos[1][1] += vel
        if paddle2_pos[1][1] > HEIGHT:
            paddle2_pos[0][1] = HEIGHT - PAD_HEIGHT
            paddle2_pos[1][1] = HEIGHT
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_pos[0][1] -= vel
        paddle2_pos[1][1] -= vel
        if paddle2_pos[0][1] < 0:
            paddle2_pos[0][1] = 0
            paddle2_pos[1][1] = PAD_HEIGHT
    
def keyup(key):
    global paddle1_vel, paddle2_vel


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
