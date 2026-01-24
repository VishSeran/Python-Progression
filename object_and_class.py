## In python everything is an object
## Every object has,
##         * A type
##         * A internl data repersentation
##         * Own methods(Functionalities)

# creating a class:
#   class class_name (object):

# lets create two classes, one for circle and one rectangle
class Circle (object):
    
    def __init__(self, radius, color):
        self.radius = radius,
        self.color = color
        
    
    #increase radius
    def add_raidus(self,r):
        self.radius = self.radius + r
        return self.radius
    
#rectangle creation
class Rectangle (object):
    
    def __init__(self, height, width, color):
        self.height = height,
        self.width = width,
        self.color = color
        
c1 = Circle(4, 'green')
print(c1)
print(c1.color)

r1 = Rectangle(4,3,'red')
print(r1)
print(r1.color)