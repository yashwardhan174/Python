class Student:
    name="Yash"
    def __init__(self,fullname):
        self.name=fullname
        print("Adding new student to the database")

s1=Student("Yash")
print(s1.name)

