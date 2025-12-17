#Doc strings helps understand function
def square(n):
    '''Takes in n and give square of n''' #position stays here
    print(n**2)
square(5)
print(square.__doc__)

#recursion

def fact(n):
    if n==1 or n==0:
        return 1
    else :
        return (n*fact(n-1))

s=fact(5)
print(s)
def fib(n):
    if (n==0):
        return 0
    elif(n==1 or n==2):
        return 1
    else:
        return fib(n-1)+fib(n-2)

n=int(input("Enter any number"))
print(f"The fibonacci series of {n} is:")
for i in range (n):
    print(fib(i), end=" ")
