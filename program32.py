#Create a new file "practice.txt" using python , add following data in it

#Hi everyone
#we are learning File I/O
#using Java
#I like programing in Java

with open("practice.txt","w")as f:
    f.write("Hi Everyone\nwe are learning File I/O\nusing Java\nI like programing in Java")
    f.close()