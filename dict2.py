data = {'name1': "january", 'name2':"feb", 'name3':"march"}
for i in range(1,10):
    n=input("do you want to perform the task yes/no:")
    if n=="yes":
        str1 = input("enter a name")
        if str1 in data.keys():
            print("name exists in the dict and its value is:",data[str1])
        else:
            data[str1]="new month"
            print("new data is:",data)
    else:
        print("thanks")
        break