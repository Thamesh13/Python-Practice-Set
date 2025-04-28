a=int(input('Enter the a value:'))
b=int(input('Enter the b value:'))
if a>b:
    print('a is the greatest')
else:
    print('b is greatest')

c=input('Enter a charecter:')
if c in 'a,e,i,o,u':
    print('Its vowles')
else:
    print('Its not')

x=input('Enter a gender:')
if x=='m':
    print('Male')
elif x=='y':
    print('Female')
else:
    print('gender invalid')

y=int(input('Enter a amount:'))
if y<500:
    d=y*10/100
elif y>=500 and y<1000:
    d=y*20/100
elif y>=1000 and y<1500:
    d=y*30/100
else:
    d="not valid"
print('Ans:' ,d)

l=int(input('Enter the l value:'))
match l:
    case _ if l<10:
        print('lower')
    case _ if l>=10:
        print('Normal')
    case _ if l<20:
        print('ok')
    case _ if l>20:
        print('Excellent')

    


