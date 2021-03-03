import turtle
import random
import time

def fel():
    positionY = spaceship.ycor()
    positionY += 10
    spaceship.sety(positionY)

def le():
    positionY = spaceship.ycor()
    positionY -= 10
    spaceship.sety(positionY)

def jobb():
    positionX = spaceship.xcor()
    positionX += 10
    spaceship.setx(positionX)

def bal():
    positionX = spaceship.xcor()
    positionX -= 10
    spaceship.setx(positionX)


space = turtle.Screen()
space.setup(width=800, height=600)
space.bgpic("bg.png")
space.addshape("sprite.gif")
space.tracer(0)
space.listen()
space.onkey(fel, "Up")
space.onkey(le, "Down")
space.onkey(bal, "Left")
space.onkey(jobb, "Right")

spaceship = turtle.Turtle()
spaceship.shape("sprite.gif")
spaceship.penup()

while True:

    space.update()
    time.sleep(0.1)

    if spaceship.ycor() > 300:
        spaceship.sety(-300)
    if spaceship.ycor() < -300:
        spaceship.sety(300)
    if spaceship.xcor() > 400:
        spaceship.setx(-400)
    if spaceship.xcor() < -400:
        spaceship.setx(400)

