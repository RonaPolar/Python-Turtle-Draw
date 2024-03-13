import turtle
import random
t = turtle.Turtle()
t.pensize(2)
t.speed(8)
t.penup() #not ready to draw

#Start Line
t.goto(-270,180)#width,height
t.pendown() #ready to draw
t.write("Player", align='center', font = ['Arial', 16, 'normal']) #text, font style, size
t.penup() #not ready to draw
t.right(90)  #turn by 90 degree/downward
t.forward(2) #forward by 2 for the space of text
t.pendown() #ready to draw
t.forward(288) #forward downward for the line
t.left(90) #turn by 90 degree
t.penup() #not ready to draw

#writting players numbers
tWrite1 = turtle.Turtle()
tWrite1.hideturtle() #not showing turtle
tWrite1.penup() #not ready to draw
tWrite1.goto(-290,150)
tWrite1.right(90)  #turn by 90 degree

for w in range(5): #loop for creating the lines with label
  tWrite1.pendown() #ready todraw
  tWrite1.write(w, font=("Verdana", 20, "bold")) #writing the label for players
  tWrite1.penup() #not ready to draw
  tWrite1.forward(50) #forward for wring text
  
t.goto(260,135) #positioning
t.right(0) #turn by 0 degree

# drawing lane race
for l in range(4): #loop for creating the lines with label
  t.pendown() #not ready to draw
  t.fillcolor('Red') #color
  t.begin_fill() #start coloring
  t.backward(500) #drawing line backward
  t.right(90) #turn by 90 degree
  t.forward(50) #forward turtle in the left
  t.left(90) #turn  by 90 degree
  t.forward(500) #drawing line forward 
  t.right(0) #turn  by 0 degree for loop
  t.end_fill() #end coloring
t.backward(500) #drawing line backward to have line at the last
t.hideturtle() #not showing turtle
                                    
#Finish Line
t.penup() #ready to draw
t.goto(260,180) #width,height
t.showturtle() #showing turtle
t.write("Finish Line", align='center', font = ['Arial', 16, 'normal']) #text, font style, size
t.penup() #not ready to draw
t.right(90)  #turn by 90 degree/downward
t.forward(2) #forward by 2 for the space of text
t.pendown() #ready to draw
t.forward(288) #forward downward for the line
t.left(90) #turn  by 90 degree
t.hideturtle() #not showing turtle

t1 = turtle.Turtle() #first turtle
t1.color('Fuchsia') #first turtle color
t1.shape('turtle') #"turtle" shape
t1.penup() #not ready to draw
t1.goto(-260,110) #positioning the turtle
t1.pendown() #ready to draw

t2 = t1.clone() #cloning from first turtle to be 2nd turtle
t2.color('DarkMagenta') #second turtle color
t2.shape('turtle') #"turtle" shape
t2.penup() #not ready to draw
t2.goto(-260,60) #positioning
t2.pendown() #ready to draw

t3 = t2.clone() #cloning from second turtle to be 3rd turtle
t3.color('DeepSkyBlue') #second turtle color
t3.shape('turtle') #"turtle" shape
t3.penup() #not ready to draw
t3.goto(-260,10) #positioning
t3.pendown() #ready

t4 = t3.clone() #cloning from third turtle to be 4th turtle
t4.color('DarkBlue') #"turtle" color
t4.shape('turtle') #"turtle" shape
t4.penup() #not ready to draw
t4.goto(-260,-40) #positioning
t4.pendown() #ready to draw

die = [1,2,3,4,5,6] #die

#declarations of race winner and input for die
for i in range(20): #loop
 if t1.pos() >=(260,110): #width,height
        print("PLAYER ONE WINS")
        break
 elif t2.pos() >=(260,60): #width,height
        print("PLAYER TWO WINS")
        break
 elif t3.pos() >=(260,10): #width,height
        print("PLAYER THREE WINS")
        break
 elif t4.pos() >=(260,-40): #width,height
        print("PLAYER FOUR WINS")
        break
 else:  #die roll random imput & outcome
        t1_turn = input("Press Keyword 'Enter' to roll the die")
        die_outcome = random.choice(die)
        print("Die number is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        t1.fd(20*die_outcome)

        t2_turn = input("Press Keyword 'Enter' to roll the die")
        die_outcome = random.choice(die)
        print("Die number is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        t2.fd(20*die_outcome)

        t3_turn = input("Press Keyword 'Enter' to roll the die")
        die_outcome = random.choice(die)
        print("Die number is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        t3.fd(20*die_outcome)

        t4_turn = input("Press Keyword 'Enter' to roll the die")
        die_outcome = random.choice(die)
        print("Die number is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        t4.fd(20*die_outcome)
input()