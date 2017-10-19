
#a is greater or less
a = input("input a number: ")
if a>0:
    print "a is greater than zero"
else:
    print "a is less than zero"
    
#v2 a is greater or less
a = input("input a number: ")
if a>0:
    print "%d is greater than zero"%a
else:
    print "%d is less than zero"%a


#v3 a is greater or less
a = input("input a number: ")
if a>0:
    print "%.2f is greater than zero"%a
else:
    print "%.2f is less than zero"%a


#a+b is greater or less
a = input("input a number: ")
b = input("input another number: ")
if (a+b)>0:
    print "%d + %d is greater than zero"%(a,b) #(a+b) is a tuple
else:
    print "%d + %d is less than zero"%(a,b)

#v2 a+b is greater or less
a = input("input a number: ")
b = input("input another number: ")
if (a+b)>0:
    print "%d + %d = %d is greater than zero"%(a,b, (a+b)) #(a+b) is a tuple
else:
    print "%d + %d = %d is less than zero"%(a,b, (a+b))

#odd or even
b = input("input a number: ")
if b%2 == 0:
    print "%d is even"%b
else:
    print "%d is odd"%b

#positive,, negative or zero
b = input("input a number:")
if b > 0:
    print "psitive"
elif b < 0:
    print "negative"
else:
    print "zero"

