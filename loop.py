##-----------------------------20 MAR 25---------------------------------------------------------------------------------------
'''
#PRINT 'HELLO' 5 TIMES:
count=0
while count<5:
    print('Hello')
    count +=1


#PRINT 'HI' 10 TIMES
count=10
while count>0:
    print('Hi')
    count -=1



#PRINT 'n' REVERSE ORDER one by one:
n=1234
while n>0:
    l=n%10
    print(l)
    n=n//10



#PRINT 'n' REVERSE ORDER one by one:
n=56789
rev=0
while n>0:
    l=n%10
    t=rev*10+l
    print(t)
    n=n//10




#PRINT 'n' REVERSE ORDER:
n=1234
rev=0
while n>0:
    l=n%10
    rev=rev*10+l
    n=n//10
print(rev)


#NO OF TIMES PRINTING 'CANDY':
count=int(input('Enter the count;'))
if count>0 and count<11:
    i=1
    while i<=count:
        print('candy')
        i +=1
else:
    print('Invalid No:')



#PRINT 'i' VALUE
i=0
while i<3:
    print(i)
    i +=1
    
print(i)



#ADDING THE NO. OF VALUES
sab=3
i=0
s=0
while i<sab:
    m=int(input('Enter the Mark:'))
    s +=m
    i +=1
print(s)


#PRINT VALUE AS LIST
n=int(input('Elevate size:'))
l=[]
i=0
while i<n:
    m=int(input('Enter Number:'))
    l.append(m)
    i+=1
print(l)


n=int(input('Enter size:'))
p=0
l=[]
y=0
k=[]
while p<=n:
    num=int(input('Enter Number:'))
    if num>=0:
        l.append(num)
        p +=1
    else:
        k.append(num)
        y +=1
        
print(l)
print(p)
print(k)
print(y)
'''


##------------------------------------------------21 MAR 25---------------------------------------------------------------------------------------

'''
##CONTINUE STATEMENT:(Iteration will continue eventhough condition isn't match)
i=1
while i<=10:
    if i%3==0:
        i+=1
        continue
    print(i)
    i = i+1



## WHILE TRUE: Its helps to continue loop infinite time's
## BREAK STATEMENT:(Iteration will continue till meet the break statement) 
n=int(input('Enter the Number:'))
while True:
    if n>0:
        print('positive')
    elif n<0:
        print('negative')
    else:
        break
print('Stop loop')



## PASS STATEMENT: (The value will be Pass when the condition isn't match)
i=0
while i<10:
    if i%2==0:
        print(i)
    else:
        pass
    
    i+=1




## Break the Iteration of loop by using BREAK STATEMENT inside 'if' condition:
i=0
while i<20:
    print(i)
    i+=1
    if i>10:
        break
else:
   print('Ending')
print('end')



## Break the Iteration of loop by using the BREAK STATEMENT inside 'else' based of 'if' condition:
i=0
while i<20:
     if i<=10:
         print(i)
         i+=1
     else:
        break
print('end')



##Printing Each Character on by one:
x='Hello'
for character in x:
    print(character)



##Printing Each value of the list one by one
h=[1,2,3]
for v in h:
    print(v)


## Printing Each value of the Range one by one
z=range(0,10)
for i in z:
    print(i)




## Printing Each value in Sequence By using end='  ' insted of default attribute end='\n'

for y in range(20, 10, -2):
    print(y, end='\n')

for i in range(20, 10, -2):
    print(i, end=' ')



## NESTED LOOP

# Print the value in new line for each iteration by using 'print()'
for i in range(0,5):
    for j in range(10,15):
        print(i,j, end='  ')
    print()

# Print the value with the Sequence order due to not using 'print()'
for i in range(0,5):
    for j in range(10,14):
        print(i,j, end='  ')
'''

'''
## PRINTING '#' PATTERN FROM 0-5(Ascending order)
for i in range(0,6):
    print('#'*i)


## PRINTING '#' PATTERN FROM 5-1(Descending order)
for i in range(5,0,-1):
    print('#'*i)


## PRINTING '#' PATTERN LIKE BOX SHAPE
for i in range(0,5):
    for j in range(1,5):
        print('#', end=' ')
    print()

## PRINTING '#' PATTERN LIKE BOX SHAPE
for i in range(5,0, -1):
    for j in range(1,5):
        print('#', end=' ')
    print()
'''


##------------------------------------------------24 MAR 25---------------------------------------------------------------------------------------

'''
## PRINTING '#' PATTERN FROM 0-5(Ascending order)
for i in range(1):
    for j in range(1,6):
        print('@'*j)

## PRINTING '#' PATTERN FROM 5-1(Descending order)
for i in range(1):
    for j in range(5,0,-1):
        print('#'*j)

## PRINTING '#' PATTERN FROM 0-5(Ascending order)
for i in range(1,6):
    for j in range(1):
        print('$'*i)

## PRINTING '#' PATTERN FROM 5-1(Descending order)
for i in range(5,0,-1):
    for j in range(1):
        print('%'*i)
'''

'''
## PRINTING '#' PATTERN LIKE BOX SHAPE
for i in range(4):
    for j in range(4):
        print('$', end=' ')
    print()

## PRINTING '#' PATTERN FROM 0-5(Ascending order)
for i in range(4):
    for j in range(i+1):
        print('#', end=' ')
    print()

## PRINTING '#' PATTERN FROM 5-1(Descending order)
for i in range(4):
    for j in range(4-i):
        print('%', end=' ')
    print()
'''

'''
##MATCH CASE FUNCTION: Match/Case is a Keyword
x=int(input('enter input:'))
match x:
    case 1:
        print('sunday')
    case 2:
        print('monday')
    case 3:
        print('tuesday')
    case 4:
        print('wednesday')
    case 5:
        print('thursday')
    case 6:
        print('Friday')
    case 7:
        print('Saturday')
    case _:
        print('day')


##PRINT else block 5 times
num=[12,16,18,21,26]
for n in num:
    if n%5==0:
        print(n)
        break
    else:
        print('N/A')




##PRINT else block in 1 time
num=[12,16,18,21,26]
for n in num:
    if n%5==0:
        print(n)
        break
else:
    print('N/A')

##PRINT the value which is divisible by 5
num=[12,15,18,21,26]
for n in num:
    if n%5==0:
        print(n)
        break
else:
    print('N/A')




##Adding '-' among the Numbers:
a,b,c=(1,2,3)
print(a,b,c,)

a,b,c=(1,2,3)
print(a,b,c, sep='-')


##Joining the Name Method:
m='Tham'
print(m,'esh')
print(m+'esh')
#print(a+'esh')
print(a,'esh')



a='Suresh'
b=22
c=4.1234
print('Name %s, Number %d, Float %f' % (a,b,c))
print('%s' %a)
print('Name:', a, 'Number:', b, 'Float:',c)

##Using Format
print('Name: {} \n Number: {}'.format(a,b))
print(f'Name: {a} \t  Age: {b}')
print('Name:{0} \\ Age: {1}'.format(a,b))

'''


##------------------------------------------------25 MAR 25---------------------------------------------------------------------------------------

'''
##Defining string as a character, Number and Spl. Character.
s='Hello'
b='@#$*&'
n='12543'
print(s,b,n, sep=' || ')



##Identify character by using index value
s='Friend'
print(s[2])
print(s[5])
print(s[-1])
print(s[0])
print(len(s))



##Checking the String with single/double quot's
#s='Ram's hand' -->(It will thrown an error)
b='Ram"s hand'
c="Ram's friend"
f='Ram\'s bro'
print(b,c,f, sep=' || ')



##Create a New object & and storing the values.
s1='ab'
s2='cd'
print(s1+s2)
s1=s1+s2
print(s1)



##Adding 2 values & Multiply values || Use indexing.
s1='Hello'
s2='Ram'
print(s1+s2)
##print(s1+15)-->(It's throw erro bcz of different type of value's)
print(s1+str(15))
s=s1+s2
print(s)
print(s1*3)
print(s[2])
print(s[-5])



##Slizing Method(Starting:Ending:Step)
##STEP=Positive || Starting > Ending / STEP=Negative || Starting < Ending
s='Hello World'
print(s[::])
print(s[0:5:1])
print(s[0:5:2])
print(s[6::1])
print(s[:5:2])
print(s[0:15])
print(s[::-1])
print(s[-4::1])
print(s[-4:10:1])
print(s[-4:-10:-1])



##Length Method
s='Hello World'
print(len(s))
print(type(s))
print(s[0:len(s)])
print(s[0:len(s):2])
print(s[0:len(s):-2])
print(s[len(s):0:-2])
print(s[::-1])



##Boolian Method
s='Hello World'
m='madam'
print(m==m[::-1])
print('h' in s)
print('Hel' in s)
print('HelloWorld' in s)
print('HelloWorld' not in s)



##Using type || dir || endswith || find
a=''
print(type(a))
#Showing list of Methods
print(dir(a))

s='hello'
print(help(s.endswith))
print()

print(help(s.find))




s='Hello world'
s1='Hello'
s2='world'

##FIND(Exhibit -1 when the substring isn't placed)
print(s)
print(s.find('o'))
print(s.find('o',5))
print(s.find('x'))
print(s.rfind('o'))
print(s.rfind('z'))
print()


##INDEX (Exhibit Error msg when the substring isn't placed)
print(s.index('o'))
#print(s.index('z'))-->ValueError: substring not found
print(s.index('world'))
print()


##COUNT (Exhibit 0 when the substring isn't placed)
print(s.count('o'))
print(s.count('z'))


##JUST (It set space for the character)
s1='hello'
print(s1.ljust(10))
print(s1.rjust(10))
##print(s1.just())
print()


##STRIP
m1='  Python'
m2='Ram   '
print(m1.lstrip())
print(m1.rstrip())
print(m2.lstrip())
print(m2.rstrip())
print(m1.strip())

n='  python programming'
print(n.strip())

n='....###python'
print(n.lstrip())
print(n.lstrip('.'))
print(n.lstrip('.#'))






s='Hello world'
m='Hello wOrLd'
#capital each word starting
print(m.title())
print(m.capitalize())

#Upper & lower case
print(m.lower())
print(m.upper())

#upper change to lowercase & loswercase change to upper
print(m.swapcase())

#check m is uppercase or not
print(m.isupper())
print('HELLO'. isupper())

#Checking Address of Str
print(id('HELLO'))

##BOOL Method:
print('How Are'.istitle())

#Check Aplhabet & Number
print('abc12'.isalnum())
print('abc12#'.isalnum())

#Check Aplhabet & Number
print('abcYU'.isalpha())

#Check space
print('hello world'.isspace())
print('helloworld'.isspace())
print(' '.isspace())





##Usingg Endswith || Remove Suffix & Prifix
s='hello world'

#Check the world endswith as per character or not
print(s.endswith('ld'))
print(s.endswith(' world'))
print(s.startswith(' word'))
print(s.startswith('h'))

#Helps to delete Prefix & Suffix
print('python'.removesuffix('on'))
print('python'.removeprefix('on'))
print('python'.removeprefix('py'))

s='python is language'
s='python is pro language'
#It change each word as a string
print(s.partition('is'))
'''


##------------------------------------------------26 MAR 25---------------------------------------------------------------------------------------

'''
#REPLACE -->Return a copy with all occurrences of substring old replaced by new
s='a-b-c-d'
print(help(s.replace))
print(s.replace('-',' '))
print('abcd@gmail.com'.replace('gmail','yahoo'))
'''

'''
#JOIN -->String Concatenate in between each given string.
s1='xyz'
s2='abc'
print(help(s1.join))
print(s1.join(s2))
print(' '.join(s2))
print('.'.join(s1))
'''

'''
##SPLIT -->Return a list of the substrings in the string / Seperated by Delimited
s='ram dev sita'
print(s.split())
print(help(s.split))
print('abcd@gmail.com'.split('@'))
print('abcd@gmail.com'.split('@')[0])
'''

'''
##APPEND & EXTEND function in List
l1=[1,2,3,4]
l2=list((4,5,6,7))
print(type(l2))
l1[0]=6
print(l1)
print(len(l1))
print(l1[-2])

#Append object to the end of the list.
l1.append(7)
print(l1)
print(len(l1))
print(help(l1.append))

#Extend list by appending elements from the iterable.
#l1.extend(8) -->TypeError: 'int' object is not iterable
l1.extend([8])
print(l1)
print(help(l1.extend))
l1.extend([9,10])
print(l1)
'''

'''
m=[1,2,3]
print(m)
print(m+[5])
print(m*2)
print(2 in m)
print(5 not in m)
#Dir -->what are list properties are availabe inside the string object
print(dir(m))
m.extend('abc')
print(m)
#Adding value based on index
m.insert(0,10)
print(m)
'''

'''
l1=[12,3]
l2=l1.copy()
print(l2)
#It create new object and store value
print(id(l1))
print(id(l2))

a=[1,2]
b=a
#It store value in same address
print(id(a))
print(id(b))
'''

'''
##POP & DELETE--> Remove and return item at index (default last)
n=[1,2,3,4,5]
n.pop()
print(n)
print(help(n.pop))
n.pop(2)
print(n)
del n[0]
print(n)
'''

'''
##REMOVE --> Remove first occurrence of value
m=[1,2,3,4]
print(m)
del m[0:2]
print(m)
m.remove(3)
print(m)
m.remove(4)
print(m)
print(help(m.remove))
#m.remove(5) -->Raises ValueError if the value is not present
print(m)


l=[10,1,2,3,10]
l.remove(10)
print(l)
l.clear()
print(l)

x=[10,1,2,3,10]
del x[:]
print(x)
'''

'''
##INDEEX || COUNT || REVERSE || SORT

k=[10,2,3,4,5,10]
#Printing Index of the value
print(k.index(10))
print(help(k.index))

#Printing No. of value inside list
print(k.count(10))

#Printing the values in reverse order
k.reverse()
print(k)

#Printing values in ascending order
k.sort()
print(k)
print(help(k.sort))

#Printing values in Descending order
k.sort(reverse=True)
print(k)
'''

'''
##SORT
z=['aa','BB','JJ']
#Ascending order based on Askey key value of the alphabets
z.sort()
print(z)
#Printing value in Ascending order based in alphabets
z.sort(key=str.lower)
print(z)
#Ascending order based on Askey key value of the alphabets
print(sorted(z))
'''

'''
#SORT -->Arrange based on alphabet ascending order
a=['Thamesh','Rajesh','Abi','Balu']
a.sort()
print(a)
'''

'''
##RANGE -->LIST COMPRIENTIION
l=[x for x in range(1,11)]
print(l)
x=[x**2 for x in range(1,11)]
print(x)
z=[x for x in (1,2,3,4) if x%2==0]
print(z)
n=[x.lower() for x in 'Python']
print(n)
'''

'''
#TUPLE:
t=(1,2,3)
print(type(t))
print(t[0])
print(t[-2])
print(t[1:3])
#t[2]=10 -->can't edit the value bcz its immutable
print(t)
#Tuple access time very faster than list, bcz its immutable

#print(t[5])--.It index error

#Properties of Tuple
print(dir(t))
print(t.index(2))
'''

'''
##Single value inside tuple --> It consider as <class 'int'>
z=(10)
print(type(z))
#z=tuple((10)) -->TypeError: 'int' object is not iterable

#value in list enclose with tuple --> type is <class 'tuple'>
z=tuple([10])
print(type(z))

#Single value with comma in tuple -->It consider as <class 'tuple'>
d=(11,)
print(type(d))
'''


'''
r=10
print(type(r))
r1=1,2,3,4
print(r1)
print(type(r1))


a,c,d,e=r1
print(a,c,d,e)

m,n,o=9,7,4
print(m,n,o)

x,y,z='man'
print(y)
'''

##------------------------------------------------27 MAR 25---------------------------------------------------------------------------------------

'''
##LIST COMPRIENTION
l=[x for x in range(1,10)]
print(l)

##TUPLE COMPRIENTION
#Its give a output like detailed address.
y=(x for x in range(11,15))
b=((x for x in range(5,9)))
print(y)
print(b)

#Range is Coverting into the tuple
r=tuple(x for x in range(1,5))
print(r)

#The * helps to print the range as a tuple with the help of Comma at the end.
m=(*(x for x in range (1,10) if x%2==0),)
print(m)

z=(*(x for x in 'PyThoN' if x.islower()),)
print(z)

#(1,2)+(3,4)
t=(1,2,3,4,5)
s=(*(x for x in t),)
print(s)
r=(*(x for x in t[3:5]),)
print(r)
l=(*(x for x in t*2),)
print(l)
'''


'''
##SET

#The duplicate isn't allow
s={1,2,3.5,'Ram',3.4,'Ram'}
print(s)


#print(s[0])
#print(s[0:3]) -->Typerror

t=set((1,2,3))
print(t)

x=(4,3,2)
print(set(x))

m='tham'
print(set(m))

n=set('Ram')
print(n)

#Based on Ash size the print order will differ
n={1,2,3,4,5,6,7,8,9}
print(n)
s={5,10,21,15,3,11}
print(s)
print()

s1={1,2,3,5,7,13,15}
s2={5,7,9,10,11}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
s1.difference_update(s2)
#s1.intersection_update(s2)
print(s1)

#What are value are intercept with r1 by r2, that value's are updating in r1
r1={1,2,3,5,7}
r2={5,7,9,10,11}
#r1.difference_update(r2)
r1.intersection_update(r2)
print(r1)
'''

'''
a={1,2,3,4,5,6,7,8}
b={1,2,3,5,7}
c={4,56,8,10}
print(b.issubset(a))
print(a.issubset(b))
print(c.issubset(a))

#Adding value 60 at end of set
a.add(60)
print(a)

#Type erro due to add 1 value
#a.add(70,80)

#use to add 2 more values within ()
a.add((70,80))
print(a)

a.copy()
print(a)

#Add 2 more element
a.update({11,12})
print(a)

#Deleting 1st value
a.pop()
print(a)

#Deleted (70,80) value
a.discard((70,80))
print(a)

#Deteting value 60
a.discard(60)
print(a)

#Removing 2 value
a.remove(2)
print(a)

#Clear everything
a.clear()
print(a)

#Printing range 1 to 9
s={x for x in range(10)}
print(s)

#Can't add list & dict innside set bcz it lead to type error.
#s={1,2,[3,4],5}
#n={1,2,{a:5,b:2},10} -->TypeError
print(s)
#print(n)
'''

'''
##DICT
d={'Name':'Thame', 'Age':22, 'Org':'Working'}
print(d)
print(d['Name'])

d={1:2, 3:5}
print(d[3])

#TypeError: unhashable type: 'list'
#d={[1,2]:4}
#print(d)
#print(d[1,2])


d={(1,2):2}
print(d)
#TypeError: 'dict' object is not callable
#print(d(1,2))

d={101:'Tham', 102:'Sam'}
print(d[101])

#Updating
d[101]='Arun'
print(d)

#Creat new key value pair
d[103]='Sunil'
print(d)

#Key,value pair is deleted
del d[103]
print(d)
'''

'''
d={101:'Tham', 102:'Sam'}

#Only key are printing
for i in d:
    print(i)

#Key , values are printing
for i in d:
    print(i, d[i])
'''

'''
#Checking the Dict type
d1=dict()
d2={}
print(type(d2))
print(type(d1))
'''

'''
#Tuple inside Tuple convert to the Dict
d=dict(((1,2),(3,4),(5,6)))
print(d)

s=('ab', 'cd')
n=dict(s)
print(n)

#Zip helps to merge both list and given as Dict
l1=['a','b','c']
l2=['apple','ball','cat']
d=dict(zip(l1,l2))
print(d)

#Enumerate help to print Index, value
for i in enumerate(l1):
    print(i)

#Enumerate convert to dict
d=dict(enumerate(l1))
print(d)

#using range in loop and printing like Dict
d={x:x**2 for x in range(1,5)}
print(d)

#S={1,2,3}
#{} -->Set object is mutable by using many method to add the value
#1,2,3 -->set value is immuatable, can't edit it
'''


##------------------------------------------------28 MAR 25---------------------------------------------------------------------------------------

'''
##Metods of Dict
d={101:'apple', 102:'org', 103:'acc'}
print(d[101])
print(d.get(102))
#KeyError: 105
#print(d[105])
print(d.get(105))

for i in d:
    print(i)

for i in d:
    print(i,d[i])

print(d.keys())
print(d.values())
print(d.items())

for i, j in d.items():
    print(i,j)

d2=d.copy()
print(d2)

d.update({105:'sam', 106:'tham'})
print(d)

print(d.setdefault(102))
print(d.setdefault(107))

del d[107]
print(d)
 
print(d.setdefault(107,'AI'))
print(d)

del d[107]
print(d)
'''


'''
d={101:'apple', 102:'org', 103:'acc'}

l=[11,12,33,44]
d3={}

#TypeError: 'int' object is not iterable
#d3.fromkeys(1,100)
print(d3)

d.pop(103)
print(d)

#TypeError: pop expected at least 1 argument, got 0
#d.pop()
d.pop(102)
print(d)

d.clear()
print(d)
'''

'''
d={'HTML':'Notepad', 'c#':'vscode', 'python':['pycharm','jupyter'], 'java':{'javaEE':'eclipse','MobileAPP':'jetbrains'}}
print(d['c#'])
print(d['python'][0])
print(d['python'])
print(d['java']['javaEE'])
'''

'''
##FUCTION
def add3(a,b,c):
    r=a+b+c
    return r
m,n,o=5,6,7
#positional arguments
s=add3(m,n,o)
print(s)
print(type(s))
s2=add3(3.1,6,5)
print(s2)
print(type(s2))

#inside def is local space
#outside def is global space
def up(x):
    print(x, id(x))
    x=8
    print(x, id(x))
a=10
print('a1',a, id(a))
up(a)
print('a2',a, id(a))
'''


##------------------------------------------------31 MAR 25---------------------------------------------------------------------------------------

##FUNCTION(ARGUMENTS):

'''
#Positional Argument --> It copy
def sal(base, var, ded):
    net=base+var-ded
    return net
print(sal(1000,200,100))

#Key word argument
def sal(base, var, ded):
    net=base+var-ded
    return net
print(sal(1000,100,ded=300))

#key word argument --> within print using argument (ded= ,  var= )
def sal(base, var, ded):
    net=base+var-ded
    return net
print(sal(1000,ded=100,var=300))

#positional arguments follow key word argument 
def sal(base, var, ded):
    net=base+var-ded
    return net
print(sal(1000,ded=100,var=300))
#print(sal(base=1000,ded=100,300))

#positional arguments follow key word argument
def sal(base, var, ded):
    net=base+var-ded
    return net
#TypeError: sal() got multiple values for argument 'base'
#print(sal(1000,base=100,var=300))
'''

'''
##DEFAULT ARGUMET
def add(a,b=0,c=0):
    return a+b+c
print(add(4,5,6))
#TypeError: add() missing 1 required positional argument: 'c'
print(add(4,5))
#TypeError: add() missing 2 required positional arguments: 'b' and 'c'
print(add(4,5,6))

print(add(4,5))
print(add(4))

#default it follow with the non-default argument
'''


'''
def addI(item, L=[]):
    L.append(item)
    return L

#NameError: name 'L' is not defined -->Local & Global variable
#print(L)
L1=[1,2,3,4]
addI(5,L1)
print(L1)

#Once defint the argument outside the function then only it give output
L=[1,2,3]
addI(6,L)
print(L)

#Default arguments will define one time
print(addI(11))
#value is adding with the existing list
print(addI(21))
print(addI(31))
'''



'''
#Before / it mandatory to give positional Argument
#After / it might be positional or keyword Argument
def add(a,b,/,c,d,e,f):
    print(a+b+c+d+e+f)
add(1,2,3,4,5,6)
add(1,2,3,4,f=5,e=6)
#positional argument follow keyword Argument
#add(1,2,d=3,4,f=5,e=6)
add(1,2,c=3,d=4,f=5,e=6)
'''


'''
#Before / it mandatory to give positional Argument
#After / it might be positional or keyword Argument
#After * it should be keyword Argument
#Before * it might be positional or keyword Argument
def add(a,b,/,c,d,*,e,f):
    print(a+b+c+d+e+f)
add(1,2,3,4,e=5,f=6)
#TypeError: add() takes 4 positional arguments but 5 positional arguments (and 1 keyword-only argument) were given
#add(1,2,3,4,5,f=6)
add(1,2,3,d=4,f=6,e=7)
'''

'''
##VARIABLE LENGTH ARGUMENT -->Can add multiple value with one argument

# '*' define a = Variable length Argument

def fun1(*arg):
    print(arg)
fun1(1)
fun1(1,2,3)
fun1(9,8,6,45,4,3)
'''

'''
def fun1(m,n,*a):
    print(m,n,a)
#TypeError: fun1() missing 1 required positional argument: 'n'
#fun1(1)
    
fun1(1,2,3)
fun1(1,2,34,5,6)
fun1(1,2)
'''

'''
def fun2(a,b,c):
    print(a,b,c)
L=[11,22,33]
fun2(L[0],L[1],L[2])
#Unpack Argument -->It follow the Variable argument
fun2(*L)
'''

'''
def fun3(a,b,c):
    return a+1, b+1,c+1
m,n,o =fun3(4,5,6)
print(m,n,o)

#Packing Argument -->All the value its stored in the one variable
g=fun3(4,1,2)
print(g)
'''

'''
##KEYWORD VARIABLE LENGTH ARGUMENT --> Instead of positional, We passing Keyword Argument

def fun1(**kargs):
    print(kargs)
    print(kargs['roll'])
    
fun1(name='Tham', roll=40)


def fun2(a,b,*arg,**kargs):
    print(a,b,arg,kargs) 
    
fun2(10,20,1,2,3,name='Tham', roll=40)
#positional arguments follow with keyword argument
#fun2(a=10,20,1,2,3,name='Tham', roll=40)

def fun3(a,b,c):
    print(a,b,c)
s='sku'
fun2(*s)

'''

##------------------------------------------------01 APR 25---------------------------------------------------------------------------------------

###(generator,decorator,iterator) ->it save time and space instead of use for or while loop

'''
#ITERATION -->Each iteration is calling loop one by one
l=[11,22,33]
itr=iter(l)
print(next(itr))
print(next(itr))
print(next(itr))
#StopIteration
#print(next(itr))
'''

'''
#GENERATOR -->'Yield' is important for generator
def name():
    n=['ram','sam','mam']
    i=0
    #while true -->run infinite / continue loop infinite time
    while True:
        x=n[i]
        i=(i+1)%3
        yield x

d=name()
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))

#Return -->whatever the statement after the return it won't execute also once the return is triggered after the statement, it come out from the statement or loop.



def topten():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1
values=topten()
for i in values:
    print(i)
'''   

'''
#RECURTION FUNCTION -->Function is calling by itself

#It give the infinite output -> till 1000 times.
def greet():
    print('hi')
    greet()
greet()
'''


'''
#FACTORIAL -->5*4*3*2*1 -- Also we can use for loop

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
print(fact(4))
'''



'''
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

print(fact(4))
#4*f(3)-6 -->24,3*f(2)-2 -->6,2*f(1)-1 -->2,1*f(0)-1 -->1

#STACK DSA --> Last in 1st out, RECURTION is follow the stack Data Structure.

#Take a Recurtion code and debug it, spend more time on recurtion, it vary important concept of recurtion.

'''


'''
#DECORATOR

def div(a,b):
    print(a/b)
div(4,2)
div(2,4)



def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

div1=smart_div(div)
div1(2,4)
div1(6,3)
'''

'''
##LOCAL & GLOBAL VARIABLE:

a=10
def some():
    a=9
    print(a)
    print(id(a), end='\n\n')
some()
print(a)
print(id(a), end='\n\n')


#Global variable changing to the local variable
a=10
def some():
    global a
    a=9
    print(a)
    print(id(a), end='\n\n')
some()
print(a)
print(id(a), end='\n\n')

a=10
b=6
def some():
    global a
    global b
    #a=9
    print(a,b)
    print(id(a,b), end='\n\n')
some()
print(a,b)
print(id(a,b), end='\n\n')

'''

##------------------------------------------------02 APR 25---------------------------------------------------------------------------------------

'''
#LOCAL-use to access with one value of the variable
#GLOBAL-use to access all the value of the variable in global section

a,b,c,d=10,20,30,40
def func1 (a=15, b=25):
    x,y,z=1,2,3
    print(locals())
func1()
print(globals())
print(globals()['b'])
'''

'''
##LAMDA FUNCTION 1 Expression or 1 Statement

#Normal Function
def km2mil (miles):
    kms=1.6*miles
    return kms
print(km2mil(10))

#Lambda Function
k=lambda miles:1.6*miles
print(k(10))


f=lambda a,b:a+b
print(f(2,3)) 

g=lambda a,b: a if a>b else b
print(g(1,2))
'''


##EXCEPTION HANDLING -->Handling the Errors, It changes the flow of Execution, Its like Conditional statement.

#Syntex Error - Mistake in syntak of the code
#Logical Error - Expectation output can't get bcz we given worng input.
#Runtime Error - Error occur while running the code
#Type Error, Key Error, Value Error

'''
l=[10,20,30]
i=int(input('Enter index'))
print(l[i])
'''

'''
## TRY & EXCEPTIONAL HANDLING:

#How many Try block we using, That many times except block need to create.

l=[10,20,30]
try:
    i=int(input('Enter No:'))
    print(l[i])
    print('End Try block')
except:
    print('Invalid Index')
print('End')
'''

'''
l=[10,20,30]
try:
    i=int(input('Enter No:'))
    print(l[i])
    print('End Try block')
except IndexError:
    print('Invalid Index')
except ValueError:
    print('Invalid Value')
print('End')
'''

'''
l=[10,20,30]
try:
    i=int(input('Enter No:'))
    print(l[i])
    print('End Try block')
except (IndexError,ValueError) as msg:
    print(msg)
print('End')
'''

'''
#If 'Try' block is satisfied, the 'else' block also execute
#If 'Try' block is not satisfied, it will go to 'except' block but not execute 'else' block
l=[10,20,30]
try:
     a=int(input('Enter No1:'))
     b=int(input('Enter No2:'))
     c=a/b
     print('Try success')
except ZeroDivisionError as msg:
    print(msg)

else:
    print('Division',c)
print('End')
'''
'''
#FINALLY is help to once the job is done it help to close it / close the connetion.
l=[10,20,30]
try:
     a=int(input('Enter No1:'))
     b=int(input('Enter No2:'))
     c=a/b
     print('Try success')
except ZeroDivisionError as msg:
    print(msg)

else:
    print('Division',c)
finally:
print('End')
'''

##------------------------------------------------03 APR 25---------------------------------------------------------------------------------------



##------------------------------------------------07 APR 25---------------------------------------------------------------------------------------


## MODULE

import sim
print(sim.add(5,2))

















































































































































































