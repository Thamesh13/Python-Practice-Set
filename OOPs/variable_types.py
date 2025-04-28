'''# Ways to creating instance variables:

class Test:
    def __init__(self):
        self.a=5

    def fun(self):
        self.b=20

t1=Test()
t1.fun()
t1.c=25
print(dir(t1))
print(t1.a)
print(t1.b)
print(t1.c)'''



'''
# CLASS & STATIC METHOD:
class Rectangle:
    # class variable
    count =0

    def __init__(self, len, bre):
        self.l=len
        self.b=bre
        Rectangle.count+=1

    def area(self):
        return self.l*self.b
    
    def perimeter(self):
        return 2*(self.l+self.b)
    
    # class method
    @classmethod
    def get_count(cls):
        return cls.count
    
    # static method
    @staticmethod
    def is_square(l,b):
        return l==b
    
r1=Rectangle(10,20)
r2=Rectangle(30,40) 
r3=Rectangle(15,60)

print(r1.area())
print(r2.area())
print(r3.area())
print(r1.l)
print(r2.l)
print(r3.l)

# the count based on the memory block above.
print(r1.get_count())
print(r2.get_count())
print(Rectangle.get_count())


print(r1.is_square(10,20))
print(r1.is_square(20,20))'''



'''
# ACCESSER & MUTATOR:
# ACCESSER -->Read and get the value from the object
# MUTATOR -->Set and Update the value of the object


class Rectangle:
    def __init__(self, h, w):
        self.height=h
        self.width=w

    # ACCESSER -->Read and get the value from the object
    def getlen(self):
        return self.height
    
    # MUTATOR -->Set and Update the value of the object
    def setlen(self, h):
        self.height=h

    def area(self):
        return self.height*self.width
    
    def perimeter(self):
        return 2*(self.height+self.width)
    
r1=Rectangle(10,20)
r2=Rectangle(30,40)

print(r1.getlen())
print(r2.getlen())

r1.setlen(50)
r2.setlen(20)

# what are values are updated with help of MUTATOR, that will print here.
print(r1.getlen())
print(r2.getlen())'''




'''
# SINGLE LEVEL INHERITANCE:
# Parent class can not access the Child class.
# Child class can access the Parent class.
class Rectangle:
    def __init__(self,l,b):
        self.len=l
        self.bre=b

    def area(self):
        return self.len*self.bre
    
class Cuboid(Rectangle):
    def __init__(self,l,b,h):
        # super() is used to call the constructor(instant variable & methods) of the parent class.
        super().__init__(l,b)
        self.hei=h

    def vol(self):
        return self.len*self.bre*self.hei

c=Cuboid(10,20,5)
print(c.area())
print(c.vol())

r=Rectangle(10,20)
print(r.area())
print(r.vol()) # Error: 'Rectangle' object has no attribute 'vol'
'''





'''
# MULTI LEVEL INHERITANCE:
class A:
    def feature1(self):
        print("Feature 1 from class A")
    def feature2(self):
        print("Feature 2 from class A")

# Inheriting by using B(A):
class B(A):
    def feature3(self):
        print("Feature 3 from class B")
    def feature4(self):
        print("Feature 4 from class B")

class C(B):
    def feature5(self):
        print("Feature 5 from class C")

    def feat(self):
        super().feature1()

a1=A()

a1.feature1()
a1.feature2()

# a1.feature3() # Error: 'A' object has no attribute 'feature3'

# using feature1 from class A
b1=B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()

# b1.feature5() # Error: 'B' object has no attribute 'feature5'

c1=C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
'''





'''
# MULTIPLE INHERITANCE:

class A:

    def __init__(self):
        print("This is call method of class A")

    def feature1(self):
        print("Feature 1 from class A")

    def feature2(self):
        print("Feature 2 from class A")

# Inheriting by using B(A):
class B:
    def __init__(self):
        print("This is call method of class B")

    def feature3(self):
        print("Feature 3 from class B")

    def feature4(self):
        print("Feature 4 from class B")

# Inheriting by using C(B,A):

class C(A,B):

    def __init__(self):
        super().__init__()
        print("This is call method of class C")

    def feature5(self):
        print("Feature 5 from class C")


a1=A()
# a1 can access only the Class A features:
a1.feature1()
a1.feature2()
# a1.feature3() # Error: 'A' object has no attribute 'feature3'

b1=B()
# b1 can access only the Class B features:
b1.feature3()
b1.feature4()
# b1.feature1() # Error: 'B' object has no attribute 'feature1'


c1=C()
# c1 can access the Class A & B features:
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()'''


'''
# POLYMARPHYSM:
# Method Overriding:
def Driver(car):
    car.driver()

class Creta:
    def driver(self):
        print("Creta is driving")

class Mercedes:
    def driver(self):
        print("Mercedes is driving")

c=Creta()
m=Mercedes()
Driver(c)
Driver(m)
'''

'''
class Arith:
    def sum(self, x, y):
        return x+y
    
a=Arith()
print(a.sum(10,20))
print(a.sum(1.5,2.5))
print(a.sum("Hello", " World"))'''

'''class Arith:
    # 2nd func is overriding the 1st function, so we need to pass the 3 value below.
    def sum(self,x,y):
        return x+y
    
    def sum(self,x,y,z):
        return x+y+z
a=Arith()
a.sum(5,6,7)
a.sum(5,6,7)'''

'''
# Method Overloading:
# In Python, we can overload the method by using the default value of the parameter.
class Arith:
    def sum(self,x,y,z=None):
        s=x+y
        if z==None:
            return s
        else:
            return s+z
a=Arith()
print(a.sum(5,6,7))
print(a.sum(5,6))'''




'''
# Method Overriding:
# In Python, we can override the method by using the super() method.
# In the below example, we are overriding the home method of the parent class.
# The super() method is used to call the parent class method.
class Nokia:
    def home(self):
        print("Home screen nokia")
class Samsung(Nokia):
    def home(self):
        print("Home screen sam")
        super().home()

n=Samsung()
o=Nokia()
n.home()
o.home()
'''

# print(len('besant'))
# print(len([1,2,3]))

'''
# Operator overloading polymorphism
a=9
b=1
print(a+b)
print(int.__add__(a,b)) # 9+1=10'''

'''
class Student:
    def __init__(self, m1, m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=Student(m1,m2)
        return s3

    def __gt__(self, other):
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        if r1> r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)
    
s1=Student(58,60)
s2=Student(60,65)
s3=s1+s2
print(s1.__add__(s2))
print(s3.m1)

if s1>s2:
    print('True')
else:
    print('false')

a=int(9)
print(a)
print(a.__str__())

print(s1)
print(s1.__str__())

print(s2)
print(s2.__str__())'''




















