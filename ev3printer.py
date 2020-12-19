#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.parameters import Color
from pybricks.ev3devices import TouchSensor
# Create your objects here

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize a motor at port B.
wheel_motor = Motor(Port.B)
penheight_motor = Motor(Port.C) 
penpos_motor = Motor(Port.A) 
ts = TouchSensor(Port.S1)
# Write your program here

# # Play a sound.
# ev3.speaker.beep()

# # Run the motor up to 500 degrees per second. To a target angle of 90 degrees.
# wheel_motor.run_target(500, 360)
# ev3.screen.draw_text(0, 0, 'Hello', text_color=Color.BLUE, background_color=Color.GREEN)

# # Play another beep sound.
# ev3.speaker.beep(frequency=500, duration=1000)

# ev3.light.on(Color.RED)
# ev3.speaker.set_speech_options(language='en', voice='m1', speed=150, pitch=50)
# ev3.speaker.set_volume(100, which='_all_')
# for x in range (1):
#     ev3.speaker.say('I S H A N Sir')
def forward(distance):
    wheel_motor.run_angle(360, -distance)
def left(distance):
    penpos_motor.run_angle(360, distance)

def penup():
    penheight_motor.run_angle(360, 100)
def pendown():
    penheight_motor.run_angle(360, -100)
x=6
def make_1():
    pendown()
    forward(100)
    penup()
    forward(-100)
    left(-100)
def make_2():
    pendown()
    left(30)
    forward(50)
for x in range(3):
    penup()
while ts.pressed() == False:
    penheight_motor.run_angle(360, -30)
    
    left(-100)
    left(100)
penup()

#forward(400)
#left(100)        
    #run_time(speed, time, then=Stop.HOLD, wait=True)
penups = 0    

def drawDigit(segments):
    global penups
    mydistance = 50
    if segments[0]==1: #Segment A
        pendown()
        penups-=1
        forward(mydistance)
        penup()
        penups+=1
    else:
        penup()  
        penups+=1
        forward(mydistance)
        pendown()
        penups-=1
    while penups < 0:
        penup()
        penups+=1
    while penups > 0:
        pendown()
        penups-=1

    if segments[1]==1: #Segment B
        pendown()
        penups-=1
        forward(mydistance)
        forward(-2*mydistance)
        penup()    
        penups+=1
    else:
        penup() 
        penups+=1 
        forward(mydistance)
        forward(-2*mydistance)
        pendown()
        penups-=1
    while penups < 0:
        penup()
        penups+=1
    while penups > 0:
        pendown()
        penups-=1



    if segments[2]==1: #Segment C
        pendown()
        penups-=1
        left(-mydistance)
        penup()
        penups+=1
    else:
        penup() 
        penups+=1
        left(-mydistance)
        pendown() 
        penups-=1
    while penups < 0:
        penup()
        penups+=1
    while penups > 0:
        pendown()
        penups-=1


    if segments[3]==1: #Segment D
        pendown()
        penups-=1
        forward(mydistance)
        penup()
        penups+=1
    else:
        penup()  
        penups+=1
        forward(mydistance)
        pendown()
        penups-=1
    while penups < 0:
        penup()
        penups+=1
    while penups > 0:
        pendown()
        penups-=1




    if segments[4]==1: #Segment E
        pendown()
        penups-=1
        left(mydistance)
        penup()
        penups+=1
        left(-mydistance)
    else:
        penup()
        penups+=1
        left(mydistance)  
        
        left(-mydistance)
        pendown() 
        penups-=1
    while penups < 0:
        penup()
        penups+=1
    while penups > 0:
        pendown()
        penups-=1



    if segments[5]==1: #Segment F
        pendown()
        penups-=1
        forward(mydistance)
        penup()
        penups+=1
    else:
        penup()  
        penups+=1
        forward(mydistance)
        pendown() 
        penups-=1 
    while penups < 0:
        penup()
        penups+=1
    while penups > 0:
        pendown()
        penups-=1
    if segments[6]==1: #Segment G
        pendown()
        penups-=1
        left(mydistance)
        penup()
        penups+=1
        left(-mydistance)
        forward(-2*mydistance)
        while penups < 0:
            penup()
            penups+=1
        while penups > 0:
            pendown()
            penups-=1
        left(2.5*mydistance)
        pendown()
        penups-=1
    else:
        penup()  
        penups+=1
        left(mydistance)    
        left(-mydistance)
        forward(-2*mydistance)
        while penups < 0:
            penup()
            penups+=1
        while penups > 0:
            pendown()
            penups-=1
        left(2.5*mydistance)
        pendown()
        penups-=1
#drawDigit([1,1,1,1,1,1,0])
#drawDigit([0,0,0,1,0,1,0])
def draw_1():
    drawDigit([0,0,0,1,0,1,0])
def draw_b():
    drawDigit([1,1,1,1,1,1,1])
def draw_a():
    drawDigit([1,1,1,1,1,1,0])
def draw_c():
    drawDigit([0,0,1,1,0,1,1])
# draw_a()
# draw_b()
# draw_c()
def write(word):
    for x in range(len(word)):        
        func = 'draw_'+str(word[x])
        print (func)
        globals()[func]()
        # func()
#write('abc')

#penup()
# while x>5:
#     if ts.pressed() == True:
#         for x in range (7):
#             pendown()
#             #left(50)
#             #left(-100)
if Button().any():
    print ('yes')        