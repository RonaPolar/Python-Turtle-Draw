import turtle
t = turtle.Turtle()
t.shape('turtle')

def move_left():
  t.penup()
  t.setheading(180)
  t.fd(100)
  
def move_right():
  t.penup()
  t.setheading(0)
  t.fd(100)
  
def move_up():
  t.penup()
  t.setheading(90)
  t.fd(100)
  
def move_down():
  t.penup()
  t.setheading(270)
  t.fd(100)
  
def draw_square():
  t.fillcolor('SeaGreen')
  t.pendown()
  t.begin_fill()
  for i in range(4):
    t.fd(85)
    t.rt(90)
  t.penup()
  t.end_fill()

def draw_circle():
  t.fillcolor('HotPink')
  t.pendown()
  t.begin_fill()
  t.circle(45)
  t.end_fill()
  
def draw_triangle():
  t.fillcolor('red')
  t.pendown()
  t.begin_fill()
  for i in range (3):
    t.fd(90)
    t.rt(120)
  t.penup()
  t.end_fill()
  
screen = turtle.Screen()
screen.onkey(move_left, 'Left')
screen.onkey(move_right, 'Right')
screen.onkey(move_up, 'Up')
screen.onkey(move_down, 'Down')
screen.onkey(draw_square, 's')
screen.onkey(draw_circle, 'c')
screen.onkey(draw_triangle, 't')
screen.listen()
screen.mainloop()