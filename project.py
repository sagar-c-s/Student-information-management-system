import hashlib
import secrets

# Hash the password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Compare two hashes securely
def verify_password(stored_password, provided_password):
    stored_password_hash = hash_password(stored_password)
    provided_password_hash = hash_password(provided_password)
    return secrets.compare_digest(stored_password_hash, provided_password_hash)

# Example usage
stored_password = 'a2sa'
provided_password = input("Enter password: ")

if verify_password(stored_password, provided_password):
    print("Password matches!")
    
    students = {}
    
    def add_student(students):
        name = input("Enter student name: ")
        roll_no = int(input("Enter roll number: "))
        class_name = input("Enter class: ")
        section = input("Enter section: ")
        students[roll_no] = {'Name': name, 'Class': class_name, 'Section': section}
        print("Student added successfully!")

    def view_student(students, roll_no):
        if roll_no in students:
            print("Student Details:")
            print("Name:", students[roll_no]['Name'])
            print("Class:", students[roll_no]['Class'])
            print("Section:", students[roll_no]['Section'])
        else:
            print("Student not found!")

    def display_all_students(students):
        if not students:
            print("No students found.")
        else:
            print("Student List:")
            for roll_no, details in students.items():
                print(f"Roll No: {roll_no}")
                print(f"Name: {details['Name']}")
                print(f"Class: {details['Class']}")
                print(f"Section: {details['Section']}")
                print()

    def update_student(students, roll_no):
        if roll_no in students:
            name = input("Enter new name: ")
            class_name = input("Enter new class: ")
            section = input("Enter new section: ")
            students[roll_no]['Name'] = name
            students[roll_no]['Class'] = class_name
            students[roll_no]['Section'] = section
            print("Student details updated successfully!")
        else:
            print("Student not found!")

    def delete_student(students, roll_no):
        if roll_no in students:
            del students[roll_no]
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    def export_to_excel(students):
        import pandas as pd
        df = pd.DataFrame.from_dict(students, orient='index')
        df.to_excel('a2.xlsx', index=True, index_label='Roll No')
        print("Data exported to Excel successfully!")

    while True:
        print("\nStudents Information Management System")
        print("1. Add Student")
        print("2. View Student")
        print("3. View All Students")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Export to Excel")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student(students)
        elif choice == 2:
            roll_no = int(input("Enter roll number of student to view: "))
            view_student(students, roll_no)
        elif choice == 3:
            display_all_students(students)
        elif choice == 4:
            roll_no = int(input("Enter roll number of student to update: "))
            update_student(students, roll_no)
        elif choice == 5:
            roll_no = int(input("Enter roll number of student to delete: "))
            delete_student(students, roll_no)
        elif choice == 6:
            export_to_excel(students)
        elif choice == 7:
            print("Closing the program...")
            break
        else:
            print("Invalid choice. Please try again.")

else:
    print("Password does not match!")