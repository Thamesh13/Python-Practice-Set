class Rectangle:
    def __init__(self, h, w):
        self.height=h
        self.width=w

    def area(self):
        return self.height*self.width
    
    def perimeter(self):
        return 2*(self.height+self.width)

r1=Rectangle(10,20)
r2=Rectangle(30,40)

print(r1)
print(r2)
print(r1.area())
print(r1.perimeter())
print(r2.area())
print(r2.perimeter())