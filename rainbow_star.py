import turtle
import colorsys

# Allow turtle to use RGB values from 0 to 1
turtle.colormode(1)

# Create turtle and screen
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)  # Fastest drawing

# Parameters
n = 36        # Number of distinct hues
h = 0         # Starting hue

# Drawing loop
for i in range(460):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)  # HSV to RGB
    h += 1 / n                          # Step through hues
    t.color(c)
    t.left(145)
    for j in range(5):                 # Draw 5-pointed star
        t.forward(300)
        t.left(150)

turtle.done()  # Keep window open
