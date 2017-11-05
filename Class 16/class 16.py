#015.11.17

#printing hello
# def fh():
#     print "hello"
#
# fh()

#length function
# def length(s):
#     c = 0
#     for i in s:
#         c+=1
#     return c
# a= 'ATCGGTACG'
# print length(a)

#odd or even
# def chk(num):
#     if num%2==0:
#         return True
#     else:
#         return False
#
# print chk(20)
# print chk(51)
# print chk(-1)
# print chk(0)

#base count
def base_count(seq):
    seq = seq.upper()
    A = seq.count("A")
    C = seq.count("C")
    G = seq.count("G")
    T = seq.count("T")

    return A,T,G,C

seq = "ATCGATCGACTAGCTAGCTACGAT"
a,t,g,c = base_count(seq)
print a
print t
print g
print c

