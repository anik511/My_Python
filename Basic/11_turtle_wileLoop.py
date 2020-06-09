import turtle
turtle.color('blue')
turtle.speed(6)
count=0
while count<36:
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.right(10)
    count+=1
turtle.exitonclick()
