import turtle

shelly = turtle.Turtle()
shelly.shape("turtle") #makes shelly in realistic turtle shape!
shelly.forward(100) #moves shelly forward 100 steps
shelly.right(90) #turns shelly right 90 degrees
shelly.left(60) #turns shelly left 60 degrees
shelly.penup() #makes shelly lift pen
shelly.backward(100) #moves shelly backward 100 steps
shelly.pendown() #makes shelly put the pen down to draw
shelly.color("red") #makes shelly draw in color red
shelly.circle(10) #makes shelly draw a circle of size 10
shelly.reset() #clears screen and goes back to start position
shelly.goto(35,80) #moves to x coordinate 35, y coordinate 80
shelly.hideturtle() #makes shelly not visible on the screen
print(shelly.xcor(), shelly.ycor()) #print out current coordinates
turtle.screensize()


turtle.done()



