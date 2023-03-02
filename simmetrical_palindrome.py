str1="amam"
half=int(len(str1)/2)
#print(half)
if len(str1)%2==0:
    first=str1[:half]
    #print(first)
    second=str1[half:]
    #print(second)
else:
    first=str1[:half]
    print(first)
    second=str1[half+1:]
    print(second)
if first==second:
    print(str1,"is symmetric")
else:
    print(str1,"is not symmetric")

if first==second[::-1]:
    print(str1, "is a palindrome")
else:
    print(str1,"is not a palindrome")