import turtle

shelly = turtle.Turtle()
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'lime']
for n in range(6):
    shelly.penup()
    shelly.forward(30)
    shelly.pendown()
    shelly.color(colors[n])
    for i in range(4):
        shelly.forward(20)
        shelly.left(90)
shelly.hideturtle()
turtle.done()

