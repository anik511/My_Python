class Vehicle:
    """Base class for all vehicles"""

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def drive(self):
        print("Driving", self.manufacturer, self.name)

    def turn(self, direction):
        print("Turning", self.name, "to", direction)

    def brake(self):
        print(self.name, "is stopping")


class Car(Vehicle):
    """This Care class is inheritance class of  Vehicle class"""

    def chang_gear(self, gear_name):
        print(self.name, "is changing gear to", gear_name)


if __name__ == "__main__":
    v1 = Vehicle("Fusion 110 EX", "Walton", "Black")
    v2 = Vehicle("Softail Delux", "Harly-Davidson", "Blue")
    v1.drive()
    v2.drive()
    v1.turn("Right")
    v1.brake()
    v2.brake()

    # inheritance
    v3 = Car("Mustang 5.0 GT", "Ford", "Red")
    v3.drive()
    v3.turn("Left")
    v3.brake()
    v3.chang_gear("p")
