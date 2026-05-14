#CORE DATA TYPES
a=0
print(type(a))
#2
a="hjn"
print(type(a))
#list
a=[1,2,3,6,90,4]
print(a)
#tuple
a=(1,2,4,6,2)
print(a)
#set
#a=set(input(int(2)))
print(a)
#dictonary
a={1,2,35,54}
print(a)
#to add numbers to the set
a=[1,3,6,23]
print(a)
a.append(90)
print(a)

# core functions
a=[1,32,43,3,60]
print(a)
a.append(32)
print(a)
#duplicate list
p=(a.copy())
print(p)
print(a.count(1))
#combine two list
print(p.extend(a))
print(a)

#store
print(p.index(1))
#index the value element to be inserted
print(a.insert(4,2))
print(a)

#delete the last element
print(a.pop())
print(a)

#index element is removed
print(a.pop(1))
print(a)

#change the element with the position
print(a.remove(3))
print(a)

#revese the set
print(a.reverse())
print(a)

#sort data type
b=["s","ss","dsd","dsaq"]
print(a.sort())
print(a)
