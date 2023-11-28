#the code perform multiple operations on a text file as per user requirement


def count_line(fn) :
    f=open(fn,"r")
    x=0
    while f.readline():
        x=x+1
    return x

f_name=input("Enter the file name : ")
op=input("operation to perform :")
if op=="line" :
   print( count_line(f_name))
~                                                                                                                                                                                                                  
~                                                                                                                                                                                                                  
~                                                                                                                                                                                                                  
~                                               
