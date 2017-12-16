#Trivial

#5 cpu time
import time
start = time.time()
#program
for i in range(100000):
    pass
end =time.time()

print "time", (end-start)


#6 random mutation
import random
seq = "ATGCATTGCATCGATCAACGTA"
bases = 'ATGC'
point = random.randint(0,len(seq))
mutation = random.choice(bases)
newseq = seq[:point] + mutation + seq[point+1:]
print newseq
