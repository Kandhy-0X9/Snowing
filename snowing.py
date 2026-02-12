from turtle import *
import random

# setup
Screen().bgpic(r"snowingBG.gif")
setup(1500,1001) # screen size to match background
hideturtle()
speed(0)
pensize(4)
color("white")

# SnowFlake functions
def diagnolLine(size):
    # make first diagnol line
    forward(size*2) # makes twice the normal length
    backward(size*4) # moves back to make the whole line
    forward(size*2)
    right(45)

def snowFlake(size):
    forward(size)
    backward(size*2) # moves back to make the whole line
    forward(size)
    right(45)
    diagnolLine(size) # make the first diagnol line
    # make the small vertical line
    forward(size/2) # makes half of the normal length
    backward(size) # moves back to make the whole line
    forward(size/2)
    right(45)
    diagnolLine(size) # make the second diagnol line

def snowPosition():
    posX = window_width() // 2 # get the width of the window and divide by 2 to get the range for x coordinates
    posY = window_height() // 2 # get the height of the window and divide by 2 to get the range for y coordinates
    penup()
    goto(random.randint(-posX, posX), random.randint(-posY, posY)) # randomly position the turtle within the window
    pendown() 

# draw 50 snowflakes
for i in range(50):
    # randomly position the turtle and draw a snowflake
    snowPosition()
    setheading(0) # resets turtle's direction to the right
    size = random.randint(5, 15) # random size for snowflakes
    snowFlake(size)

# keep the window open
done()