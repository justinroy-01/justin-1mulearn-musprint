#While loop
i=0
while (i<10):
    print(i)
    i=i+1

else:
    print("Hi") #Else can be used with while
#break and continue in python

for i in range (1,12):
    if (i==5):
        continue
    elif (i==11):
        print("Broken")
        break
    print(i)
