
#01 area of a rectangle
h = input("Input the height: ")
w = input("Input the width: ")
A = h*w
print "Area of the rectangle: %d"%A

#02 area of a circle
r = input("Input the raius: ")
pi = 3.14
A = pi*r**2
print "Area of the circle: %.2f"%A

#03 area of a triangle
b = input("Input the base: ")
h = input("Input the height: ")
A = .5*b*h
print "Area of the triangle: %.2f"%A

#04 volume of a box
h = input("Input the height: ")
w = input("Input the width: ")
d = input("Input the depth: ")
V= h*w*d
print "Volume of the box: %.2f"%V

#05 Square of a hypotenuse
a= input()
b= input()
h_sqr = a**2 + b**2
print h_sqr

#06 Find the root
a= input()
b= input()
c= input()
x1 = (-b+(b**2-4*a*c)**.5)/2*a
x2 = (-b-(b**2-4*a*c)**.5)/2*a
print "x1 =", x1, " x2 =",x2


#07 print hello Name
name = raw_input("Input your name: ")
print "Hello", name


#08 4 random numbers
import random
for i in range(0,4):
    print random.random(),",",

#09 print pi 12 digits
from math import pi
print "%.12f"%pi

#10 payment amount
price = 450
vat = 15/100
s_charge = 10.25/100
price_vat = price + price*vat
total = price_vat + price_vat*s_charge
print "You have to pay:", total

#11 Count the frequency of "ATGC"
seq = raw_input("Input the nucleotide sequence: ")
seq = seq.upper()
A = seq.count("A")
T = seq.count("T")
G = seq.count("G")
C = seq.count("C")
U = seq.count("U")
print "A:",A,",T:",T,",G:",G,",C:",C,",U:",U

#12 Calculate GC content

seq = raw_input("Input the nucleotide sequence: ")
seq = seq.upper()
total = len(seq)
G = seq.count("G")
C = seq.count("C")
GC = (G+C)*100/total
print "GC content:", GC ,"%"


#13 Mutation in random position
import random

seq = raw_input("Input the original sequence: ")
seq = seq.upper()
l = len(seq)
n = random.randint(0,l)
mutation = random.choice("ATGC")
while mutation == seq[n]:
    mutation = random.choice("ATGC")
    continue
new = seq[:n] + mutation + seq[(n+1):]
print "Random mutation at %dth position"%(n+1)
print new

#14 positive, negative or zero
i = input('Input the number: ')
if i>0:
    print "Positive"
elif i<0:
    print "Negative"
else:
    print "Zero"


#15 Even or Odd
i = input("Input the number: ")
if i%2==0:
    print "Even"
else:
    print "Odd"

#16 Assign letter grade
mark = input("Input the mark: ")
if mark >=90:
    print "A"
elif mark >=80:
    print "B"
elif mark >=70:
    print "C"
elif mark >=60:
    print "D"
elif mark >=50:
    print "E"
else:
    print "F"


#17 Male/Female & age group
age = input("Input your age: ")
gender = raw_input("Input your gender(M/F): ")
gender = gender.upper()
if gender == "M":
    print "He is a",
else:
    print "She is a",
    
if age in range(0,11):
    print "Child"
elif age in range(11,18):
    print "Teenager"
elif age in range(18,26):
    print "Young adult"
elif age in range(26,36):
    print "Adult"
elif age in range(36,56):
    print "Middle aged"
elif age in range(56,120):
    print "Senior"

#18 Print color
color = raw_input("Input the first letter of the color: ")
color = color.upper()
if color == "R":
    print "Red"
elif color == "O":
    print "Orange"
elif color == "Y":
    print "Yellow"
elif color == "G":
    print "Green"
elif color == "B":
    print "Blue"
elif color == "I":
    print "Indigo"
elif color == "V":
    print "Violet"


#19 Print "ATGC
l = raw_input("Input a letter: ")
l = l.upper()
if l == 'A':
    print "Adenine"
elif l == 'T':
    print "Thymine"
elif l == 'G':
    print "Guanine"
elif l == 'C':
    print "Cytosine"
elif l == 'U':
    print "Uracil"
else:
    print "Unknown"


#20 Age restriction
age = input("Input your age: ")
if age>=0 and age<=12:
    print "Can only watch PG rated movies"
elif age>=13 and age<=17:
    print "Can watch PG-13 rated movies"
elif age>=18:
    print "Can watch R rated movies"


#21 Check leap year
y = input("Input the year: ")
if y%400 == 0:
    print "Leap year"
elif y%100 ==0:
    print "Not Leap year"
elif y%4 == 0:
    print "Leap year"
else:
    print "Not Leap year"

