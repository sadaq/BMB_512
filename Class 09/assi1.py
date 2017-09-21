#06 Find the root
import math
a= input("input a: ")
b= input("input b: ")
c= input("input c: ")
d = b**2-4*a*c
if d>=0:
    e = math.sqrt(d)
    x1 = (-b+e)/2*a
    x2 = (-b-e)/2*a
    print "x1 =", x1,', ' " x2 =",x2
else:
    d = -d
    e = math.sqrt(d)
    x = (-b/2*a)
    y = (e/2*a)
    print "x1= %.2f + %.2fi "%(x,y), ",", "x1= %.2f - %.2fi "%(x,y)

    
    

