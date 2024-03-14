# code to find LCM and GCD of two number

a,b=input("Enter two number :").split()
a=int(a)
b=int(b)
i=1;

while(1) :
    if((a*i)%b==0) :
        lcm=a*i
        break
    else :
        i=i+1

print("\n LCM = ",lcm)
i=2
gcd=1
while(1):
    if(a%i==0 and b%i==0) :
        gcd=i
        i=i+1
    else:
        i=i+1
    if(i>a or i>b):
        break

print("\n GCD = ",gcd)
    
