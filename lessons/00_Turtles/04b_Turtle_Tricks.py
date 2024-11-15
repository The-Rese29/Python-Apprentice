"""
For this program, you will tell Tina the Turtle to draw 
a pentagon.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a pentagon
# Make each side of the pentagon a different color with 
# tina.pencolor()


... # Your code here
tina.penup()
tina.pencolor('blue')
tina.pensize(3)
tina.goto (50,150)
tina.pendown()
tina.forward(50)
tina.right(72)
tina.forward(50)
tina.right(72)
tina.forward(50)
tina.right(72)
tina.forward(50)
tina.right(72)
tina.forward(50)
tina.penup()
tina.pencolor('black')
tina.goto(-100,100)
tina.right(72)
tina.pendown()
tina.forward(30)
tina.left(90)
tina.forward(180)
tina.left(90)
tina.forward(60)
tina.left(90)
tina.forward(40)
tina.right(90)
tina.forward(2)
tina.circle(15)
tina.penup()
tina.goto(-130,210)
tina.left(90)
tina.pendown()
tina.forward(55)
tina.left(45)
tina.forward(30)
tina.penup()
tina.goto(-130,155)
tina.right(90)
tina.pendown()
tina.forward(30)
tina.penup()
tina.goto(-130,190)
tina.right(90)
tina.pendown()
tina.forward(30)
tina.goto(-130,190)
tina.left(270)
tina.forward(30)
tina.penup()
tina.goto(-170,15)
tina.right(45)
tina.pendown()
tina.forward(40)
tina.penup()
tina.forward(20)
tina.pendown()
tina.forward(40)
tina.penup()
tina.forward(20)
tina.pendown()
tina.forward(40)
tina.penup()
tina.goto(-160,30)
tina.pendown()
tina.pencolor('blue')
tina.circle(20,-180)
tina.penup()
tina.goto(-100,30)
tina.right(180)
tina.pendown()
tina.circle(15,-220)
tina.right(-150)
tina.forward(50)
tina.penup()
tina.goto(-40,30)
tina.left(160)
tina.pendown()
tina.forward(60)
tina.penup()
tina.goto(-60,70)
tina.right(90)
tina.pendown()
tina.forward(40)




turtle.exitonclick()                    # Close the window when we click on it
