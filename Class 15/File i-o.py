# with open("test.txt", "w+") as fh:
#     a = """AATCGCGTAGCTAGCATCGACTAGCATCGACTAGCTAC
# ATCGCGCTAGCTAGCTAGCTAGCGACGATCGAGCAGCTACG
# ACTGTCAGCTAGCATCGACTAGCTACGATCAGCTACGACT
# ACTAGGCTAGACTAGCATCGACTAGCACGTACGACT"""
#     fh.write(a)
#
#
# with open('test.txt', 'r') as fh:
#     for c in fh.read():
#         print c


with open('test.txt','r') as fh:
    a = fh.read()
    print "length = ",len(a)

    print "A = ", a.count("A")
    print "T = ", a.count("T")
    print "G = ", a.count("G")
    print "C = ", a.count("C")

#
# nums = []
# sum = 0
# with open('test2.txt','r') as fh:
#     line = fh.readline()
#     snums = line.split(" ")
#     for i in snums:
#         j = float(i)
#         nums.append(j)
#     for i in nums:
#         sum +=i
#
# print sum

# sum = 0
# with open('test3.txt','r') as fh:
#     lines = fh.readlines()
#     for i in lines:
#         snums = i.split(" ")
#         for j in snums:
#             sum += int(j)
# print sum