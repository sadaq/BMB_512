
#generation of all codon of length 2
bases = "ATGC"

for i in bases:
	for j in bases:
		print i+j,
	print ""
	
#find the 2 base length codons of a sequence

seq = "ATACGAAT"

n = len(seq)
i = 0
while i<n:
	print s[i]
	i+=1

m = 0
o = len(seq)
i = 0
while i<o:
	print seq[m:(m+2)]
	m+=2
	i+=2

m = 0
o = len(seq)
i = 0
while i<o-1:
	print seq[m:(m+2)]
	m+=1
	i+=1

#add 10 to all the items of a list
#v1
list = [80, 45, 90, 71, 62, 59, 11]
j = 0
for i in list:
	list[j] = i+10
	j+=1
print list

#v2
n = len(list)
i = 0
while i<n:
	list[i]+=10
	i+=1
print list

for i in range(0, len(list)):
	list[i]+=10
print list

#Dictionary

names = {'A': "Adenine", 'T': "Thymine", 'G' : "Guanine", 'C' : "Cytosine"}

s = 'ATACCGTT'
for i in s:
	print names[i]



