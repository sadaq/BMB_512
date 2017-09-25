'''
#add only the positive numbers
#count the positive numbers from a list
#average of the numbers 
number = [2, 3, -34, -75, -400, -720, -4]
p_sum = 0
c = 0
for i in number:
	if i>0:
		p_sum+=i
		c+=1
print "%d positive numbers"%c
print "summation: ",p_sum
print "average: %.2f"%(float(p_sum)/c)

#count the GC content
seq = raw_input("insert the sequence: ")
seq = seq.upper()
A = seq.count("A")
T = seq.count("T")
G = seq.count("G")
C = seq.count("C")
total = len(seq)
print "A:%d, T:%d, G:%d, C:%d "%(A,T,G,C)
print "GC content: %.2f"%(float(G+C)*100/total), "%"

#count GC content of several sequences
seq= ['ATACTGCA', 'AAACGT', 'ACCCTAA', 'CCAATTA', 'AAATGA']
for i in seq:
	print "The sequence:",i
	G = i.count("G")
	C = i.count("C")
	total = len(i)
	print "GC content: %.2f"%(float(G+C)*100/total), "%"

def GC(seq):
	seq = seq.upper()
	G = seq.count("G")
	C = seq.count("C")
	total = len(seq)
	print "GC content: %.2f"%(float(G+C)*100/total), "%"
Sequences= ['ATACTGCA', 'AAACGT', 'ACCCTAA', 'CCAATTA', 'AAATGA']
for i in Sequences:
	GC(i)
#Input one number for several times. (untill user wants)
a = 1
while a!=0:
	a = input('a=')
	print 'Our input =%d'%a
print 'END'

#Input one number for specific times
times = input("How many times do you want to do the work?:")
a= 0
while times >a:
	inp = input("input number: ")
	a+=1
print "END"

times = input("How many times do you want to do the work?:")
a= 0
list = []
while times >a:
	inp = input("input number: ")
	a+=1
	list.append(inp)
total = 0
for i in list:
	total+=i
print "END"

# 10 random numbers
import random
c = 0
while c <10:
	a =random.random()
	print "number: ",a
	c+=1
'''
# problem ex sheet2.13
x = input("input a positive number:" )
while x>=1:
    if x%2 == 0:
        x= x/2
    else:
        x = x*3+1
    print x, ",",
    continue








