import turtle
import random
colors = ['red', 'green', 'blue', 'yellow', 'orange']
# turtle.penup()
for i in range(50):
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    turtle.setposition(x, y)
    turtle.dot(colors[random.randint(0, len(colors)-1)])
turtle.done()