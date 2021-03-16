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
space.addshape("meteora1.gif")
space.addshape("meteora2.gif")
space.tracer(0)
space.listen()
space.onkeypress(fel, "Up")
space.onkeypress(le, "Down")
space.onkeypress(bal, "Left")
space.onkeypress(jobb, "Right")

spaceship = turtle.Turtle()
spaceship.shape("sprite.gif")
spaceship.penup()

meteor = turtle.Turtle()
meteor.penup()
shapes = ["meteor2.gif","meteora1.gif","meteora2.gif"]
meteor.shape(random.choice(shapes))
meteor.setx(400)
meteor.sety(random.randint(-270,270))


#Számláló
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Találatok: 0",align="center",font=("Courier",18,"bold"))
#Találatok száma
score_a=0

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

    if meteor.xcor() < -400 or meteor.ycor() < -300 or meteor.ycor() > 300:
        meteor.shape(random.choice(shapes))
        meteor.setx(400)
        meteor.sety(random.randint(-270,270))
    if spaceship.distance(meteor.xcor(), meteor.ycor()) < 70:
        meteor.shape(random.choice(shapes))
        meteor.setx(400)
        meteor.sety(random.randint(-270,270))
        score_a+=1
        pen.clear()
        pen.write("Találatok: {}".format(score_a),align="center",font=("Courier",18,"bold"))

    if meteor.shape() == "meteor2.gif":
        meteor.setx(meteor.xcor()-15)
    elif meteor.shape() == "meteora1.gif":
        meteor.setx(meteor.xcor()-15)
        meteor.sety(meteor.ycor()-15)
    else:
        meteor.setx(meteor.xcor()-15)
        meteor.sety(meteor.ycor()+15)