import turtle
turtle.speed(3)
turtle.shape('turtle')
turtle.color('red')
def drow_triangle(length):
    for i in range(3):
        turtle.forward(length)
        turtle.left(120)
    turtle.exitonclick()
l = int(input("Enter Length:"))
drow_triangle(l)
