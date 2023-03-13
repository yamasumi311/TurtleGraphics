import turtle

shelly = turtle.Turtle()

# face
shelly.begin_fill()
shelly.color('green')
shelly.circle(100)
shelly.end_fill()

# left eyes
shelly.goto(-30,100)
shelly.begin_fill()
shelly.color('white')
shelly.circle(30)
shelly.end_fill()
shelly.begin_fill()
shelly.color('black')
shelly.circle(20)
shelly.end_fill()
shelly.penup()

# right eyes
shelly.goto(30,100)
shelly.pendown()
shelly.begin_fill()
shelly.color('white')
shelly.circle(30)
shelly.end_fill()
shelly.begin_fill()
shelly.color('black')
shelly.circle(20)
shelly.end_fill()
shelly.penup()

# mouth
shelly.goto(0,30)
shelly.pendown()
shelly.begin_fill()
shelly.color('red')
shelly.circle(30)
shelly.end_fill()

shelly.hideturtle()
turtle.done()