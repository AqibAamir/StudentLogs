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
def update_student(old_name, new_name, filename='students.txt'):
    try:
        with open(filename, 'r') as file:
            students = file.readlines()
        
        students = [student.strip() for student in students]
        
        if old_name in students:
            with open(filename, 'w') as file:
                for student in students:
                    if student == old_name:
                        file.write(new_name + '\n')
                    else:
                        file.write(student + '\n')
            print(f"Student '{old_name}' has been updated to '{new_name}'.")
        else:
            print(f"Student '{old_name}' not found.")
    
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

def delete_student(name, filename='students.txt'):
    try:
        with open(filename, 'r') as file:
            students = file.readlines()
        
        students = [student.strip() for student in students]
        
        if name in students:
            students.remove(name)
            with open(filename, 'w') as file:
                for student in students:
                    file.write(student + '\n')
            print(f"Student '{name}' has been deleted.")
        else:
            print(f"Student '{name}' not found.")
    
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

choice = str(input("Please type [1] if you want to view a student's overall score, type [2] if you want to adjust their score, type [3] to view all students, type [4] to update a student's name, or type [5] to delete a student: "))
if choice == "1":
    student_name = input("Enter the student's name: ")
    check_student(student_name)

elif choice == "2":
    new_student_name = input("Enter the new student's name to add: ")
    add_student(new_student_name)

elif choice == "3":
    view_all_students()

elif choice == "4":
    old_student_name = input("Enter the student's current name: ")
    new_student_name = input("Enter the student's new name: ")
    update_student(old_student_name, new_student_name)

elif choice == "5":
    student_name = input("Enter the student's name to delete: ")
    delete_student(student_name)

def add_student_score(name, score, filename='scores.txt'):
    try:
        with open(filename, 'a') as file:
            file.write(f"{name}: {score}\n")
        print(f"Score for student '{name}' has been added.")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_student_score(name, filename='scores.txt'):
    try:
        with open(filename, 'r') as file:
            scores = file.readlines()
        
        found = False
        for entry in scores:
            student, score = entry.strip().split(': ')
            if student == name:
                print(f"{name}'s score: {score}")
                found = True
                break
        
        if not found:
            print(f"No score found for student '{name}'.")
    
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")


def update_student_score(name, new_score, filename='scores.txt'):
    try:
        with open(filename, 'r') as file:
            scores = file.readlines()
        
        with open(filename, 'w') as file:
            for entry in scores:
                student, score = entry.strip().split(': ')
                if student == name:
                    file.write(f"{name}: {new_score}\n")
                else:
                    file.write(entry)
        print(f"Score for student '{name}' has been updated to {new_score}.")
    
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

ef delete_student_score(name, filename='scores.txt'):
    try:
        with open(filename, 'r') as file:
            scores = file.readlines()
        
        with open(filename, 'w') as file:
            for entry in scores:
                student, score = entry.strip().split(': ')
                if student != name:
                    file.write(entry)
        print(f"Score for student '{name}' has been deleted.")
    
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
