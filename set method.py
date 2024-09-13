collection=set()

collection.add(1)
collection.add(2)
collection.add(2)#2nd 2 wont be considered because repeating is not allowed

print(collection)

#output => {1,2}

collection.remove(1) #1 will be removed
print(collection)

collection.add("Hello World")
collection.add((1,2,3))
collection.add([1,2,3]) #this will give error as list cant be added because list is mutable but set is immutable
