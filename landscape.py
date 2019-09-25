import turtle

turtle.bgcolor("dodger blue")

scn = turtle.Screen()
Aaron = turtle.Turtle()
Bob = turtle.Turtle()
Calvin = turtle.Turtle()
Donald = turtle.Turtle()

Aaron.speed(.5)
Bob.speed(.5)
Calvin.speed(.5)
Donald.speed(.5)

#grass
Aaron.color("forest green")
Aaron.speed(.5)
Aaron.begin_fill()
Aaron.forward(800)
Aaron.right(90)
Aaron.forward(800)
Aaron.right(90)
Aaron.forward(1600)
Aaron.right(90)
Aaron.forward(800)
Aaron.right(90)
Aaron.forward(800)
Aaron.end_fill()

#trees
Bob.forward(300)
Bob.left(180)
Bob.forward(40)
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
Bob.color("forest green")
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
Bob.color("forest green")
Bob.forward(100)

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
Bob.color("dark green")
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
Bob.color("forest green")
Bob.forward(100)

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
Bob.color("forest green")
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
Bob.color("forest green")
Bob.forward(100)

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
Bob.color("yellow green")
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
Bob.color("forest green")
Bob.forward(100)

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
Bob.color("green yellow")
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
Bob.color("forest green")
Bob.forward(100)

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
Bob.color("sea green")
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
Bob.color("forest green")
Bob.forward(100)

#sky
Calvin.color("forest green")
Calvin.forward(320)
Calvin.left(90)
Calvin.color("dodger blue")
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
Calvin.color("dodger blue")
Calvin.forward(200)
Calvin.color("gold")
Calvin.begin_fill()
Calvin.circle(60)
Calvin.end_fill()
Calvin.left(30)
Calvin.color("dodger blue")
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

#houses
Donald.right(90)
Donald.color("forest green")
Donald.forward(100)
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
turtle.exitonclick()

