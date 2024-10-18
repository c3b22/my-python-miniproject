import math
import cmath
from fractions import Fraction
print ('if you have have  fraction paste 1')
print ('if not paste 0')
p = 1
while p == 1 :
    p = int(input('Choose!'))
    if p == 1 :
        a1 = int(input('upper fraction :'))
        a2 = int(input('down fraction :'))
        a3 = Fraction(a1,a2)
        print (float (a3))
print ('-----------------find square------------------')
a = 1
while a == 1 :
    print ('(ax^2) + bx + c')
    print ('you want to exit chooose a = 0')
    a = float(input('ax^2;a = '))
    if a != 0 :
        b = float(input('bx;b = '))
        c = float(input('c = '))
        fs1 = (b**2)-4*a*c
        fs2 = (b**2)-4*a*c
        fs3 = -b + math.sqrt(fs1)
        fs4 = fs3 /2*a
        fs5 = -b - math.sqrt(fs1)
        fs6 = fs5 /2*a
        print (fs3,',',fs5)
        print ('(-b+((b^2)-4ac)^1/2))/2a','=',fs4)
        print ('(-b-((b^2)-4ac)^1/2))/2a','=',fs6)
        if fs4 < 0 :
            if fs6 < 0 :
                print ('(x',fs4,')(x',fs6,')')
            if fs6 >= 0 :
                print ('(x',fs4,')(x +',fs6,')')
        else :
            if fs6 < 0 :
                print ('(x +',fs4,')(x',fs6,')')
            if fs6 >= 0 :
                print ('(x +',fs4,')(x +',fs6,')')
    print ('--------------------end-----------------------')
