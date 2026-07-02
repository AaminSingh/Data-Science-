while True:
    print("====== MENU ======")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == '1':
        print("add student selected")
        
    elif choice == '2':
        print("view student selected")
        
    elif choice == '3':
        print("search student selected")
        
    elif choice == '4':
       print("Update Student Selected")

    elif choice == '5':
       print("Delete Student Selected")

    elif choice == '6':
       print("Exiting...")
       break
    else:
        print("Invalid choice. Please try again.")            