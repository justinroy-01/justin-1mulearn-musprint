#Functions
#2 types , user defined and built in
def GeoMetric(a,b): #function definition
    return ((a*b)/(a+b))

x=int(input("Enter 1st no:"))
y=int(input("Enter 2nd no:"))

print("Gmean is ",GeoMetric(x,y))

#4 types of arguiments

"""
Default arg (order matters)
Keyword arg (order doesnt matter)
Required arg (atleast one value is needed)
variable length arg
"""
