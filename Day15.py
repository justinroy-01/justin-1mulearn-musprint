#Sets
s={2,3,5,65,2}
print(s)
#Unordered data and immutable
info={"Carla",45,False,4.5,19,2,19}
print(info)
l=set()#To create an empty set


#Set Methods
s1={1,2,3,4,5,6,7}
s2={7,8,9}
print(s1.union(s2))#To find union of set , s1 and s2 not changed
#s1.update(s2)#to add values of s2 to s1 ui8io89*9
print(s1)
#s1.intersection_update(s2)#Those that ae not common
print(s1)
s3=s1.difference(s2)
print(s3)
print(s1.isdisjoint(s2))#check if both set have common element
