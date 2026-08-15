class Camera:
    def take_photo(self):
        print("Taking photo")


class Phone:
    def make_call(self):
        print("Making call")


class Smartphone(Camera, Phone):
    pass


s = Smartphone()

s.take_photo()
s.make_call()
