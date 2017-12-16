#collection
#2

mylist = ['a','b','c','d']

for i in mylist:
    print mylist.index(i), i

#3
adict = {"a": 'apple', "b": 'ball'}
print adict
#insertion
adict["c"]= 'coil'
print adict
#deletion
adict.pop("b")
print adict
'''or 
del adict[b]
'''
print adict
# searching
adict["a"]
#or
adict.get("a")
print adict

#Strings
#1
a = 'ACGT'
b = 'CAT'

final = ''

for i in a:
    final += (i+b)
print final

#2

bla = "bla"
print bla*5

#3
seq = 'TACACGCTA' +'GATTTA'
print seq[:3:-1]
#output = "ATTTAGATCGC"

#4
s1 = "abcd"
s2 = "efgh"
combine = s1+s2


#functions
#1 GC content
def GC(seq):
    seq = seq.upper()
    total = float(len(seq))
    G = seq.count('G')
    C = seq.count('C')
    gc = ((G+C)*100)/total
    return gc
seq = 'ATGCATGCATGCATGCAT'
print GC(seq),'%'


#2
def occur(dna, pattern):
    number = dna.count(pattern)
    return number
seq = "ATCCTGCTATCCATCTAT"
pat = "ATC"

print occur(seq, pat)


#3
def basecount(seq):
    A = seq.count("A")
    T = seq.count("T")
    G = seq.count("G")
    C = seq.count("C")
    return A, T, G, C
seq = "ATCGTGCTAGCTCGATCGCT"
A, T, G, C = basecount(seq)
print A, T, G, C



#Control Statement


#3 odd total
n = 10
total = 0
for i in range(1,n+1):
    if i%2 !=0:
        total+= i
print total

#4 even total
n = 10
total = 0
for i in range(0,n+1):
    if i%2 ==0:
        total+= i
print total

#5
seq = 'ATCGTAGCTAG'
length = 0
for i in seq:
    length += 1
print length

#6
#same as 5

#7
s1 = "ATGCATGC"
s2 = "ATGCATGC"

for i in s1:
    for j in s2:
        if i == j:
            print "*",
        else:
            print ".",
    print""

#8 Random nucleotide sequence
import random
N = 7
bases = 'ATGC'
finalseq = ''
for i in range(N):
    tem = random.choice(bases)
    finalseq += tem
print finalseq

#9
import random
N = 15
aa = 'ARNDBCEQZGHILKMFPSTWYV'
pseq = ''
for i in range(N):
    tem = random.choice(aa)
    pseq += tem
print pseq

#10






