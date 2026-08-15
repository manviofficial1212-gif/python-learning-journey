class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Woof!")


d = Dog()

d.eat ()
d.bark ()