class Car(object):

    wheels = 4

    # Static Methods
    @staticmethod
    def make_car_sound():
        print 'VRooooommmm!'

    def __init__(self, make, model):
        self.make = make
        self.model = model


mustang = Car('Ford', 'Mustang')
print mustang.wheels
# 4
print Car.wheels
# 4
mustang.make_car_sound()
Car.make_car_sound()
