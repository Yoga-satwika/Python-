
class Animal:
    def sound(self):
        print("Animals make different sounds.")

class Dog(Animal):
    def bark(self):
        print("Dog barks Woof!")

d = Dog()
d.sound()  
d.bark()   
