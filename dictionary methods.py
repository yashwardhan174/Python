#dictname.keys() resturns all keys
student={
    "name":"Yash",
    "subjects":{
        "phy":97,
        "math":99,
        "chem":96
    }
}
print(student.keys())
print(list(student.keys())) #Conerts it to List
print(student.values())
print(student.items())
print(student.get("name"))
student.update({"city" : "Indore"})
print(student)