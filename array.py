import turtle

shelly = turtle.Turtle()

colors = ['red', 'green', 'blue']
for i in range(3):
    shelly.color(colors[i])
    shelly.forward(50)
    print(colors[i])

turtle.done()