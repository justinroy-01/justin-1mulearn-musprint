#For loop with else
for i in range(5):
    print(i)
else:
    print("No")
"""
Happens when for is false
"""

#Exception handling

try:
    x=int(input("Enter a no1:"))
    x1=int(input("Enter a no2:"))
    print(x/x1)
except Exception as E:
    print(E)
