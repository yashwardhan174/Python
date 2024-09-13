#Type Casting means forcefully converting a data type into other data type

#Example of simple Addition between int and float

a = 2
b = 4.25 

sum = a+b
print(sum)


#Example of Converting String into integer

a1 = "2"
b1 = 4.25 #here "2" + 4.25 will give error because "2" is considered as a string


#Converting "2" into int
c,d = 1,"2"
e = int(d)
sum = c+e

print(sum) # here "2" which is stored in variable d has been converted to Int by using another variable e
#<variable1> = int(var to convert)
#<var2> = float(var to convert)