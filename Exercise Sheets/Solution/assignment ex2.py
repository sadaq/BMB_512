
#2.1
a = " to be or not to be "
a_r = a.strip()
print a_r

#2.2
print len(a_r)

#2.3
last2 = a_r[-2:]
print last2

#2.4
a_rnew1 = a_r.replace("be", "it")
print a_rnew1

a_rnew2 = a_r[:-2] + 'it'
print a_rnew2

#2.5
a = " to be or not to be "
a_rp = a.replace("to be", "two beer")
print a_rp

#2.6

print a_r.startswith('to')

#2.7
li = [1, 2, 3]
print li[2]
print li[-1]
print li[0:2]
print li[-2:]


#2.8
li = [1, 2, 3]
li.append(5)
print li

#2.9
li2 = li + [6, 7, 8]
print li2
li.extend([6, 7, 8])
print li

#2.10
x = 1
y = 2
x,y = y,x
print x,y

#2.11
def eval(x):
    if x > 100:
        print 'big'
    else:
        print 'small'
a = input("input the number: ")
eval(a)

#2.12
money =[100, 200, 20, 50, 1, 10, 2, 5, 500]
#1
for i in money:
    print i
#2
for i in money:
    if i>20:
        print i
#3
for i in sorted(money, reverse = True):
    print i



#2.13

x = input("input a positive number:" )
while x>1:

    if x%2 == 0:
        x= x/2
        print x, ",",
        continue
    else:
        x = x*3+1
        print x, ",",
        continue

