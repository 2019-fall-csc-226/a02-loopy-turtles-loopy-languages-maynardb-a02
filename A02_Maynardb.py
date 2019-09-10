#########################################################
# Author: Ben Maynard
# Username: Maynardb
#
# Assignment: A02: Loopy Turtles
# Purpose: To draw a baseball using turtles
#
#########################################################
import turtle

wn = turtle.Screen()
ball = turtle.Turtle()  # create the ball turtle

size = 15 # my pensize variable to keep track of numbers

ball.pensize(size)
ball.penup()

seam = turtle.Turtle()   # create the seam turtle
seam.color("red")        # setting the color of seam
seam.pensize(size)
seam.penup()            # set seam position
seam.setpos(-30, 82)
seam.pendown()
seam.right(90)

for seams in range(35):     # create the first seam
    seam.forward(5)
    seam.right(1)

seam.penup()
seam.home()             # set seam position for the 2nd seam
seam.setpos(30, 82)
seam.pendown()
seam.right(90)
for seams2 in range(36):        # creation of seam2
    seam.forward(5)
    seam.left(1)

ball.home()
ball.setpos(0, 100)             # Draw the ball over top of the seams
ball.pendown()
for circle in range(75):
    ball.forward(10)
    ball.right(5)

wn.exitonclick()
