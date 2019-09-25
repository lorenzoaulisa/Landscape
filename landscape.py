import turtle

def DrawTree(color):
    Bob.right(90)
    Bob.color("brown")
    Bob.begin_fill()
    Bob.forward(80)
    Bob.left(90)
    Bob.forward(10)
    Bob.left(90)
    Bob.forward(80)
    Bob.end_fill()
    Bob.right(180)
    Bob.forward(80)
    Bob.color(color)
    Bob.begin_fill()
    Bob.circle(20)
    Bob.end_fill()
    Bob.right(90)
    Bob.forward(5)
    Bob.begin_fill()
    Bob.circle(20)
    Bob.end_fill()
    Bob.forward(5)
    Bob.right(90)
    Bob.begin_fill()
    Bob.circle(20)
    Bob.end_fill()
    Bob.color("brown")
    Bob.forward(80)
    Bob.right(90)
    return;




turtle.bgcolor("dodger blue")

scn = turtle.Screen()
Aaron = turtle.Turtle()
Bob = turtle.Turtle()
Calvin = turtle.Turtle()
Donald = turtle.Turtle()

Aaron.speed(1000)
Bob.speed(1000)
Calvin.speed(1000)
Donald.speed(1000)

#grass
Aaron.color("forest green")
Aaron.speed(.5)
Aaron.begin_fill()
Aaron.forward(1000)
Aaron.right(90)
Aaron.forward(800)
Aaron.right(90)
Aaron.forward(2000)
Aaron.right(90)
Aaron.forward(800)
Aaron.right(90)
Aaron.forward(1000)
Aaron.end_fill()

#trees
Bob.forward(900)
Bob.left(180)
Bob.forward(40)

for j in range (4):
    for i in range (3): 

        DrawTree("dark green")
        Bob.color("forest green")
        Bob.forward(100)

        DrawTree("yellow green")
        Bob.color("forest green")
        Bob.forward(100)

        DrawTree("green yellow")
        Bob.color("forest green")
        Bob.forward(100)

        DrawTree("sea green")
        Bob.color("forest green")
        Bob.forward(100)

        DrawTree("dark green")
        Bob.color("forest green")
        Bob.forward(100)

        DrawTree("yellow green")
        Bob.color("forest green")
        Bob.forward(100)
    Bob.forward(-1800)
    Bob.left(90)
    Bob.forward(200)
    Bob.right(90)


#sky
Calvin.color("forest green")
Calvin.forward(620)
Calvin.left(90)
Calvin.color("dodger blue")
#cloud1
Calvin.forward(250)
Calvin.color("white")
Calvin.begin_fill()
Calvin.circle(35)
Calvin.end_fill()
Calvin.left(40)
Calvin.forward(40)
Calvin.begin_fill()
Calvin.circle(35)
Calvin.end_fill()
Calvin.left(40)
Calvin.forward(60)
Calvin.begin_fill()
Calvin.circle(35)
Calvin.end_fill()
Calvin.forward(18)
Calvin.begin_fill()
Calvin.circle(35)
Calvin.end_fill()
#cloud2
Calvin.color("dodger blue")
Calvin.left(10)
Calvin.forward(200)
Calvin.right(80)
Calvin.color("white")
Calvin.begin_fill()
Calvin.circle(35)
Calvin.end_fill()
Calvin.left(40)
Calvin.forward(40)
Calvin.begin_fill()
Calvin.circle(35)
Calvin.end_fill()
Calvin.left(40)
Calvin.forward(60)
Calvin.begin_fill()
Calvin.circle(35)
Calvin.end_fill()
Calvin.forward(18)
Calvin.begin_fill()
Calvin.circle(35)
Calvin.end_fill()
#sun
Calvin.color("dodger blue")
Calvin.forward(200)
Calvin.color("gold")
Calvin.begin_fill()
Calvin.circle(60)
Calvin.end_fill()
Calvin.left(30) 

#cloud3
Calvin.color("dodger blue")
Calvin.right(20)
Calvin.forward(150)
Calvin.color("white")
Calvin.begin_fill()
Calvin.circle(25)
Calvin.end_fill()
Calvin.right(15)
Calvin.forward(15)
Calvin.begin_fill()
Calvin.circle(25)
Calvin.end_fill()
Calvin.right(10)
Calvin.forward(15)
Calvin.begin_fill()
Calvin.circle(25)
Calvin.end_fill()
Calvin.forward(15)
Calvin.begin_fill()
Calvin.circle(25)
Calvin.left(5)
Calvin.end_fill()
Calvin.forward(15)
Calvin.begin_fill()
Calvin.circle(25)
Calvin.end_fill()
Calvin.right(10)
Calvin.forward(15)
Calvin.begin_fill()
Calvin.circle(25)
Calvin.end_fill()
#cloud4
Calvin.color("dodger blue")
Calvin.left(20)
Calvin.forward(200)
Calvin.right(80)
Calvin.color("white")
Calvin.begin_fill()
Calvin.circle(35)
Calvin.end_fill()
Calvin.left(40)
Calvin.forward(40)
Calvin.begin_fill()
Calvin.circle(35)
Calvin.end_fill()
Calvin.left(40)
Calvin.forward(60)
Calvin.begin_fill()
Calvin.circle(35)
Calvin.end_fill()
Calvin.forward(18)
Calvin.begin_fill()
Calvin.circle(35)
Calvin.end_fill()

#houses
Donald.right(90)
Donald.color("forest green")
Donald.forward(150)
Donald.right(90)
Donald.forward(50)
Donald.color("peru")
Donald.begin_fill()
Donald.forward(100)
Donald.left(90)
Donald.forward(100)
Donald.left(90)
Donald.forward(100)
Donald.left(90)
Donald.forward(100)
Donald.end_fill()
Donald.color("maroon")
Donald.begin_fill()
Donald.right(120)
Donald.forward(60)
Donald.left(170)
Donald.forward(70)
Donald.left(40)
Donald.forward(100)
Donald.left(40)
Donald.forward(70)
Donald.left(170)
Donald.forward(60)
Donald.right(30)
Donald.forward(100)
Donald.end_fill()
Donald.color("peru")
Donald.right(90)
Donald.forward(100)
Donald.right(90)
Donald.forward(50)
Donald.color("black")
Donald.begin_fill()
Donald.right(90)
Donald.forward(60)
Donald.left(90)
Donald.forward(20)
Donald.left(90)
Donald.forward(60)
Donald.left(90)
Donald.forward(20)
Donald.end_fill()
Donald.color("peru")
Donald.forward(45)
Donald.left(90)
Donald.forward(30)
Donald.color("blue")
Donald.begin_fill()
Donald.forward(30)
Donald.left(90)
Donald.forward(30)
Donald.left(90)
Donald.forward(30)
Donald.left(90)
Donald.forward(30)
Donald.end_fill()



turtle.exitonclick()

