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

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = spaceship.xcor()-5
        y = spaceship.ycor()
        bullet.setposition(x,y)
        bullet.showturtle()

#Bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 70

bulletstate = "ready"

space = turtle.Screen()
space.title("StarWars")
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
space.onkey(fire_bullet, "space")

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
pen.write("Találatok: 0",align="center",font=("Ariel",18,"bold"))
#Találatok száma
score_a=0
#Meteor találatok száma
pen.goto(-300,260)
pen.write("Meteorok: 0",align="center",font=("Arial",18,"bold"))
meteortalalatok=0
#élet
szamlalo = 3
#kijelző
kijelzo = turtle.Turtle()
kijelzo.hideturtle()

#Leaderboard
leaderboard = turtle.Turtle()
leaderboard.penup()
leaderboard.hideturtle()

leaderboardMembers = []

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
    #Lövedékérzékelés
    if meteor.distance(bullet.xcor(), bullet.ycor()) < 50:
        meteor.shape(random.choice(shapes))
        meteor.setx(400)
        meteor.sety(random.randint(-270,270))
        meteortalalatok+=1
        pen.goto(0,260)
        pen.clear()
        pen.write("Találatok: {}".format(score_a),align="center",font=("Arial",18,"bold"))
        pen.goto(-300,260)
        pen.write("Meteorok: {}".format(meteortalalatok),align="center",font=("Arial",18,"bold"))
        bullet.setx(500)
        bulletstate="ready"
    if spaceship.distance(meteor.xcor(), meteor.ycor()) < 70:
        meteor.shape(random.choice(shapes))
        meteor.setx(400)
        meteor.sety(random.randint(-270,270))
        score_a+=1
        pen.clear()
        pen.goto(0,260)
        pen.write("Találatok: {}".format(score_a),align="center",font=("Arial",18,"bold"))
        pen.goto(-300,260)
        pen.write("Meteorok: {}".format(meteortalalatok),align="center",font=("Arial",18,"bold"))
        szamlalo -= 1   
    if meteor.shape() == "meteor2.gif":
        meteor.setx(meteor.xcor()-15)
    elif meteor.shape() == "meteora1.gif":
        meteor.setx(meteor.xcor()-15)
        meteor.sety(meteor.ycor()-15)
    else:
        meteor.setx(meteor.xcor()-15)
        meteor.sety(meteor.ycor()+15)

    if bulletstate == "fire":
        x = bullet.xcor()
        x +=bulletspeed
        bullet.setx(x)
    if bullet.xcor() > 390:
        bullet.hideturtle()
        bulletstate = "ready"

	# 3 meteor találat és game over
    if szamlalo == 0:
        space.clear()                                                                
        kijelzo.write("Game Over!", align="center", font=("Arial", 36, "bold"))
        time.sleep(1)
        user = turtle.textinput("Leaderboard details", "Name:")
        file = open ("leaderboard.txt", "a")
        file.write("\n")
        file.write(user)
        file.write(";")
        file.write(str(meteortalalatok))
        file.close()
        kijelzo.clear()
        leaderboard.write("LEADERBOARD\n",align="center",font=("Arial",20,"bold"))
        with open("leaderboard.txt") as fp:
            for line in fp:
                piece1 = line.split(';')[0]
                piece2 = line.split(';')[1]
                leaderboardMembers.append((str(piece1),int(piece2)))
        leaderboardMembers.sort(key=lambda a: a[1], reverse=True)
        count = 0
        for member in leaderboardMembers:
            if count < 3:
                leaderboard.write("{}\t{}".format(member[0],member[1]),align="center",font=("Arial",20,"bold"))
                leaderboard.goto(leaderboard.xcor(), leaderboard.ycor()-30)
            else: 
                break
            count += 1
        time.sleep(10)
