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

    def __init__(self, name, manufacturer, color, year):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = 2017
        self.wheel = 4
        print("A new Car Has been Created. Name:", self.name)
        print("It has", self.wheel, "wheel.")

    def chang_gear(self, gear_name):
        print(self.name, "is changing gear to", gear_name)

    def turn(self, direction):
        print(self.name, "is turning", direction)


if __name__ == "__main__":
    v1 = Vehicle("Fusion 110 EX", "Walton", "Black")
    # v1.drive()
    v1.turn("Right")
    # v1.brake()

    # inheritance
    v3 = Car("Mustang 5.0 GT", "Ford", "Red", 1999)
    # v3.drive()
    v3.turn("Left")
    # v3.brake()
    # v3.chang_gear("p")
