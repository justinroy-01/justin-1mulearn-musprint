# Conditional operators continued


a=int(input("Enter the price of apple:"))

if (a>40):
    print("The price is too high")
elif (0<=a<=40):
    print("You can buy the apple")
else :
    print("price cant be negative")

#Exerscise 2

#program to greet goodmorning
import time

timestamp1=int (time.strftime('%H'))

print (timestamp1)

if (12>timestamp1>6):
    print("Good Morning Sir")
elif (12<=timestamp1<17):
    print("Good Afternoon Sir")
elif (17<=timestamp1<20):
    print("Good Evening Sir")
else :
    print ("Good night Sir")
