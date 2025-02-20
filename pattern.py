import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a list of turtle names
turtle_names = ["Leo", "Mikey", "Donnie", "Raph", "April"]

# Create a list to hold the turtle objects
turtles = []

# Initialize turtles with different colors
colors = ["red", "blue", "green", "orange", "purple"]

for i in range(len(turtle_names)):
    t = turtle.Turtle()
    t.name = turtle_names[i]
    t.color(colors[i])
    t.speed(3)
    turtles.append(t)

# Function to draw a star
def draw_star(turtle, size):
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
        
# Position turtles and draw stars
for i, t in enumerate(turtles):
    t.penup()
    t.goto(-200 + i * 100, 0)
    t.pendown()
    draw_star(t, 100)

# Hide turtles and display the result
for t in turtles:
    t.hideturtle()

# Keep the window open until clicked
screen.exitonclick()
