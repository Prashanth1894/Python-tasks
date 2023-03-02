x = [1203, 1256, 312456, 98]
#count how many times each digit appears
# 0 1
# 1 3
# 2 3
# 3 2
count=[0]*10
for i in x:
    for char in str(i):
        count[int(char)]+=1
for i in range(0,10):
    print(i,count[i])