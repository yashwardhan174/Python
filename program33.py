#WAF that replace all occurance of "Java " with "Pyhton" in program 32 file

with open("practice.txt","r")as f:
    data=f.read()

new_data=data.replace("Java","Python")
print(new_data)

with open("practice.txt","w")as f:
    data=f.write(new_data)