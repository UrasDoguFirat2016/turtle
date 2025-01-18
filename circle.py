import turtle

screen = turtle.Screen()
screen.bgcolor("black")

x = turtle.Turtle()
x.shape("turtle")
x.color("white")
x.speed(100000)

for _ in range(100000000000000000):
    x.forward(500)
    x.left(90)
    x.forward(100)
    x.left(90)
    x.forward(500)
    x.left(90)
    x.forward(100)
    x.left(90)
    x.left(1)

x.hideturtle()
turtle.done()