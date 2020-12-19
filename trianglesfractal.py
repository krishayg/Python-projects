import turtle
from random import choice

def make_triangle(tur):
  global distance

  for c in range(3):
    tur.pendown()
    tur.forward(distance/2)
    ts.append(tur.clone())
    tur.forward(distance/2)
    tur.left(120)
    # tur.pendown()
    # tur.forward(distance/2)
    # ts.append(tur.clone())
    # tur.forward(distance/2)
    # tur.left(120)
    # tur.pendown()
    # tur.forward(distance/2)
    # ts.append(tur.clone())
    # tur.forward(distance/2)
    # tur.left(120)
t=turtle.Turtle()
t.penup()
t.goto(-100,-100)
t.pendown()
angle=45
distance=200
ts = []
t.speed(0)
t.hideturtle()
# t.pencolor('black')
ts.append(t)
myvar=1
mycolors = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray']
while True: 
  col = choice(mycolors)
  for x in range (myvar):
    theturtle = ts.pop(0)
    theturtle.pencolor(col)
    make_triangle(theturtle)
  myvar=myvar*3
  distance = distance/2