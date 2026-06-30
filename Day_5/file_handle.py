with open("class.txt", "w") as file:
    file.write("Good morning class!\n")
    file.write("Hello everyone, welcome to the class!\n", )
    file.write(f"Karan, 23,Pune\n")


with open("class.txt","r") as file:

    content = file.read()
    print(content)


with open("class.txt","r") as file:
    for line in file:
        print(line.strip())

with open("class.txt",'r') as file:
     first_line = file.readline 
     print(first_line)  
    