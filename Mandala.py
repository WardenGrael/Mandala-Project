from tkinter.ttk import Style
import turtle
turtle.bgcolor("black")

base = turtle.Turtle()
base.speed(0)
base.color("white")
base.pensize(5)

for i in range(8):
    base.left(45)
    for i in range(1):
        base.forward(150)
        base.left(90) 
        base.forward(80) 
        base.left(90) 
        base.forward(150) 
        base.left(90) 
        base.forward(80) 
        base.left(90) 

for i in range(8):
    base.left(45)
    for i in range(8):
        base.forward(100)
        base.left(45)

for i in range(8):
    base.circle(100)
    base.left(45)

circle = turtle.Turtle()
circle.hideturtle()
circle.color("white")
circle.pensize(5)
circle.penup()
circle.goto(0, -260.0)
circle.pendown()
circle.circle(263)
circle.penup()
circle.goto(0,-240)
circle.pendown()
circle.circle(240)
circle.penup()
circle.goto(0,-200)
circle.pendown()
circle.circle(199)

def buttonclick(x,y):
    print("You clicked at this coordinate({0},{1})".format(x,y))
 
 #onscreen function to send coordinate
turtle.onscreenclick(buttonclick,1)
turtle.listen()  # listen to incoming connections
turtle.speed(10) # set the speed
turtle.done()    # hold the screen