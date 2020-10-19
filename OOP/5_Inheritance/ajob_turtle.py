import turtle


class AjobTurtle(turtle.Turtle):
    """Ajobturtle inherits Turtle Calss"""
    pass

    # class AjobTurtle(turtle.Turtle):
    #     """Ajobturtle inherits Turtle Calss"""

    # def forward(self, pixel):
    #     super().backward(pixel)
    #
    # def backward(self, pixel):
    #     super().forward(pixel)
    #
    # def left(self, angle):
    #     super().right(angle)
    #
    # def right(self, angle):
    #     print("I won't turn rite, because Iam ajob")
    # pass

    if __name__ == "__main__":
        montu = AjobTurtle()
        montu.left(30)
        montu.forward(200)
        jhontu = turtle.Turtle()
        jhontu.left(30)
        jhontu.forward(200)
