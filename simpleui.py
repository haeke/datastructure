

import simplegui

counter = 0

def increment():
    global counter
    counter += 1

def tick():
    increment()
    print counter

#create a frame
frame = simplegui.create_frame("GUI Test", 100, 100)

#register the handler
timer = simplegui.create_timer(1000, tick)

#start frame and timers
frame.start()
timer.start()
