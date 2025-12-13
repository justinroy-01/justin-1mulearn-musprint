#Lists are  ordered items
#Lists are mutable
l=[1,23,3,56,2,'hello there']
print(l)
#List stores multiple values under a same name
print(l[0])
print(l[1])

print(l[2])

print(l[3])
#List index is same as string indexing


'''
We can access elements from a list using positive indexing or negative indexing
negative indexing->len(list)-negative index (positive index)
'''
#eg
print(l[-1]) #same as print(l[len(l)-1)
print(l[len(l)-1])

#membership operator

if 7 in l:
    print("Present")
elif 2 in l:
    print("Present2")
else:
    print("Absent")

print(l[:]) #slicing to print all the elements

print(l[::2])#Jumps by 2
#List comprehension
Lis=[i for i in range(40)]
l2=[i for i in l if i==2]
