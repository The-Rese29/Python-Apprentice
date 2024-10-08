"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()  
                # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a triangle
# Make each side of the triangle a different color with 
# tina.pencolor()

tina.shape('turtle')
tina.speed(2)

tina.pencolor('blue')
tina.pendown()
tina.forward(90)

tina.left(120)
tina.forward(90)
tina.left(120)
tina.forward(90)
tina.penup()
tina.right(120)
tina.forward(90)
tina.left(60)
tina.pendown()
tina.forward(50)
tina.right(90)
tina.forward(200)
tina.left(90)
tina.forward(50)
tina.left(90)
tina.forward(200)

turtle.exitonclick()
