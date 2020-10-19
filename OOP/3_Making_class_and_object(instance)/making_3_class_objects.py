# creating class
class Car:
    # Class attributes
    name = ''
    manufacturer = ''
    color = ''
    production_year = ''
    engine_power = ''

    # Methods
    # self(preferred by Python)(ex: def start(self))
    # more detailed in line 42
    def start(self):
        print('Start the engine')

    def brake(self):
        print('Brake the car')

    # or any thing(ex: def start(any_thing))

    def drive(pot):
        print('Drive the car')


# for thise if statement after importing this file or class nothing will be print from below
if __name__ == '__main__':
    # creating object
    my_car = Car()
    # Graving attribute of class
    my_car.name = 'Tesla'
    my_car.manufacturer = 'Tesla'
    my_car.color = 'Black'
    my_car.production_year = "2017"
    my_car.engine_power = '1500 cc'

    # printing them out
    print('Car name:', my_car.name)
    print('Car manufacturer:', my_car.manufacturer)
    print('Car color:', my_car.color)
    print('Car production_year:', my_car.production_year)
    print('Car engine_power:', my_car.engine_power)

    # thise will not be work if we don't place "self(preferred by Python)(ex: def start(self))"
    # "or any thing(ex: def start(any_thing))" in our methods.
    # the reason is that when we do not pass any argument in methods when we call them from an object
    # then object will be pass as "argument" .
    my_car.start()
    my_car.brake()
    my_car.drive()
