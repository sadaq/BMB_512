#collection
#2

mylist = ['a','b','c','d']

for i in mylist:
    print mylist.index(i), i

#3
adict = {"a": 'apple', "b": 'ball'}
print adict
#insertion
adict["c"]= 'coil'
print adict
#deletion
adict.pop("b")
print adict
'''or 
del adict[b]
'''
print adict
# searching
print adict["a"]
#or
print adict.get("a")
print adict

