str1="GeeksForGeeks"
#if i=4, k should be remove
new_str=""
for i in range (len(str1)):
    if i!=3:
        new_str=new_str+str1[i]
print(new_str)