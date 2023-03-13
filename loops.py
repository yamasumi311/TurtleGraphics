import turtle

shelly = turtle.Turtle()

# set color before the shape is drawn
shelly.begin_fill()
shelly.color('red')
for n in range(6):
    shelly.left(60)
    for i in range(4): #start counting at 1, stop before 10, and go up in steps of 2 =>
        shelly.forward(100)
        shelly.left(90)
        print(i)

# and then end with end_fill function
shelly.end_fill()

turtle.done()

