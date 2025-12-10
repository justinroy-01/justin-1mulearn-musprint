#Match case
x=int(input("enter the value"))

match x:
    case 0:
        print("Value is 0")
    case 1:
        print("Value is 1")
    case _ if x!=0 and x!=1 and x>-1:
        print("Value is not 0 neither 1")
    case _ :
        print("Normal negative value")

#Loops
#For loop
#While loop

x="Hey I am Justin"
for i in x:
    print(i,end='')

c=[1,4,3,45,67,865,2,456,3]
for i in c:
    print(i)
#nested loop
for i in range(1,21):
    for j in range (1,5):
        print(i*'@',j*'!')
