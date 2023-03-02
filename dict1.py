
'''L = [ name, gender, age, address]
D = [ name:sophie , gender:female , age : 6 , address: Hyderabad ]
if the item in the list is present in the dic -- print the item in the dict
else print : address is not present in D'''
L = ["name", "gender", "city","age", "address","hello"]
D= {"name":"sophie", "gender": "female" , "age": 6, "address":"Hyderabad"}
for i in L:
    if i in D:
        print(D[i])
    else:
        print("item is not present in list")