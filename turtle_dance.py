import turtle

screen = turtle.Screen()
screen.bgcolor("black")

x = turtle.Turtle()
x.shape("turtle")
x.color("white")
x.speed(2)

for _ in range(100000000000000000000):
    x.circle(1)


x.hideturtle()
turtle.done()