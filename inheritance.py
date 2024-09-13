class Car:
    color = "Black"
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1= ToyotaCar("Fortuner")
car2= ToyotaCar("Legender")

print(car1.color)