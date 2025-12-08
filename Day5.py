#String methods continued


a="good morning"
print(a.capitalize()) #Capitalize first letter and lower other

print(a.center(50)) #add charachter to the left

print ( a.count('o')) #count the ocurence

print(a.endswith('g')) #t/f

print(a.endswith('g',2,7)) #slice and so it
print(a.find('d')) #returns -1 if false
print(a.index('d')) #error if the element not found
print(a.isalnum()) # returns false if other cases
print(a.isalpha()) #check if all are characters
print(a.isupper()) #check if upper case
print(a.islower()) #check if its lower case
print(a.isspace()) #check for space
print(a.istitle()) #check if all the character of first word is capital or not
print(a.startswith('g'))  #Check if it starts with a chara
print(a.swapcase()) #used to swapcase
print(a.title()) #all the character of first word is capital

#If Else condition & conditional operators
# >,<,==,<=,>=,!=

age=int(input("Enter your age:"))
print("Your age is:",age)
if age>18:
    print('you are able to drive')
else:
    print("Not able to drive")
