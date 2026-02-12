from turtle import *
import random

# setup
Screen().bgpic(r"snowingBG.gif")
setup(1500,1001) # screen size to match background
hideturtle()
speed(0)
pensize(4)
color("white")

# SnowFlake

def diagnolLine(size):
    # make first diagnol line
    forward(size*2) # makes twice the normal length
    backward(size*4) # moves back to make the whole line
    forward(size*2)
    right(45)

def snowFlake(size):
    forward(size)
    backward(size*2)
    forward(size)
    right(45)
    diagnolLine(size)
    # make the small vertical line
    forward(size/2) # makes half of the normal length
    backward(size)
    forward(size/2)
    right(45)
    diagnolLine(size)

i = 0
while i <=50:
    size =  random.randint(5,20)
    # goto to random position
    posX = random.randint(-1500,1500) # go to random position on x
    posY = random.randint(-1001,1001) # go to random position on y
    penup()
    goto(posX,posY)
    pendown()
    snowFlake(size)
    i+=1


# keep the window open
done()