#Set continued

cities={"Tokyo","Madrid","Berlin"}
cities2={"Tokyo"}
print(cities.issuperset(cities2))
cities.add("Dublin")

print(cities)
cities.remove("Madrid")
cities.discard("Madrid")#Doesnt give error
cities.pop()

#Dictionary
dic={"Justin":"Human","Spoon":"Object"}
print(dic["Justin"])

#Key value pair in dictionary

print(dic.get("Justin")) #returns none if key not exist

