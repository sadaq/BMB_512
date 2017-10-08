'''
#Dictonary Practice

names = {'A':"Adenine",'C':"Cytosine",'G':"Guanine",'T':"Thymine",'U':"Urcile"}
print names['A']
#Update
namess['U'] = "Others"
#Delete
del names['U']
#Find key
names.key()

#Find values
names.values()

#Find items/pairs
names.items()


'''
#Reverse complement
s = "ATACCA"        ##input sequence

s1 = s[::-1]        ##Reverse the sequence
s2 = ''

for i in s1:        ##Access every base
    if i == "A":    ##Check every base
        i = "T"     ##Change every base
        s2+=i       ##Add to new string
    elif i == "T":
        i = "A"
        s2+=i
    elif i == "G":
        i = "C"
        s2+=i
    elif i == "C":
        i = "G"
        s2+=i

print s2            ##Print complement

#Reverse complement using dictionary

s = 'ATACCA'
r = s[::-1]
c = ''
cd ={'A':"T", 'T':"A", 'G':"C", 'C':"G"}
for b in r:
    c+=cd[b]

print c


