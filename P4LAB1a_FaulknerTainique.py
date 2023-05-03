# CTI-110

# P4LAB1a - Shapes

# Tainique Faulkner

# 5/2/2023

#

import turtle

# Create a turtle object
t = turtle.Turtle()

# Draw a square
for i in range(4):
    t.forward(100)
    t.right(90)

# Move the turtle to a new position
t.penup()
t.goto(-150, 0)
t.pendown()

# Draw a triangle
for i in range(3):
    t.forward(100)
    t.left(120)

# Keep the window open
turtle.mainloop()
