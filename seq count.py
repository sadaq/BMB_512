seq = raw_input("input the sequence: ")
seq = seq.lower()
base = "atgc"
n = 0
for j in base:
    for i in seq:
        if i == j:
            n += 1
    print j, "= ", n        
    n = 0

        
    
