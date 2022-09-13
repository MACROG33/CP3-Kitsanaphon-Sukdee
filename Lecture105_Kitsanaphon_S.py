class Vehicle:
    lecenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")
class Car(Vehicle):
    pass

class Pickup(Vehicle):
    pass

class Van(Vehicle):
    pass
class EstateCar(Vehicle):
    pass

car = Car()
car.turnOnAirConditioner()
pickup = Pickup()
pickup.turnOnAirConditioner()
van = Van()
van.turnOnAirConditioner()
estateCar = EstateCar()
estateCar.turnOnAirConditioner()
