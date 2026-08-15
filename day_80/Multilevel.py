class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Woof!")


class Puppy(Dog):
    def play(self):
        print("Playing")


p = Puppy()

p.eat()
p.bark()
p.play()
