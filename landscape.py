import turtle

turtle.bgcolor("blue")

scn = turtle.Screen()
Aaron = turtle.Turtle()
Bob = turtle.Turtle()
Calvin = turtle.Turtle()

#grass
Aaron.color("green")
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

turtle.exitonclick()

