class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # call parent constructor
        self.breed = breed

    def sound(self):
        super().sound()  # call parent method
        print(f"{self.name} barks Woof!")

d = Dog("Tommy", "Labrador")
d.sound()
