from abc import ABC, abstractmethod

# Encapsulation
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public attribute
        self.__balance = balance    # Private attribute (encapsulated)

    # Public method to access private data
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds.")

    # Public method to access private data
    def get_balance(self):
        return self.__balance


# Abstraction
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

    def move(self):
        return "Runs"

class Bird(Animal):
    def sound(self):
        return "Chirp"

    def move(self):
        return "Flies"


#Inheritance

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"Make: {self.make}, Model: {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)  # Call parent class constructor
        self.num_doors = num_doors

    def display_info(self):
        return f"{super().display_info()}, Doors: {self.num_doors}"

#Polymorphism Override

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Polymorphism Overload

class MathOperations:
    def add(self, *args, **kwargs):  # Overloading with variable-length arguments
        return sum(args, kwargs)
    
    


