while True:
    print("====== MENU ======")
    def add_student():
      print("1. Add Student")
    def view_student():  
     print("2. View Student")
    def search_student(): 
     print("3. Search Student")
    def update_student(): 
      print("4. Update Student")
    def delete_student():  
      print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == '1':
       add_student()
    elif choice == '2':
        view_student()
        
    elif choice == '3':
        search_student()
        
    elif choice == '4':
       update_student()

    elif choice == '5':
       delete_student()

    elif choice == '6':
       print("Exiting...")
       break
    else:
        print("Invalid choice. Please try again.")  


class Student:
   def __init__(self,name,age,course,RollNumber):
        self.name = name
        self.age = age
        self.course = course
        self.RollNumber = RollNumber

new_student = Student("Bisht",21,"B.tech",1201) 
print(new_student.__dict__)    

        
        
                  