def add(*args):
   return sum(args)

def calculate(**kwargs):
    print(kwargs)

print(add(1, 2, 3, 4))
calculate(add=1, mult=2)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan", model="GT-R")