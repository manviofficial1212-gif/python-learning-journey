class Vehicle:
    def start(self):
        print("Vehicle is starting")


class Car(Vehicle):
    def start(self):
        print ("car is starting")


v = Vehicle()
v.start()

c = Car()
c.start()