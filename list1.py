#1).colours=["red","green","yellow","white","brown"]
#print the largest string in the list of strings
#Print the no.of strings wholse length is >=5
#print the count of strings which have first and last character same


colours=["red","green","yellow","white","brown","nun","codec"]
maximum = max(colours, key = len)
print("largest string in the list of strings:",maximum)
print("no.of strings wholse length is >=5 :")
for i in colours:
    if len(i)>=5:
        print(i)
count=0
print("strings which have first and last character same:")
for i in colours:
    k=i
    if k[0]==k[-1]:
        count=count+1
        print(k)
print("count of strings which have first and last character same:",count)