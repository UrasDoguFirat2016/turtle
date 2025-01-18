import turtle

screen = turtle.Screen()
screen.bgcolor("darkgreen")

x = turtle.Turtle()
x.color("white")
x.shape("turtle")
x.speed(20)

for _ in range(10):
    x.forward(100)
    x.left(45)
    x.forward(100)
    x.left(45)
    x.forward(100)
    x.left(45)
    x.forward(100)
    x.left(45)
    x.forward(100)
    x.left(45)
    x.forward(100)
    x.left(45)
    x.forward(100)
    x.left(45)
    x.forward(100)
    x.right(20)

for _ in range(10):
    x.left(45)
    x.forward(100)
    x.right(90)
    x.forward(100)
    x.right(90)
    x.forward(100)
    x.right(90)
    x.forward(100)
    x.right(20)

x.hideturtle()
turtle.done()