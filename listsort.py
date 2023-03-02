animals = ['chicken', 'cow', 'snail', 'elephant']
animals.sort()
print(animals)
animals.sort(key=len)
print(animals)
animals.sort(key=len,reverse=True)
print(animals)