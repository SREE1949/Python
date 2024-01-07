#create a student class initialized with student name
#should have a function variable to store marks of different subject

class student:
    def __init__(self,name):
        self.name=name

    def marks(self):
        while True :
            s=input("enter the subject : ")
            m=input("Enter the subject marks:")
            self.s_mark={s:m}
            print("marks entered")
            y=input("do you want to continue? (y/n)")
            if y=="n" :
                break
            else :
                continue

x=input("enter the student name: ")
s1=student(x)
s1.marks()
print("mark sheet of ",s1.name)
print(s1.s_mark)
