# template for "Stopwatch: The Game"

import simplegui
# define global variables
miliseconds = 0
interval = 100
suc_stop = 0
tot_stop = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    d = t % 10
    c = t / 10
    a = 0
    if c > 10 and c <= 59:        
        b = ''
    elif c < 10:
        c = str(0) + str(c)
    else:
        a = c / 60
        c = (t - a * 60 * 10 - d) / 10
        if c < 10:
            c = str(0) + str(c)
    return str(a) + ':' + str(c) + '.' + str(d)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    timer.start()
    
def stop_handler():
    global suc_stop, tot_stop
    if timer.is_running():
        if miliseconds % 10 == 0:
            suc_stop = suc_stop + 1
        tot_stop = tot_stop + 1    
    timer.stop()
    
def reset_handler():
    global miliseconds, suc_stop, tot_stop
    miliseconds = 0
    suc_stop = 0
    tot_stop = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global miliseconds
    miliseconds = miliseconds + interval / 100  

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(miliseconds), (70, 110), 30, 'White')
    canvas.draw_text(str(suc_stop) + '/' + str(tot_stop), (150, 20), 20, 'White')
    
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
