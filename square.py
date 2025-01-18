import turtle

screen = turtle.Screen()
screen.bgcolor("aqua")

x = turtle.Turtle()
x.shape("turtle")
x.color("green")
x.speed(2)

for _ in range(4):
    x.forward(100)
    x.left(90)

x.hideturtle()
turtle.done()