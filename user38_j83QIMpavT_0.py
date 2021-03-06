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
paddle1_pos = [[0, HEIGHT / 2 - HALF_PAD_HEIGHT], 
               [0, HEIGHT / 2 + HALF_PAD_HEIGHT]]
paddle2_pos = [[WIDTH, HEIGHT / 2 - HALF_PAD_HEIGHT],
               [WIDTH, HEIGHT / 2 + HALF_PAD_HEIGHT]]
paddle1_vel = 0
paddle2_vel = 0
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0] # pixels per update (1/60 seconds)
ball_acc = 1.1
score1 = 0
score2 = 0
TEXTSIZE = 60

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    paddle1_vel = 0
    paddle2_vel = 0
    if direction == LEFT:
        ball_vel[0] = -random.randrange(2, 5)
    elif direction == RIGHT:
        ball_vel[0] = random.randrange(2, 5)
    if random.randrange(1, 3) > 1:
        ball_vel[1] = random.randrange(1, 4)
    else: 
        ball_vel[1] = -random.randrange(1, 4)
        
# define event handlers
def new_game():
    global ball_pos, paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    paddle1_pos = [[0, HEIGHT / 2 - HALF_PAD_HEIGHT], 
                   [0, HEIGHT / 2 + HALF_PAD_HEIGHT]]
    paddle2_pos = [[WIDTH, HEIGHT / 2 - HALF_PAD_HEIGHT],
                   [WIDTH, HEIGHT / 2 + HALF_PAD_HEIGHT]]
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    paddle1_vel = 0
    paddle2_vel = 0
    if random.randrange(1, 3) > 1:
        spawn_ball(LEFT)
    else: 
        spawn_ball(RIGHT)
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    #right paddle
    if (ball_pos[0] > WIDTH - PAD_WIDTH - BALL_RADIUS):        
        if (ball_pos[1] >= paddle2_pos[0][1] and ball_pos[1] <= paddle2_pos[1][1]):
            ball_vel[0] = ball_vel[0] * ball_acc            
            ball_vel[0] = -ball_vel[0]
            ball_pos[0] += ball_vel[0]
        else:
            score1 += 1
            spawn_ball(LEFT)         
    #left paddle
    if (ball_pos[0] < BALL_RADIUS + PAD_WIDTH):
        if (ball_pos[1] >= paddle1_pos[0][1] and ball_pos[1] <= paddle1_pos[1][1]):
            ball_vel[0] = ball_vel[0] * ball_acc            
            ball_vel[0] = -ball_vel[0]
            ball_pos[0] += ball_vel[0]
        else:
            score2 += 1
            spawn_ball(RIGHT)    
    if (ball_pos[1] > HEIGHT - BALL_RADIUS) or (ball_pos[1] < BALL_RADIUS):
        ball_vel[1] = ball_vel[1] * ball_acc
        ball_vel[1] = - ball_vel[1]
        ball_pos[1] += ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    # update paddle's vertical position, keep paddle on the screen   
    paddle1_pos[0][1] += paddle1_vel
    paddle1_pos[1][1] += paddle1_vel
    paddle2_pos[0][1] += paddle2_vel
    paddle2_pos[1][1] += paddle2_vel
    if paddle1_pos[0][1] < 0:
        paddle1_pos[0][1] = 0
        paddle1_pos[1][1] = PAD_HEIGHT
        paddle1_vel = 0        
    if paddle1_pos[1][1] > HEIGHT:
        paddle1_pos[0][1] = HEIGHT - PAD_HEIGHT
        paddle1_pos[1][1] = HEIGHT
        paddle1_vel = 0
    if paddle2_pos[1][1] > HEIGHT:
        paddle2_pos[0][1] = HEIGHT - PAD_HEIGHT
        paddle2_pos[1][1] = HEIGHT
        paddle2_vel = 0
    if paddle2_pos[0][1] < 0:
        paddle2_pos[0][1] = 0
        paddle2_pos[1][1] = PAD_HEIGHT 
        paddle2_vel = 0
    
    # draw paddles
    canvas.draw_line(paddle1_pos[0], paddle1_pos[1], 14, 'Orange')
    canvas.draw_line(paddle2_pos[0], paddle2_pos[1], 14, 'Orange')
    # draw scores
    canvas.draw_text(str(score1), [WIDTH / 4, HEIGHT/2], TEXTSIZE, 'White')
    canvas.draw_text(str(score2), [(WIDTH / 4) * 3, HEIGHT/2], TEXTSIZE, 'White')
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    vel = 2
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= vel        
    elif key == simplegui.KEY_MAP["s"]:        
        paddle1_vel += vel        
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += vel        
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= vel
    
def keyup(key):
    global paddle1_vel, paddle2_vel

def button_handler():
    global score1, score2
    score1 = 0
    score2 = 0
    new_game()
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button = frame.add_button('Restart', button_handler, 100)

# start frame
new_game()
frame.start()
