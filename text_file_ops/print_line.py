# this code is to print the line from text file given by the user

file_name=input("Enter the file name: ")
n=input("Enter the line number: ")

f=open(file_name,"rt")
for x in range(int(n)-1) :
 f.readline()
print(f.readline())
f.close()                    
