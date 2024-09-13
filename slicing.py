#Slicing means Accesing parts of String
#str[starting_index : ending_index] #starting index will be included but ending index will not be included

#Example
str = "Yashwardhan Nigam"
print(str[2 : 8 ]) #output will be shward because at index 2 s is stored and at 7th index d is stored 

#if we do not write the starting index python autometically considers it from 0 index 
#example str[ :5] it will start from 0
#if we do not write the ending index python autometically considers till last index
#example str[3:] it will consider till last index