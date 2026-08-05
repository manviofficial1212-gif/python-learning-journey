class Phone:
    brand = "Samsung"

    def __init__(self, model):
        self.model = model

    def call(self):
        print("Calling...")


p = Phone("Galaxy")
print(dir(p))
print(p.__dict__)
help(p)