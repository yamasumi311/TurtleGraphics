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
turtle.done()