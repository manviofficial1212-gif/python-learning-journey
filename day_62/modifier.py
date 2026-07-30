class laptop:
    def __init__(self):
        self.brand="HP"
        self._ram = "16gb"
        self.__price =65000
    def show (self):
        print(self.brand)
        print(self._ram)
        print(self.__price)
lap = laptop ()
print (lap.brand)
print(lap._ram)
lap.show()
print (lap.__price)