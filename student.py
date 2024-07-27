print("Welcome to the student datalogs. ")
print("Please enter the name of the student that you want to the see the acadeic status for.")

def check_student(name, filename='student.txt'):
    try:
        with open(filename, 'r') as file:
            students = file.readlines()
        
       
        students = [student.strip() for student in students]
        
        if name in students:
            print("Yes, student found")
        else:
            print("No, student not found")
    
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

def add_student(name, filename='student.txt'):
    try:
        with open(filename, 'a') as file:  
            file.write(name + '\n')
        print(f"Student '{name}' has been added to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")



choice=str(input("Please type [1] if you want to view a students overall score, or please type [2] if you want to adjust there score: "))
if choice=="1":
    student_name = input("Enter the student's name: ")
    check_student(student_name)

elif choice=="2":
    new_student_name = input("Enter the new student's name to add: ")
    add_student(new_student_name)
