import turtle  
polar = turtle.Turtle()  
polarBg = turtle.Screen()
polarBg.bgcolor("black") #background color
polar.pensize(3)
polar.hideturtle()

   
# To design curve  
def curve():  
    for i in range(200): #loop curve
        polar.right(1)  
        polar.forward(1)  

polar.color("red", "Pink") #color of heart
polar.begin_fill()  
polar.left(140)  
polar.forward(115)  
curve()  
   
polar.left(120)  
curve()  
polar.forward(112)  
polar.end_fill()  
 
turtle.done()