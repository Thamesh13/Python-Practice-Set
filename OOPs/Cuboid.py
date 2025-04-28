class Cuboid:

    # l=10
    # b=20
    # h=5
    def __init__(self,l,b,h):
        self.len=l
        self.bre=b
        self.hei=h

    def l_area(self):
        return self.len*self.bre
    
    def t_area(self):
        return 2*(self.len*self.bre+self.len*self.hei+self.bre*self.hei)

    def vol(self):
        return self.len*self.bre*self.hei

    def compare(self,other):
        if self.len==other.len and self.bre==other.bre and self.hei==other.hei:
            return True
        else:
            return False
    
c1=Cuboid(10,20,5)
c2=Cuboid(10,20,5)
# c1=Cuboid()
# c2=Cuboid()
# give the Address of c1
print(c1)
# give the type of c1
print(type(c1))

print(c1.l_area())
print(c1.t_area())
print(c1.vol())
print(id(c1))
print(id(c2))
print(c1==c2)
print(c1 is c2)
print(c1.len)
print(c1.bre)
print(c1.hei)

print(c2.l_area())
print(c2.t_area())
print(c2.vol())

print(c1.compare(c2))