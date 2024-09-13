#Create student class that takes name & marks of 3 subjects as arguments in constructor . Then create a method to print average

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Hi",self.name,"Average of Marks is:",sum)

s1=Student("Yash",[100,98,96])
s1.get_avg()