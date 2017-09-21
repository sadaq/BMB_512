import random
seq = raw_input("Input the original sequence: ")
seq = seq.upper()
l = len(seq)
n = random.randint(0,l)
print n
mutation = random.choice("ATGC")
new = seq.replace(seq[n-1], mutation)
print new
