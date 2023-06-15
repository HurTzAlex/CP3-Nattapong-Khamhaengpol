class Vehicle:
    license = ""
    SerialCode = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air Condition")

class PickUp(Vehicle):
    pass

class Car(Vehicle):
    pass

class Van(Vehicle):
    pass

class Estatecar(Vehicle):
    pass

pickup1 = PickUp()
pickup1.turnOnAirConditioner()
car1 = Car()
car1.turnOnAirConditioner()
van1 = Van()
van1.turnOnAirConditioner()
estatecar1 = Estatecar()
estatecar1.turnOnAirConditioner()