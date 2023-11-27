# This code will search for the word given by user and append if not present in text file
#Also if the file not exist it will create the file and append the word


import re
import os.path as op

#function to check word in file
def f_search(fn,wr) :
    f=open(fn,"r")
    l=f.readline()
    x=0
    while l :
        x=re.search(wr,l)
        if x:
            break
        l=f.readline()
    f.close()
    return x

f_name=input("Enter the file name: ")
wd=input("Enter the word to search: ")

if op.isfile(f_name) :
    if f_search(f_name,wd):
        print("The file exist and the word present in the file ")
    else:
        f=open(f_name,"a")
        f.write(wd)
        print("The file exist and the word written into the file")
        f.close()
    
else :
    f=open(f_name,"a")
    f.write(wd)
    print("The file not  exist and the word written into the new file")
    f.close()
