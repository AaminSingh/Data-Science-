# marks = 70
# if marks >= 90:
#     print("A grade")    
# elif marks >= 80:
#     print("B grade")
# else:
#     print("C grade")


age = int(input("Enter your age:"))

license = input("Do you have a driving license? (yes/no): ").strip().lower()

if age>=18:
    if license == "yes":
        print("You are eligible to drive.")
    else:
        print("You are not eligible to drive.")
else:
    print("You are not eligible to drive.You must be at least 18 years old.")




val = int(input("Enter a val: "))

if val % 2==0:
    print(val,"the number is even")
elif val >2:
    print(val,"the number is greater than 2")
else:
    print(val,"the number is odd")


    