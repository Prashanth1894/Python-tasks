L=[1,2,2,3,4,5,4,4,5,5,6,7]
#[1,2,3,4,5,4,5,6,7]
newlist=[]
for i in L:
    if i not in newlist:
        newlist.append(i)
print(newlist)


