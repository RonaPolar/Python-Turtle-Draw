import turtle
import random
from turtle import *

polar = turtle.Turtle()
polar.speed(0)
polar.width(5)

colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black']#pen colors

def up():#to go up
    polar.setheading(90)
    polar.forward(100)

def down():#to go down
    polar.setheading(270)
    polar.forward(100)

def right():#to go right
    polar.setheading(0)
    polar.forward(100)

def left():#to go left
    polar.setheading(180)
    polar.forward(100)

def clickright(x, y):#random change color
    polar.color(random.choice(colors))

def clickleft(x, y):#copying the turtle
    polar.stamp()

def pendowning():#to draw
    polar.down()

def penupping():#to not draw
    polar.up()

turtle.listen()

turtle.onscreenclick(clickright, 1)#click the left of the mouse for random change color
turtle.onscreenclick(clickleft, 3)#click the right of the mouse to copy turtle
turtle.onkey(up, 'Up')#click the up arrow key to go up
turtle.onkey(down, 'Down')#click the down arrow key to go down
turtle.onkey(right, 'Right')#click the right arrow key to go right
turtle.onkey(left, 'Left')#click the left arrow key to go left
turtle.onkey(pendowning,'d')#click the 'd' to draw
turtle.onkey(penupping,'u')#click the 'u' to not draw

turtle.mainloop()#loop to keep drawing