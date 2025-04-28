'''
n=int(input('ENter Num'))
if n%2==0 and range(2,5):
    print('Not weird')
elif n%2==0 and range(6,20):
    print('Weird')
elif n%2==0 and n>20:
    print('Not Weird')
else:
    print('Weird')
'''

'''
a=int(input('Enter value a:'))
b=int(input('Enter value b:'))
print(a+b)
print(a-b)
print(a*b)
'''

'''
a=int(input('Enter value a:'))
b=int(input('Enter value b:'))
if 1<=a<=10**10 and 1<=b<=10**10:
    print(a+b)
    print(a-b)
    print(a*b)
'''
'''
a=int(input('Enter value a:'))
b=int(input('Enter value b:'))
print('{}\n{}\n{}'. format(a+b, a-b, a*b))
'''

'''
##O OUTPUT:
a=int(input('Enter value a:'))
b=int(input('Enter value b:'))
for i in "+-*":
    print(eval(a,i,b))
'''

'''
a=int(input('Enter value a:'))
b=int(input('Enter value b:'))
Sum=a+b
Difference=a-b
Product=a*b
print(Sum,Difference,Product, sep=' ')
'''
'''
a=int(input('Enter value a:'))
b=int(input('Enter value b:'))
Sum=a+b
Difference=a-b
Product=a*b
print(Sum,Difference,Product, sep='\n')
'''

'''
a=int(input('Enter value a:'))
b=int(input('Enter value b:'))
print(f'{a+b}\n{a-b}\n{a*b}')
'''

'''
##NOT SOLVE
sub1=int(input('Sub1:'))
sub2=int(input('Sub2:'))
sub3=int(input('Sub3:'))
sub4=int(input('Sub4:'))
sub5=int(input('Sub5:'))
sub=sub1,sub2,sub3,sub4,sub5
for i in sub:
    if i<=40:
        print('YEARLAG')
    else:
        print('CAZZ')
'''

'''
##Find the sum of all the multiple of 3 or 5 below N.
n=int(input('Enter Num:'))
m=[]
for i in range(1,n):
    if i%3==0 or i%5==0:
        m.append(i)
        
print(sum(m))
'''
'''
##To calculate area of rectangle given its length and width.
length=int(input('Enter Length:'))
width=int(input('Enter width:'))
a=length*width
print(a)
'''

'''
##Take User Name & Age as a input and print a greeting Message
Name=input('Enter Name:')
Age=int(input('Enter Age:'))
print(f'He is {Name} and he is {Age}')
'''

'''
##Check if a number is even or odd.
n=int(input('Enter Number:'))
if n%2 !=0:
    print('odd')
else:
    print('even')
'''

'''
##List of Numbers, find the Max and Min values:
n=[1,5,20,40,15]
print(min(n))
print(max(n))
'''

'''
##Check if a given string is Polindrome or not:
x=input('Enter String:')
if x==x[::-1]:
    print('Palindrome')
else:
    print('Not Palindrome')
'''
