#Formating strings
letter="Hey my name is {1} and I am from{0}"

country="India"
name="Justin"

print(letter.format(country,name))
print(f"Hey my name is {name} and I am from{country}" )
