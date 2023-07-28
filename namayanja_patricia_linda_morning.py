from abc import ABC, abstractclassmethod
from tkinter import messagebox
import math
import tkinter as tk

# inheritance


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating...")


class Dog(Animal):
    def bark(self):
        print(f"{self.name}is barking...")


class Cat(Animal):
    def meow(self):
        print(f"{self.name}is meowing...")


animal = Animal("Generic Animal")
dog = Dog("spot")
cat = Cat("Fluffy")

# Invoke call Eat Method
animal.eat()
dog.eat()
dog.bark()
cat.eat()
cat.meow()


# example2 demonstrating inheritance
# Example2
class vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def display_info(self):
        print("Brand:", self.brand)
        print("color:", self.color)

    def move(self):
        print("moving the vehicle...")


class Car(vehicle):
    def __init__(self, brand, color, num_wheels):
        super().__init__(brand, color)
        self.num_wheels = num_wheels

    def display_info(self):
        # super().display_info()
        print("Number of wheels:", self.num_wheels)

    def honk(self):
        print("Honking the horn...")


# create a car object
my_car = Car("Toyota", "Red", 4)
# Access and modify the car attributes
print("Brand:", my_car.brand)
my_car.color = "Gray"

# invoke the car methods
my_car.display_info()
my_car.move()
my_car.honk()

# exercise
# Exercise1
# Demonstrate using inheritance to calculate area and perimeter of circle and rectangle


class Shape:
    def calculate_area(self):
        pass  # To be implemented by subclasses

    def calculate_perimeter(self):
        pass  # To be implemented by subclasses


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


# Creating instances of Circle and Rectangle classes
circle = Circle(5)
rectangle = Rectangle(12, 6)

# Calculating area and perimeter using the inherited methods
circle_area = circle.calculate_area()
circle_perimeter = circle.calculate_perimeter()
rectangle_area = rectangle.calculate_area()
rectangle_perimeter = rectangle.calculate_perimeter()

# Displaying the results
print(f"Circle: Area = {circle_area}, Perimeter = {circle_perimeter}")
print(f"Rectangle: Area = {rectangle_area}, Perimeter = {rectangle_perimeter}")


# Example3
# Multiple inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating...")


class Flyable:
    def fly(self):
        print(f"{self.name} is flying...")


class Bird(Animal, Flyable):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

    def display_info(self):
        print(f"species:{self.species}")
        print(f"{self.name}")


# create a bird object
my_bird = Bird("Pigeon", "bird")

# invoke the bird methods
my_bird.eat()
my_bird.fly()
my_bird.display_info()

# Method overriding


class Animal:
    def make_sound(self):
        print("Animal is making a sound!")


class Dog(Animal):
    def make_sound(self):
        print("Dog is barking!")


class Cat(Animal):
    def make_sound(self):
        print("Cat is meowing!")

def make_animal_sound(animal):
    animal.make_sound()

    # create objects
    animal = Animal()
    dog = Dog()
    cat = Cat("Adam")

    # calling make_animal_sound
    make_animal_sound(animal)  # animal is making a sound!
    make_animal_sound(dog)  # dog is barking!
    make_animal_sound(cat)  # cat is meowing!


# polymorphism
# polymorphism allows you to write code that can work with different objects
# method overriding
# method overloading

# Example4
class Shape:
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length*self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius


# create shape objects
rectangle = Rectangle(5, 5)
Circle = Circle(5)

# calculate display area

print("Area of Rectangle:", rectangle.calculate_area())
print("Area of a circle:", circle.calculate_area())
"""
#overloading functions
class Calculator:
    def add(self,x,y):
       return x+y
    def add(self,x,y,c):
      return x+y+c

#create object
calculator = Calculator()
  #Display output
print(calculator.add(7,2))
#an error of one argument missing
print(calculator.add(1,2,3))
"""
# example using if conditions in overloading functions


class MyClass:

    def my_method(self, arg1, arg2=None, arg3=None):
        if arg3 is None:
            result = arg1 + arg2
        else:
            result = arg1 + arg2 + arg3
        return result


# create an object
obj = MyClass()
# invoke the function
result1 = obj.my_method(10, 5)
print(result1)

result2 = obj.my_method(10, 5, 2)
print(result2)


# example3
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating...")


class Flyable:
    def fly(self):
        print(f"{self.name} is flying...")


# demo for multiple inheritance
class Bird(Animal, Flyable):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

    def display_info(self):
        # super.display_info()
        print(f"species: {self.species}")
        print(f"Name: {self.name}")


# creating a bird object
my_bird = Bird("pigeon", "bird")

# invoke the bird methods
my_bird.eat()
my_bird.fly()
my_bird.display_info()


# CONCEPT 2
# polymorphism allows you to write code that can work with different objects
# method overriding occurs when the derived class(child class),provides its own
# implementation of a method that is already defined in its super class
# method overloading allows a class to have multiple methods with the same name
#  but different parameters

# example 4
class Shape:
    def calculate_area(self):
        pass


class circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14*self.radius

    def calculate_circumference(self):
        return 2*3.14*self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length*self.width


# creating shape objects
rectangle = Rectangle(5, 5)
circle = circle(5)

# calculate display area
print("Rectangle area:", rectangle.calculate_area())
print("circle area: ", circle.calculate_area())


# abstraction
# allows you to focus on essential features and hide them from
# unnecessary details
# example5:demonstrate abstraction

# Exercise
# Demonstrate abstraction by calculating the area of a circle and rectangle
# encapsulating enables us achieve abstraction
class Shape:
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2


class Rectangle(Shape):


    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


circle = Circle(5)
circle_area = circle.calculate_area()
print("Area of the circle:", circle_area)

rectangle = Rectangle(5,6)
rectangle_area = rectangle.calculate_area()
print("Area of the rectangle:", rectangle_area)

# Exercise
# Demonstrate abstraction by calculating the area of a circle and rectangle


class Shape:
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2


class Rectangle(Shape):


    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


# create objects
circle = Circle(5)
circle_area = circle.calculate_area()
print("Area of the circle:", circle_area)

rectangle = Rectangle(10, 3)
rectangle_area = rectangle.calculate_area()
print("Area of the rectangle:", rectangle_area)


# exercise for creating a receipt


def print_receipt():
    customer_name = customer_name_entry.get()
    item_name = item_name_entry.get()
    item_quantity = item_quantity_entry.get()
    item_price = item_price_entry.get()

    if not customer_name or not item_name or not item_quantity or not item_price:
        messagebox.showwarning("Error", "Please fill in all fields.")
        return

    total_price = int(item_quantity) * float(item_price)

    receipt_text = f"Customer: {customer_name}\n" \
                   f"Item: {item_name}\n" \
                   f"Quantity: {item_quantity}\n" \
                   f"Unit Price: ${item_price}\n" \
                   f"Total Price: ${total_price:.2f}\n"

    receipt_textbox.delete(1.0, tk.END)  # Clear any previous content
    receipt_textbox.insert(tk.END, receipt_text)


def clear_fields():
    customer_name_entry.delete(0, tk.END)
    item_name_entry.delete(0, tk.END)
    item_quantity_entry.delete(0, tk.END)
    item_price_entry.delete(0, tk.END)
    receipt_textbox.delete(1.0, tk.END)


# Create the main application window
app = tk.Tk()
app.title("Linda's Receipt Printing Program")
app.configure(background="lightgrey")

# Create and arrange the widgets
customer_name_label = tk.Label(app, text="ClientName:")
customer_name_label.grid(row=0, column=0, padx=5, pady=5)
customer_name_entry = tk.Entry(app)
customer_name_entry.grid(row=0, column=1, padx=5, pady=5)

item_name_label = tk.Label(app, text="Item Name:")
item_name_label.grid(row=1, column=0, padx=5, pady=5)
item_name_entry = tk.Entry(app)
item_name_entry.grid(row=1, column=1, padx=5, pady=5)

item_quantity_label = tk.Label(app, text="Quantity:")
item_quantity_label.grid(row=2, column=0, padx=5, pady=5)
item_quantity_entry = tk.Entry(app)
item_quantity_entry.grid(row=2, column=1, padx=5, pady=5)

item_price_label = tk.Label(app, text="Unit Price:")
item_price_label.grid(row=3, column=0, padx=5, pady=5)
item_price_entry = tk.Entry(app)
item_price_entry.grid(row=3, column=1, padx=5, pady=5)

print_button = tk.Button(app, text="Print Receipt", command=print_receipt)
print_button.grid(row=4, column=0, padx=5, pady=5)

clear_button = tk.Button(app, text="Clear Fields", command=clear_fields)
clear_button.grid(row=4, column=1, padx=5, pady=5)

receipt_textbox = tk.Text(app, height=10, width=40)
receipt_textbox.grid(row=5, columnspan=2, padx=5, pady=5)

# Start the application event loop
app.mainloop()
