# FIles
#2
with open("01.fasta", 'r') as fh:
    lines0 = fh.readlines()
    for line in lines0:
        if not line.startswith(">"):
            seq = line
            print line
#3 GC count
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
with open('03.fasta', 'r') as fh:
    with open('03output.txt', 'w')as fh2:
        lines0 = fh.readlines()
        for line in lines0:
            fseq= ''
            if line.startswith(">"):
                id = line
                id = id.strip()
                fh2.write("\n"+id+"\n")
            else:
                seq= line
                seq = seq.strip()
                fseq += seq
            fh2.write(fseq)

#6
import csv

data = []
with open('csvfile.csv','r') as csvf:
    with open('csvoutput.txt', 'w') as csvo:
        csvreader = csv.reader(csvf)
        for row in csvreader:
            data.append(row)
        print data
        csvwriter = csv.writer(csvo)
        for row in data:
            csvwriter.writerow(row[:5])


#7
from xml.etree import ElementTree as et

with open('xmlfile.xml', 'r') as xmlf:
    tree = et.parse(xmlf)

    for entry in tree.iter():
        print entry.tag, entry.attrib, entry.text


#8
from Bio import Phylo
tree = Phylo.read("simple.dnd", "newick")
print(tree)
Phylo.draw_ascii(tree)


