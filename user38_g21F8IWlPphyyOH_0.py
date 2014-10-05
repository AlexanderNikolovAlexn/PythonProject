# template for "Stopwatch: The Game"

import simplegui
# define global variables
miliseconds = 0
interval = 100

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    timer.start()
    
def stop_handler():
    timer.stop()
    
def reset_handler():
    global miliseconds
    miliseconds = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global miliseconds
    miliseconds = miliseconds + interval / 100  

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(str(miliseconds), (100, 100), 20, 'Red')
    
# create frame
frame = simplegui.create_frame('Stop watch', 200, 200)
frame.set_draw_handler(draw_handler)
start = frame.add_button('Start', start_handler, 50)
stop = frame.add_button('Stop', stop_handler, 50)
reset = frame.add_button('Reset', reset_handler, 50)
frame.start()
timer = simplegui.create_timer(interval, timer_handler)


# register event handlers  

# start frame


# Please remember to review the grading rubric
