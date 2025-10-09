import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")  # Set background color

# Create a turtle object
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.speed(1)
t.circle(6)

# Draw a square
for _ in range(8):
    t.forward(100)  # Move the turtle forward by 100 units
    t.left(45)  # Turn the turtle 90 degrees to the left
    t.circle(4)
# Hide the turtle after drawing
t.hideturtle()

# Keep the window open until clicked
screen.exitonclick()
