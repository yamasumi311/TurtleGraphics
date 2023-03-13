# make a geometric rainbow pattern
import turtle
shelly = turtle.Turtle()
# pick order of colors for the hexagon
colors = ['red', 'yellow', 'blue', 'orange', 'green', 'red']
# turn background black
turtle.bgcolor('black')
# make 36 hexagons, each 10 degrees apart
for n in range(36):
    # repeat 6 times - move forward and turn
    for i in range(6):
        shelly.color(colors[i])
        shelly.forward(100)
        shelly.left(60)
    # add a turn
    shelly.left(10)
# get ready to draw 36 circles
shelly.penup()
shelly.color('white')
# repeat 36 times to match the 36 hexagons
for i in range(36):
    shelly.forward(220)
    shelly.pendown()
    shelly.circle(5)
    shelly.penup()
    shelly.backward(220)
    shelly.right(10)
# hide turtle to finish the drowing
shelly.hideturtle()
turtle.done()