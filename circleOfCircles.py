import turtle

shelly = turtle.Turtle()

for i in range(36):
    shelly.penup()
    shelly.forward(100)
    for n in range(6):
        shelly.pendown()
        shelly.circle(5)
        shelly.penup()
        shelly.forward(20)
    shelly.goto(0,0)
    shelly.left(10)
shelly.hideturtle()
turtle.done()