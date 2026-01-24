## In python everything is an object
## Every object has,
##         * A type
##         * A internl data repersentation
##         * Own methods(Functionalities)

# creating a class:
#   class class_name (object):

# lets create two classes, one for circle and one rectangle

import matplotlib.pyplot as plt

class Circle (object):
    #use __init__ for initializing class
    def __init__(self, radius, color):
        #define atttributes
        self.radius = radius
        self.color = color
        
    
    #increase radius
    def add_raidus(self,r):
        self.radius = self.radius + r
        return self.radius
    
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()
    
#rectangle creation
class Rectangle (object):
    #use __init__ for initializing class
    def __init__(self, height, width, color): 
        #define atttributes
        self.height = height,
        self.width = width,
        self.color = color
        
c1 = Circle(4, 'green')
c1.drawCircle()
print(c1)
print(c1.color)

r1 = Rectangle(4,3,'red')
print(r1)
print(r1.color)



#real-world example

class Car:
    max_speed = 180
    
    #Initializing the class
    def __init__(self, make, model, color, speed = 0):
        self.make = make,
        self.model = model,
        self.color =color,
        self.speed = speed
    
    #acceleration the car
    def acceleration(self, acceleration):
        if self.speed + acceleration <= Car.max_speed:
            self.speed += acceleration
        
        else:
            self.speed = Car.max_speed
    
    def get_speed(self):
        return self.speed
    
toyota1 = Car('Toyota', 'Camry', 'Black')
print(toyota1.get_speed())

toyota1.acceleration(50)
print(toyota1.get_speed())
    