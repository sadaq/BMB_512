# Biopython
#1
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

my_seq = Seq('GATCGATGGGCCTATATAGGATCGAAAATCGC', IUPAC.unambiguous_dna)
gc = 100 * float(my_seq.count("G") + my_seq.count("C") ) / len (my_seq)
print("GC = ", gc)


#2 reverse complement
from Bio.Seq import Seq
my_seq = Seq("ATCGACGCATGCAGACT")
reverse_complement = my_seq.reverse_complement()
print reverse_complement


#3 translate
from Bio.Seq import Seq
my_seq = Seq("ATCGACGCATGCAGACTA")
translation0 = my_seq.translate()
print translation0


#4 parse fasta
from Bio import SeqIO
for seq_record in SeqIO.parse("04.fasta", 'fasta'):
    print seq_record.id
    print seq_record.seq
    print len(seq_record)


#5 parse genbank
from Bio import SeqIO
for seq_record in SeqIO.parse("05.gbk",'genbank'):
    print seq_record.id
    print seq_record.seq
    print len(seq_record)



#6
#same as no. 2


#7

#8
from Bio import SeqIO
from Bio import pairwise2
seq1 = "MMYQQGCFAGGTVLRLAKDLAENNRGARVLWCSEITAVTFRGPSETHLDSMVGQALFGD"
seq2 = "YPDYYFRITNREHKAELKEKFQRMCDKSMIKKRYMYLTEEILKENPSMCEYMAPSLDARQ"
alignments = pairwise2.align.globalxx(seq1,seq2)
print "length: ",len(alignments)
print alignments[0]

#9
from Bio import AlignIO
alignment = AlignIO.read("myalingn.fasta", 'fasta')
print(alignment)
