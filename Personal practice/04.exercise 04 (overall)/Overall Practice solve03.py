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



