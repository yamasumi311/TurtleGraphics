import turtle

shelly = turtle.Turtle()

turtle.bgcolor('black')
shelly.color('yellow')
for i in range(100):
    shelly.forward(i*2)
    shelly.left(90)
shelly.hideturtle()
turtle.done()