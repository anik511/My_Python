from inheritance_1 import Vehicle


class Truck(Vehicle):
    def __init__(self, name, manufacturer, color, year):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = year
        print("A new Truck has been created. Name:", self.name)

    def info(self):
        print(self.name, " Manufacturer name:", self.manufacturer + "\n" + "Color", self.color + "\n"
              + "Production year", self.year)
        """To use parent classmethod in child class method we must call super() first"""
        super().drive()

    # method overriding
    def turn(self, direction):
        print("Turning", self.name, "to", direction)


t1 = Truck("Cyber-Truck", "Tesla", "Silver", 2019)
t1.info()
t1.turn("Right")
t1.brake()
