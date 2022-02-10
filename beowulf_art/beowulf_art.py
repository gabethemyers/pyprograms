
import turtle

#setup screen
WIDTH, HEIGHT = (950, 560)
screen = turtle.Screen()
screen.colormode(255)
turtle.bgcolor(0, 191, 255)
screen.setup(WIDTH, HEIGHT)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)


tu = turtle.Turtle()

def triangle(side):
    tu.begin_fill()
    tu.rt(90)
    tu.fd(side/2)
    tu.lt(120)
    tu.fd(side)
    tu.lt(120)
    tu.fd(side)
    tu.lt(120)
    tu.fd(side/2)
    tu.lt(90)
    tu.end_fill()

#ground
tu.pen(pencolor='black', fillcolor=(86, 125, 70), pensize=2, speed=5)
tu.begin_fill()
tu.penup()
tu.right(180)
tu.fd(10)
tu.lt(90)
tu.fd(10)
tu.lt(90)
tu.pendown()
tu.fd(960)
tu.lt(90)
tu.fd(200)
tu.lt(90)
tu.fd(960)

tu.lt(90)
tu.fd(200)
tu.end_fill()

#mountains

tu.fillcolor('grey')
tu.begin_fill()
tu.penup()
tu.goto(100,190)
tu.pendown()
tu.lt(150)
tu.fd(400)
tu.rt(120)
tu.fd(175)
tu.lt(120)
tu.fd(175)
tu.rt(120)
tu.fd(400)
tu.rt(120)
tu.fd(575)
tu.end_fill()

#snow cap 1
tu.penup()
tu.goto(100,190)
tu.seth(60)
tu.fd(300)
tu.seth(0)
tu.pen(pencolor='black', fillcolor='white')
tu.begin_fill()
tu.pendown()
tu.fd(100)
tu.seth(135)
tu.goto(300, 536)
tu.seth(225)
tu.goto(250, 450)
tu.end_fill()

#snow cap 2
tu.penup()
tu.goto(387, 384)
tu.seth(60)
tu.fd(75)
tu.seth(0)
tu.pendown()
tu.begin_fill()
tu.fd(100)
tu.seth(120)
tu.fd(100)
tu.lt(120)
tu.fd(100)
tu.end_fill()

#sun
tu.pen(speed=10)
tu.penup()
tu.seth(90)
tu.goto(850, 450)
tu.pen(pencolor='yellow', fillcolor='orange',pensize=3)
tu.pendown()
tu.begin_fill()
tu.circle(50)
tu.end_fill()
tu.pensize(2)
tu.fillcolor('yellow')
tu.penup()
tu.goto(800, 450)
for x in range(12):
    tu.penup()
    tu.fd(49)
    tu.pendown()
    triangle(25)
    tu.penup()
    tu.goto(800, 450)
    tu.rt(30)

tu.pen(speed=5)
#herot hall
tu.penup()
tu.pen(pencolor='black', pensize=2)
tu.fillcolor(255,215,0)
tu.begin_fill()
xvar, yvar = 300, 40
avar, bvar = 225, 400
tu.goto(xvar, yvar)
tu.pendown()
tu.seth(90)
tu.fd(avar)
tu.rt(60)
tu.fd(231)
tu.rt(60)
tu.fd(231)
tu.seth(270)
tu.fd(avar)
tu.rt(90)
tu.fd(bvar)
tu.end_fill()
tu.penup()

#herot hall beams

tu.seth(90)
tu.fd(225)
tu.rt(90)
tu.pen(pencolor=('black'), fillcolor=(150, 75, 0))
tu.pendown()
tu.begin_fill()
tu.fd(190)
tu.lt(90)
tu.fd(110)
tu.rt(60)
tu.fd(12)
tu.rt(60)
tu.fd(12.2)
tu.rt(60)
tu.fd(109)
tu.lt(90)
tu.fd(190)
tu.rt(90)
tu.fd(20)
tu.rt(90)
tu.fd(400)
tu.rt(90)
tu.fd(20)
tu.end_fill()

# herot doors
tu.penup()
tu.goto(500, 40)
tu.seth(90)
tu.pen(pencolor='black', fillcolor=(150, 75, 0))
tu.pendown()
tu.begin_fill()
tu.fd(100)
tu.rt(90)
tu.fd(50)
tu.rt(90)
tu.fd(100)
tu.rt(90)
tu.fd(50)
tu.end_fill()
tu.begin_fill()
tu.fd(50)
tu.rt(90)
tu.fd(100)
tu.rt(90)
tu.fd(50)
tu.rt(90)
tu.fd(100)
tu.end_fill()
tu.seth(90)
tu.penup()
tu.fd(50)
tu.rt(90)
tu.fd(10)
tu.fillcolor(255,215,0)
tu.pendown()
tu.begin_fill()
tu.circle(3)
tu.end_fill()
tu.penup()
tu.back(20)
tu.pendown()
tu.begin_fill()
tu.circle(3)
tu.end_fill()

#tree
tu.penup()
tu.goto(70, 80)
tu.seth(90)
tu.pen(pencolor='black', fillcolor=(150,75,0))
tu.begin_fill()
tu.pendown()
tu.fd(200)
tu.rt(90)
tu.fd(30)
tu.rt(90)
tu.fd(200)
tu.rt(90)
tu.fd(30)
tu.end_fill()
tu.penup()
tu.seth(90)
tu.fd(50)
tu.seth(180)
tu.fillcolor(38, 69, 62)
tu.begin_fill()
tu.pendown()
tu.fd(70)
tu.seth(50)
tu.fd(75)
tu.seth(180)
tu.fd(45)
tu.seth(50)
tu.fd(75)
tu.seth(180)
tu.fd(45)
tu.seth(50)
tu.fd(120)
tu.rt(100)
tu.fd(120)
tu.seth(180)
tu.fd(45)
tu.seth(310)
tu.fd(75)
tu.seth(180)
tu.fd(45)
tu.seth(310)
tu.fd(75)
tu.seth(180)
tu.fd(68)
tu.end_fill()
tu.penup()


tu.goto(948, -10)
tu.write('By: Gabe Myers', True, align='right')
tu.home()

turtle.done()

