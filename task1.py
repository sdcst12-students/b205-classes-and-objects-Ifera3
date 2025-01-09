"""
Rectangular Prism Object
Create a class that creates a rectangular prism.  You should be able to set all of the important measurements (l,w,h) when the object is instantiated in the constructor and you should have class methods that determine the surface area and volume.
You should have class methods that also allow you to change the dimensions of the object.
Instantiate 3 separate rectangular prisms with the test data given, and check the assertions are correct.
"""

class rectPrism:

    def __init__(self, l=1, w=1, h=1):
        if l == 0:
            print("Invalide lingth entered")
        if w == 0:
            print("Invalide width entered")
        if h == 0:
            print("Invalide hight entered")
        self.lingth = l
        self.width = w
        self.hight = h

    def volume(self):
        if self.lingth == 0:
            print("Invalide lingth entered")
            return None
        elif self.width == 0:
            print("Invalide width entered")
            return None
        elif self.hight == 0:
            print("Invalide hight entered")
            return None
        else:
            A = self.lingth * self.width * self.hight
            return A 
    
    def surfaceArea(self):
        if self.width == 0:
            print("Invalide width entered")
            return None
        elif self.hight == 0:
            print("Invalide hight entered")
            return None
        elif self.lingth == 0:
            print("Invalide lingth entered")
            return None
        else:
            SA =  self.lingth * self.width * 2 + self.width * self.hight * 2 + self.lingth * self.hight * 2
            return SA

    def __str__(self):
        return f"{self.lingth}, {self.width}, {self.hight}"

# class instances and assertions below:

a = rectPrism(l=10,w=2,h=5)
assert a.volume() == 100
assert a.surfaceArea() == 160

b = rectPrism(l=1,w=1,h=1)
assert b.volume() == 1
assert b.surfaceArea() == 6

c = rectPrism(l=2,w=0,h=10)
# note the invalid width
assert c.volume() == None
assert c.surfaceArea() == None