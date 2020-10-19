# creating class
class Car:
    # attributes
    name = ''
    manufacturer = ''
    color = ''
    production_year = ''
    engine_power = ''

    # Methods
    def start():
        print('Start the engine')

    def brake():
        print('Brake the car')

    def drive():
        print('Drive the car')


# Gaving atribuit of class
Car.name = 'Ford'
Car.manufacturer = 'Ford'
Car.color = 'Black'
Car.production_year = "1997"
Car.engine_power = '1500 cc'

# printing them out
print('Car name:', Car.name)
print('Car manufacturer:', Car.manufacturer)
print('Car color:', Car.color)
print('Car production_year:', Car.production_year)
print('Car engine_power:', Car.engine_power)

# Graving Methods
Car.start()
Car.brake()
Car.drive()
# print(dir(Car))

# creating object (more detailed in making_3_class_objects)
my_car = Car()
my_car.name = 'Tesla'
print('Car name:', my_car.name)

# this will not be work if we don't place "self(preferred by Python)(ex: def start(self))" in our methods.
# the reason is that when we do not pass any argument in methods when we call them from an object
# then object will be pass as "argument" .
# my_car.start()
# my_car.brake()
# my_car.drive()
