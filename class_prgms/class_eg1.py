# code to create class with a method to convert even bits of a number to 0

class bit_op :
    def __init__(self,n) :
        self.n =bin(n).replace("0b","");
        self.nl=list(self.n)

    def __str__(self) :
        return f"number :{self.n}"
    
    def conv(self) :
        for i in range(0,len(self.nl)) :
            if i%2==1 :
                self.nl[i]=0
        l=len(self.nl)
        print(self.nl)
        self.n=0
        for i in range(0,l) :
            self.n=self.n*10+int(self.nl[i])

p=bit_op(7)
p.conv()
print(p)

