#this code used to handle exceptions

fname=input("Enter the file name: ")
try:
    f=open(fname,"r")
    try :
        print(f.read())

    except :
        print("Somthing went wrong")
    else :
        print("read file")
    finally:
        f.close()
        print("file closed")
except:
    print("File not opened")






