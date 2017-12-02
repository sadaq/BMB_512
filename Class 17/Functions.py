# def GC(seq):
#     seq = seq.upper()
#     length = float(len(seq))
#     G = float(seq.count("G"))
#     C = float(seq.count("C"))
#     GC_con = (G+C)*100/length
#     return GC_con


# def occur(dna, pattern):
#     number = dna.count(pattern)
#     return number
#
# print occur('ATCCTGCTATCCATCTAT', 'ATC')

def counting(seq):
    seq = seq.upper()
    A = seq.count("A")
    T = seq.count("T")
    G = seq.count("G")
    C = seq.count("C")
    return A, T, G, C
