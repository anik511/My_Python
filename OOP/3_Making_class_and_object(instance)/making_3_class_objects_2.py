# Advance
# Please check it after checking making_4_class_objects
import making_4_class_objects as m4o
# Or please check this file from here
import making_3_class_objects as mco

# creating object
my_car = mco.Car()

# Graving attribute of class
my_car.name = 'Audi'
my_car.manufacturer = 'Audi'
my_car.color = 'Black'
my_car.production_year = "2017"
my_car.engine_power = '1700 cc'

# printing them out
print('Car name:', my_car.name)
print('Car manufacturer:', my_car.manufacturer)
print('Car color:', my_car.color)
print('Car production_year:', my_car.production_year)
print('Car engine_power:', my_car.engine_power)
# Graving methods of class
my_car.start()
my_car.brake()
my_car.drive()

# Advance
# Please check it after checking making_4_class_objects
print("\n\nAfter checking making_4_class_objects\n")
c = "Bugati"
w = "White"
instance_object = m4o.Car(c, w)
print('instance_object Car name:', instance_object.name)
print('instance_object Car color:', instance_object.color)
instance_object.start()
instance_object.production_year = "2020"
print('instance_object Car production year:', instance_object.production_year)
