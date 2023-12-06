#receive n numbers from user and sort using buble sort
#print the list


def sort_n(n):
    for i in range(1,len(n)):
        for j in range(1,len(n)):
            if n[j] < n[j-1]:
                a=n[j-1]
                n[j-1]=n[j]
                n[j]=a
    print("The sorted list: ",*n)
    

num=input("enter the numbers (separated by space): ")

n=num.split();
n=[int(i) for i in n ]
sort_n(n)

