#There are 3 Logical Operators in Python
#AND which is written as->  <condition1>and<condition2>
#OR which is written as ->  <condition1>or<condition2>
#NOT which is written as->  not<condition1>

#Program for AND operator
age = int(input("age :"))
if(age >=18 and age <=72):
    print("You can drive")
else:
    print("You can't drive ")

#Program for OR operator

food = input("food :")
print("Sweet") if food == "cake" or food == "Jalebi" else print("Not Sweet")


#Program for NOT operator

x = False

print(not x)


