import re

def loganalysis(keywords,file_var,newfile):
    for i in re.findall(keywords,file_var):
        print(i)
        newfile.write(i)
    newfile.close()
    return

logfile = open("C:/Users/DELL/Downloads/logcat_5.txt", 'r')
newfile=open("C:/Users/DELL/Downloads/loganalysis.txt", 'w')
file_var=logfile.read()
keywords="libprocessgroup:.*\n|Zygote  :.*\n|tombstoned:.*\n"

loganalysis(keywords,file_var,newfile)