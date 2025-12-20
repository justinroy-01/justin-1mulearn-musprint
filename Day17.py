#Dictionary continued

info={"name":"Justin","Age":19,"elegible":True}
print(info.keys())
print(info.values())

for key in info.keys():
    print(f"{key}:{info[key]}")

print(info.items())

#dic methods
ep={123:45,676:90,600:69,765:78}
ep2={22:44,234:23}
ep.update(ep2)

print(ep)
ep.pop(123)#particular delete
ep.popitem(#deletes the last element
ep.clear()#Deletes all the data

empt={}#empty dic
#del ep deletes the entire dictionary

