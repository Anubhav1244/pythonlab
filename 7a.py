class Rectangle:

    def __init__(self,lenght,breadth):
        self.length=lenght
        self.breadth=breadth
    def getArea(self):
        print("area:",self.length*self.breadth)

class Triangle:

    def __init__(self,base,height):
        self.base=base
        self.height=height
    def getArea(self):
        print("area of triangle:",self.base*self.height*0.5)

class Circle:

    def __init__(self,radius):
        self.radius=radius
    def getArea(self):
        print("area of circle :",self.radius*self.radius*3.14)

r=Rectangle(3,5)
r.getArea()
t=Triangle(4,2)
t.getArea()
c=Circle(3)
c.getArea()

