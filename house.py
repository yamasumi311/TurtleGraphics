import turtle

shelly = turtle.Turtle()
turtle.bgcolor('blue')

# make a house
shelly.begin_fill()
shelly.color('gray')
for i in range(4):
    shelly.forward(100)
    shelly.left(90)
shelly.end_fill()
shelly.penup()

# make a triangle roof
shelly.goto(-20,100)
shelly.pendown()
shelly.begin_fill()
shelly.color('red')
for i in range(3):
    shelly.forward(140)
    shelly.left(120)
shelly.end_fill()
shelly.penup()

# make a window
shelly.goto(10,60)
shelly.pendown()
shelly.color('yellow')
shelly.begin_fill()
for i in range(4):
    shelly.forward(20)
    shelly.left(90)
shelly.end_fill()

shelly.hideturtle()
turtle.done()