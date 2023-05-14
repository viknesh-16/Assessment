import turtle
import random

# Create turtle object
t = turtle.Turtle()

# Set window size and background color
turtle.setup(400, 400)
turtle.bgcolor("black")

# Define function to draw a random shape in a random position
def draw_shape():
    # Set pen color and fill color
    pen_color = random.choice(["red", "blue", "green", "purple"])
    fill_color = random.choice(["yellow","cyan", "magenta", "brown"])
    t.pencolor(pen_color)
    t.fillcolor(fill_color)

    # Generate random position and size for the shape
    x = random.randint(-150, 150)
    y = random.randint(-150, 150)
    size = random.randint(10, 50)

    # Draw the shape at the random position
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(size)
    t.end_fill()

# Call the function to draw a shape in a random position
draw_shape()

# Keep the turtle window open until it is manually closed
turtle.done()
