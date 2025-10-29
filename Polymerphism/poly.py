class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks Woof!")

class Cat(Animal):
    def sound(self):
        print("Cat meows Meow!")

animals = [Dog(), Cat()]

for a in animals:
    a.sound()
