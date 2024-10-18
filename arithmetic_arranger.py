i = input('Enter :')
x,y,z = i.split(',')
a,b,c = i.split()
print(' ',a)
print(b,c)
if b == '+' :
    total = a+c
    print (' ',total)
if b == '-' :
    total = a-c
    print (' ',total)
if b == '*' :
    total = a*c
    print (' ',total)
if b == '/' :
    total = a/c
    print (' ',total)
