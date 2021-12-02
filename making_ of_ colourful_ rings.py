import turtle
colors=['orange','black','grey','white','blue']
screen=turtle.Screen()
trtl=turtle.Turtle()
trtl.speed(0)
screen.bgcolor("pink")
for x in range (120):
    trtl.pencolor(colors[x%6])
    trtl.width(x/5+1)
    trtl.forward(x)
    trtl.left(20)
