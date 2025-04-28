print('Hello')
print(5+5)
print('Welcome to python')
#-------------------------------SEQUENCE DATA TYPE------------------------------
#====>RANGE
for i in range(5):
     print(i)
for x in range(3, 8):
    print(x)
for y in range(0,10,1):
    print(y)
for a in range(5,12,2):
    print(a)
for b in range(-10, -5,1):
    print(b)
for d in range(8,2,-1):
    print(d)
list(range(10,15,1))
#-------------------------------SET DATA TYPE------------------------------
#====>SET
    #Hetrogeneous
a={"apple", 5, True, 6.1, 5+6j, False, 0}
print(a)
    #Unordered
b={5,4,3,0,-1,10,-10}
print(b)
    #Not-Allow Duplicate
c={10,2,2,20}
print(c)
    #Not-allow Indexing
#d={1,2,3}
#d[1]
    #Immutable
#e={4,5,6}
#e[2]=8
