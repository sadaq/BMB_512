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

#10 find point mutation
s1 = "ATGCATGC"
s2 = "TTGCATTC"

for i in range(len(s1)):
    if s1[i] != s2[i]:
        print i+1,

#ignore this print
print ''
#11

bases = "ATGC"

for i in bases:
    for j in bases:
        for k in bases:
            print i+j+k,
        print ''
    print ''

#12 consensus sequence




#13 all the k-mers
k = 3
seq = 'ATGCGTAGC'
kmer = []
a = 0
for i in range(len(seq)):
    mer = seq[a:a+k]
    kmer.append(mer)
    a+=1
for i in kmer:
    if len(i)==k:
        print i,

#igonre this
print''
#14 digest a protein
dp = 'I'
seq = 'MRHIAHTQRCLSRLTSLVALLLIVLPMVFSPAHSCGPGRGLGRHRARNLYPLVLKQTIPNLSEYTNSASGPLEGVIRRDSPKFKDLVPNYN RDI LFRDEE'
peptides = seq.split(dp)

print peptides

#15 align two sequences


#16 ORF
start = "AUG"
end = "UAG"
seq ='AGCAUGAAUGCAUGCACCACGAAAUAGUUAGGAUCG'
s = seq.find(start)
list0 = []
a = "AAA"
while a!= end:
    if len(a) == 3:
        a = seq[s:s+3]
        list0.append(a)
        s+=3
orf =''
for i in list0:
    orf+=i
print orf

#17 longest ORF




