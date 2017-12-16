# FIles
#2
seq = ''
with open("01.fasta", 'r') as fh:
    lines0 = fh.readlines()
    for line in lines0:
        if not line.startswith(">"):
            seq+= line
            print line
#3
def GC(seq):
    seq = seq.upper()
    total = float(len(seq))
    G = seq.count('G')
    C = seq.count('C')
    gc = ((G+C)*100)/total
    return gc
with open("02.fasta", 'r') as fh:
    with open("02result.fasta", "w") as fh2:
        lines0 = fh.readlines()
        for line in lines0:
            if line.startswith(">"):
                id = line
                fh2.write(id)
            else:
                seq = line
                seq = seq.strip()
                gc = str(GC(seq))
                fh2.write(gc)
                fh2.write("\n")

#4
with open('input.txt', 'r') as fh:
    with open('output.txt', 'w') as fh2:
        numlist = fh.read().split("\n")
        sum = 0
        for i in numlist:
            i = int(i)
            if i >= 0 and i%2 == 0:
                sum+=i
        sum = str(sum)
        fh2.write(sum)
#5



#6

#7

#8
from Bio import Phylo
tree = Phylo.read("simple.dnd", "newick")
print(tree)
Phylo.draw_ascii(tree)


