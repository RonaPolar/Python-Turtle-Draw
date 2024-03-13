import turtle
import random
from turtle import Turtle, Screen

screen = Screen()

polar = Turtle("turtle")
polar.speed(-1)
polar.width(5)

colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'brown', 'black', 'white', 'pitch']

def dragging(x, y):#dragging the turtle
    polar.ondrag(None)
    polar.setheading(polar.towards(x, y))
    polar.goto(x,y)
    polar.ondrag(dragging)

def clickright(x, y):#random change color
    polar.color(random.choice(colors))

def clear():#clear the draw
    polar.clear()

def pendowning():#to draw
    polar.down()

def penupping():#to not draw
    polar.up()

def main():
    turtle.listen()

    polar.ondrag(dragging)#for dragging the turtle
    
    turtle.onscreenclick(clickright, 3)#click the right of the mouse for random change color
    turtle.onkey(clear, 'z')#click the 'z' to clear the draw
    turtle.onkey(pendowning,'d')#click the 'd' to draw
    turtle.onkey(penupping,'u')#click the 'u' to not draw

    screen.mainloop()#loop to keep drawing

main()