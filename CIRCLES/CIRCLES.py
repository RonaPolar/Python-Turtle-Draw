import random
from turtle import *

t = Turtle()

colors=["Red","Coral","Yellow","SeaGreen","Blue","Indigo","MediumOrchid"]
t.penup()
t.speed(5)

for i in range(200):
  x = random.randint(-250,250)
  y = random.randint(-250,250)
  circle_size = random.randint(1,100)
  circle_color = random.choice(colors)
  t.goto(x,y)
  t.pendown()
  t.color(circle_color)
  t.begin_fill()
  t.pencolor("black")
  t.pensize(1)
  t.circle(circle_size)
  t.end_fill()
  t.penup()