class Person:
    
    @classmethod
    def changeName(cls,name):
        cls.name= name


p1 = Person()
p1.changeName("Yashwardhan Nigam")
print(p1.name)
print(Person.name)