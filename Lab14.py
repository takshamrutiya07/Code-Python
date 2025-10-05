# class Car:
#     # Constructor to initialize the object
#     def __init__(self, brand, model):
#         self.brand = brand  # Attribute
#         self.model = model  # Attribute

#     # Method to describe the car
#     def car_details(self):
#         return f"Car: {self.brand}, Model: {self.model}"

# # Creating an object of the Car class
# my_car = Car("Toyota", "Corolla")
# print(my_car.car_details())  


# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
#     def perimeter(self):
#         return 2 * (self.width + self.height)
# rect = Rectangle(10, 5)
# print(f"Area: {rect.area()}") 
# print(f"Perimeter: {rect.perimeter()}") 


# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.__balance = balance 

#     def deposit(self, amount):
#         self.__balance += amount

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient funds")

#     def get_balance(self):
#         return self.__balance
# account = BankAccount("John", 1000)
# account.deposit(500)
# print(account.get_balance())  
# account.withdraw(700)
# print(account.get_balance()) 


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "I am an animal."
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says Woof!"

# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says Meow!"

# dog = Dog("Buddy")
# cat = Cat("Whiskers")
# print(dog.speak())  
# print(cat.speak())   

# class Polygon:
#     def render(self):
#         print("Rendering Polygon...")

# class Square(Polygon):
#     def render(self):
#         print("Rendering Square...")

# class Circle(Polygon):
#     def render(self):
#         print("Rendering Circle...")
    
# s1 = Square()
# s1.render()
# c1 = Circle()
# c1.render()

# from abc import ABC, abstractmethod
# # Abstract class
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius

# circle = Circle(5)
# print(f"Area of the circle: {circle.area()}")


#Post Lab:
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
        
#     def AreaOfCircle(self):
#         return 3.14*self.radius*self.radius
    
#     def PerimeterOfCircle(self):
#         return 2*3.14*self.radius
    
# circle = Circle(4)
# print(f"Area of the circle:{circle.AreaOfCircle()}")    
# print(f"Perimeter of the circle:{circle.PerimeterOfCircle()}")   



# class Circle:
#     def __init__(self,radius):
#      self.radius=radius

#     def areaofcircle(self):
#         return f"area: {3.14*self.radius*self.radius}"
    
#     def perimeterofcircle(self):
#        return f"perimeter: {2*3.14*self.radius}"
    
# circle1=Circle(10)
# print(circle1.areaofcircle())
# print(circle1.perimeterofcircle())

# Circle is the class, circle1 is the object and radius is the attribute of the object circle1

class Books:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
  
    def bookdetails(self):
        return f"BookTitle: {self.title}, BookAuthor: {self.author}, BookPrice: {self.price}, DiscountOf: {0.1 * self.price}"
    
    def updatedprice(self):
        return f"Updated Price: {self.price - 0.1 * self.price}"
   
testbook1 = Books("Perks of Being A Wallflower", "Stephen Chbosky", 250)
print(testbook1.bookdetails())

testbook2 = Books("The Fault in Our Stars", "John Green", 150)
print(testbook2.bookdetails())
print(testbook2.updatedprice())

