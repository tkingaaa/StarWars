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
space.addshape("meteor2.gif")
space.tracer(0)
space.listen()
space.onkeypress(fel, "Up")
space.onkeypress(le, "Down")
space.onkeypress(bal, "Left")
space.onkeypress(jobb, "Right")

spaceship = turtle.Turtle()
spaceship.shape("sprite.gif")
spaceship.penup()

meteor2 = turtle.Turtle()
meteor2.shape("meteor2.gif")
meteor2.penup();
meteor2.setx(450)
meteor2.sety(random.randint(-300,300))

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

    meteor2.setx(meteor2.xcor()-10)
    if meteor2.xcor() < -400:
        meteor2.setx(450)
        meteor2.sety(random.randint(-300,300))
