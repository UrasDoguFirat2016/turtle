import turtle

# Create turtle object
heart = turtle.Turtle()
heart.color("red")
heart.begin_fill()
heart.speed(5)

# Draw the heart shape
heart.left(50)
heart.forward(133)
heart.circle(50, 200)  # Draw the first arc of the heart
heart.right(140)
heart.circle(50, 200)  # Draw the second arc of the heart
heart.forward(133)

# Fill the heart color
heart.end_fill()

# Hide the turtle and display the drawing
heart.hideturtle()
turtle.done()