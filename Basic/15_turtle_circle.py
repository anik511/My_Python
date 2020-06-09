import turtle
turtle.speed(3)
turtle.shape('turtle')
turtle.color('red')
def drow_circle(length):
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)

# l = int(input("Enter Length:"))
count = 0
while count < 90:
    drow_circle(100)
    turtle.right(4)
    count += 1
turtle.exitonclick()