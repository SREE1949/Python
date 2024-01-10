# Programme to interchange first and last elements of a list 

in_str=input("Enter the elements with space: ")
lst=list(in_str.split(" "))
print("The given list is : ",lst)
def end_swap(lst) :
    a=lst[-1]
    lst[-1]=lst[0]
    lst[0]=a
    return lst

print("List after interchange : ",end_swap(lst))

