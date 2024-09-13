marks=[1,2,3,4,5]
print("List Without inter changed elements")
print(marks)
last=marks.pop()
first=marks.pop(0)
marks.append(first)
marks.insert(0,last)
print("List with Changed Elements")
print(marks)