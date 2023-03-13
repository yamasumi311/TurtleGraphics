import turtle

shelly = turtle.Turtle()
turtle.bgcolor('black')
colors = ['white', 'green', 'orange', 'blue', 'yellow', 'red']
for i in range(36):
    shelly.penup()
    shelly.forward(100)
    for n in range(6):
        shelly.pendown()
        # add colors
        shelly.color(colors[n])
        # circles become bigger
        shelly.circle(5+n)
        shelly.penup()
        shelly.forward(20)
    shelly.goto(0,0)
    shelly.left(10)
shelly.hideturtle()
turtle.done()