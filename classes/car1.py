class Car(object):

    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    @staticmethod
    def test(x):
        return x == 0

mustang = Car('Ford', 'Mustang')
print mustang.wheels
# 4
print Car.wheels
# доступ к статическому методу можно получать и через класс
print Car.test(1)
# False
f = Car()
print f.test(0)    # и через экземпляр класса
# True
