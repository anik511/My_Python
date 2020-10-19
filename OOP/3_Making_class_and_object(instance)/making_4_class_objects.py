# we can also declare the character of an object
class Car:
    # we do not make any normal attribute here
    # this __init__ method is a constructor
    def __init__(self, name, color):
        # Instance attributes
        self.name = name
        self.color = color
        # Here "self.name & self.color" this are instance attribute of "my_car" object
        # Now for this type of attribute(instance) we can not use class.attribute(ex: print(Car.name))
        # this will cause "AttributeError"

    def start(self):
        print(self)
        print('Starting the engine')
        print('Car name:', self.name)
        print('Car color:', self.color)


if __name__ == "__main__":
    my_car = Car('Ferary', 'Red')
    # print('Car name:', my_car.name)
    # print('Car color:', my_car.color)
    my_car.start()
    potpie_car = Car('Lebergini', 'Blue')
    potpie_car.start()
    tuna_car = Car('Toyota', 'indigo')
    tuna_car.start()
