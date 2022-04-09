myset = {"apple", "banana", "cherry"}

print(type(myset))
print(myset)
# print(myset[0])

for i in myset:
    print(i)

myset.add("pepaya")
for i in myset:
    print(i)
    
myset.remove("banana")
for i in myset:
    print(i)
    
mysetss = {1, 1, 2, 3, 3, 4, 5, 8, 7,15,11,6}

for i in mysetss:
    print(i)
