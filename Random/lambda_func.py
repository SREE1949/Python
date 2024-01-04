# this code will generate multiplication table of a number given by user


m,l=input("Enter the number and limit: ").split()

def prod(a):
    return lambda x: int(x) * int(a)

def mult(p,q):
    for i in range(1,int(q)+1):
        r=prod(i)
        print(i,"x",p,"=",r(p) )

print("Product of number",m)
mult(m,l)


