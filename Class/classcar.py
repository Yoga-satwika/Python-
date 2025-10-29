class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def show_details(self):
        print(f"Brand: {self.brand}, Color: {self.color}")


car1 = Car("Tesla", "Red")
car2 = Car("BMW", "Black")

car1.show_details()
car2.show_details()

        
