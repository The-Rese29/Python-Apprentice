
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )

"""

... # Your code here

import turtle
turtle.setup(width=600,height=600)
tina = turtle.Turtle()
tina.shape('turtle')
tina.speed(2)

tina.forward(90)

for i in range(4):
    tina.right(90)
    tina.forward(30)

tina.left(30)
tina.forward(70)
turtle.exitonclick()