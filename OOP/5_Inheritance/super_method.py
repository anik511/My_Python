class Vehicle:
    """Base class for all vehicles"""

    def __init__(self, name, manufacturer, color):
        print("Creating a vehicle")
        self.name = name
        self.manufacturer = manufacturer
        self.color = color


class Car(Vehicle):
    """This Care class is inheritance class of  Vehicle class"""

    def __init__(self, name, manufacturer, color, year):
        print("Creating a car")
        super().__init__(name, manufacturer, color)
        self.year = year
        self.wheel = 4


if __name__ == "__main__":
    # inheritance
    v3 = Car("Mustang 5.0 GT", "Ford", "Red", 2017)
    print(v3.name, v3.year, v3.wheel)
