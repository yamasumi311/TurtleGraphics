import turtle

shelly = turtle.Turtle()
turtle.bgcolor('black')
colors = ['red', 'green', 'blue', 'orange', 'purple', 'yellow']

for i in range(6):
    shelly.penup()
    shelly.goto(0,25*i)
    for n in range(6):
        shelly.color(colors[n])
        shelly.penup()
        shelly.forward(25)
        shelly.pendown()
        for m in range(4):
            shelly.forward(15)
            shelly.left(90)

shelly.hideturtle()
turtle.done()