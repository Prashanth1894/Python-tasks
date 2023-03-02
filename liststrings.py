x=['grape banana mango','nut orange peach','apple nut banana apple mango']
#op=['grape', 'banana', 'mango', 'nut', 'orange', 'peach', 'apple', 'nut', 'banana', 'apple', 'mango']
y=" ".join(x)
print(y)
z=y.split()
print(z)
#unique fruits
u=[]
for i in z:
    if i not in u:
        u.append(i)
print(u)