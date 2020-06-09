import turtle
turtle.shape('turtle')
turtle.speed(1)
for s_l in range(50,100,10):
    for i in range(4):
        turtle.forward(s_l)
        turtle.left(90)
turtle.exitonclick()
