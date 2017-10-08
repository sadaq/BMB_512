RNAcodon = {'UUU':"F", 'UUC':"F", 'UUA':"L", 'UUG':"L",
            'UCU':"S", 'UCC':"S", 'UCA':"S", 'UCG':"S",
            'UAU':"Y", 'UAC':"Y", 'UAA':"X", 'UAG':"X",
            'UGU':"C", 'UGC':"C", 'UGA':"X", 'UGG':"W",
            'CUU':"L", 'CUC':"L", 'CUA':"L", 'CUG':"L",
            'CCU':"P", 'CCC':"P", 'CCA':"P", 'CCG':"P",
            'CAU':"H", 'CAC':"H", 'CAA':"Q", 'CAG':"Q",
            'CGU':"R", 'CGC':"R", 'CGA':"R", 'CGG':"R",
            'AUU':"I", 'AUC':"I", 'AUA':"I", 'AUG':"M",
            'ACU':"T", 'ACC':"T", 'ACA':"T", 'ACG':"T",
            'AAU':"N", 'AAC':"N", 'AAA':"K", 'AAG':"K",
            'AGU':"S", 'AGC':"S", 'AGA':"R", 'AGG':"R",
            'GUU':"V", 'GUC':"V", 'GUA':"V", 'GUG':"V",
            'GCU':"A", 'GCC':"A", 'GCA':"A", 'GCG':"A",
            'GAU':"D", 'GAC':"D", 'GAA':"E", 'GAG':"E",
            'GGU':"G", 'GGC':"G", 'GGA':"G", 'GGG':"G"}
seq = raw_input("Insert the sequence(DNA/RNA):" )

if seq.find("T") != -1:
    RNA = seq.replace('T',"U")
else:
    RNA = seq
c1 = len(RNA)
if c1%3 !=0:
    c1-= (c1%3)
c2 = 0
c3 = 0
Pseq = ''
while c2<c1:
    codon = RNA[c3:c3+3]
    Pseq += RNAcodon[codon]
    c3+=3
    c2+=3

print "The protein sequence: ",Pseq