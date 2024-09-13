class Student:
    college_name="SVVV"

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def welcome(self):
        print("welcome",self.name)
        
    def get_marks(self):
        return self.marks

s1=Student("Yash",97)
s1.welcome()
print(s1.marks)