#simple calculater, can add more functions as operations
print("Welcome to PY calculator")

def adder():
    i=input("Enter two number (separated by space) :")
    a,b=i.split()        #split("delimeter",maxsplit)
    print("The sum of two number is :",int(a)+int(b))
    

def mult():
    i=input("Enter two number (separated by space) :")
    a,b=i.split()        #split("delimeter",maxsplit)
    print("The multiplication of two number is :",int(a)*int(b))


while True:
    
    print("\n *********options*********\n")
    print("1 add two number\n2 multiply two number")
    n=input("Enter your option: ")
    if n=="1" :
        adder()
    elif n=="2" :
        mult()
    else :
        print("Enter valid option")

    c=input("Do you want to continue?(y/n): ")
    if(c=="y"):
        continue
    else :
        print("Thank you")
        break
    
