#find the cg content
seq = "AACGTT"
total_length = len(seq)
g = seq.count("G")
c = seq.count("C")
gc = (( c + g ) / float(total_length) ) * 100
print "The GC content of the sequence: ",gc,"%"