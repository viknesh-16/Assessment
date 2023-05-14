import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Pattern")

# Create a turtle object
t = turtle.Turtle()
t.speed(0)
t.color("red")

# Draw the pattern
for i in range(36):
    for j in range(4):
        t.forward(100)
        t.right(90)
    t.right(10)

# Close the turtle window when clicked
turtle.exitonclick()
