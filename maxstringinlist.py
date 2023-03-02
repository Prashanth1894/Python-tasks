str1="python automation testing interview test"
l1=str1.split(" ")
l2=""
l=0
for i in l1:
    if l<len(i):
        l=len(i)
        l2=i

print(l2)

