#List methods
l=[4,5,3,56,76543,34]
l.sort(reverse=True)
l.reverse()
print(l.index(5))
print(l.count(3))


m=l#This is a reference so m=l is same list so change happen in both
m[0]=0
print(l)
l.append(5)
l.insert(1,899)#Insert 899 at index 1
x=[4,564,34,5]
l.extend(x)

k=x+l #merges 2 list

#Tuple
tup=(1,23,43,3,4,56,4,3)
d=(1) #This will be an int and use (1,) to make tuple
#Tuple is immutable
