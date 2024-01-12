#define a class account with data members name and balance and methods to input data, deposit and amount withdraw an amount and ensure the balance of rs 1000 and diplay the details
#create an object and demonstrate the function.

class account :
    def __init__(self,name,acc_n,bal) :
        self.name=name
        self.acc_n=acc_n
        self.bal=bal

    def __str__(self) :
        return f"Name of A/C holder:{self.name} \nAccount number : {self.acc_n} \nbalance ={self.bal}"
    def depo(self) :
        w=int(input("Enter the amount to deposit : "))
        self.bal=self.bal+w
        print("Balance amount:",self.bal)
    
    def withdraw(self) :
        w=int(input("Enter the amout to withdraw : "))
        if self.bal-w < 2000 :
            print("Amount cannot withdraw")
        else :
            self.bal=self.bal-w
            print("Balance amount : ",self.bal)


while True :
    print("******************WELCOME**********************")
    a=input("Enter the name of account holder : ")
    b=int(input("Enter the account number: "))
    c=int(input("Enter the balance amount : "))
    p=account(a,b,c)
    print("Hello ",p.name)
    print(p)
    while True :
        print("*************************Menu***********************\n 1. Deposit \n 2. Withdraw \n 3. Exit")
        o=input("Select your option : ")
        if o=="1" :
            p.depo()
        elif o == "2" :
            p.withdraw()
        elif o == "3" :
            break
        else :
            print("Select valid option ")

    op=input("Do you want to check next account(y/n) :")
    if op=="n" :
        break



