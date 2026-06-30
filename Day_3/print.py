print("helo world")
a=5
if(a==5):
    print("a is equal to 5")
    

b = [23,4,13,5,6] 
#printing the 3rd element of the list

print(b[2])
#printing the type of the list
print(type(b))   

#append is for adding an element at the end of the list
b.append(24)
print(b)

#insert is for inserting an element at a specific index
b.insert(3,5)
print(b)

marks = [23,4,13,5,6]
marks[2:4] = [45,200]
print(marks)
print("marks at the index 2 to 4",marks[2:5])


