"""
For this program, you will tell Tina the Turtle to draw 
multiple shapes.

Draw two circles, filled with different colors, 
and in different places on the screen. 

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.

"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.circle() to draw a circle, and tina.goto() to move tina to a new location
# Use tina.begin_fill(), tina.end_fill(), and tina.fillcolor() to fill in the shapes


... # Your code here
#tina.circle(50)
#tina.penup()
#tina.goto(200,200)
#tina.pendown()
#tina.circle(50)
#tina.begin_fill()
#tina.end_fill()
#tina.fillcolor()
tina.shape('turtle')
tina.penup()
tina.goto(0,160)
tina.pendown()

def make_polygon(side_length, number_of_sides):
    angle = (number_of_sides - 2)*(180/number_of_sides)
    for i in range(number_of_sides):
        tina.right(180-angle)
        tina.forward(side_length)

make_polygon(1,1000)

turtle.exitonclick()                    # Close the window when we click on it


# Dont forget to check in your code!