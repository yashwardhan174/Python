marks = int(input("marks :"))
if(marks >90):
    print("Grade A+")
elif(marks <=90 and marks>80):
    print("Grade A")
elif(marks <=80 and marks>70):
    print("Grade B")
elif(marks <=70 and marks>50):
    print("Grade C")
elif(marks <=50 and marks>=33):
    print("Grade D")
else:
    print("You are fail")