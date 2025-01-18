import turtle

# Create turtle object
flower = turtle.Turtle()
flower.color("purple")
flower.speed(10)

# Draw a flower pattern
for _ in range(36):
    flower.forward(100)
    flower.left(45)
    flower.forward(100)
    flower.left(135)
    flower.forward(100)
    flower.left(45)
    flower.forward(100)
    flower.left(10)

turtle.done()
