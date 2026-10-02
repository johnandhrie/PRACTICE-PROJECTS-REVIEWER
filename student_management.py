"""
Practical Exam — Student Grade Management System
Student: [Mercado, John Andhrie M.]
"""

students = []  # starts empty — stores student records as dictionaries

def display_menu():
    print("\n=== Student Grade Management System ===")
    print("1. Add a student record")
    print("2. View all student records")
    print("3. Calculate class average grade")
    print("4. Find a student by name")
    print("5. Remove a student record")
    print("6. Exit")

    return input("Choose an option: ").strip()

def add_student(student_list):
    name = input("Enter student's name: ").strip()
    subject = input("Enter subject name: ").strip()
    
    try:
        grade = float(input("Enter grade (0-100): "))
        if not (0 <= grade <= 100):
            print("\n[Error] Grade must be between 0 and 100.")
            return
    except ValueError:
        print("\n[Error] Please enter a valid numerical grade.")
        return
    
    # Store student record as a dictionary
    student = {
        "name": name,
        "subject": subject,
        "grade": grade
    }
    student_list.append(student)
    print(f"\nSuccess: Record for '{name}' added successfully!")

def view_students(student_list):
    if not student_list:
        print("\n[Notice] No student records found in the system.")
        return
        
    print("\n--- Current Student Records ---")
    for index, s in enumerate(student_list, start=1):
        print(f"{index}. Name: {s['name']} | Subject: {s['subject']} | Grade: {s['grade']}")

def calculate_class_average(student_list):
    if not student_list:
        print("\n[Notice] No records available to calculate an average.")
        return 0.0
        
    total_grades = sum(s['grade'] for s in student_list)
    average = total_grades / len(student_list)
    
    print(f"\n--- Class Performance Summary ---")
    print(f"Total Students Tracked: {len(student_list)}")
    print(f"Class Average Grade: {average:.2f}")
    return average

def find_student(student_list):
    if not student_list:
        print("\n[Notice] No records found.")
        return
        
    search_name = input("Enter the student name to search: ").strip().lower()
    found_students = [s for s in student_list if search_name in s['name'].lower()]
    
    if found_students:
        print("\n--- Search Results ---")
        for s in found_students:
            print(f"Name: {s['name']} | Subject: {s['subject']} | Grade: {s['grade']}")
    else:
        print(f"\n[Result] Student matching '{search_name}' was not found.")

def remove_student(student_list):
    if not student_list:
        print("\n[Notice] No records to remove.")
        return
        
    search_name = input("Enter the exact name of the student to remove: ").strip().lower()
    for s in student_list:
        if s['name'].lower() == search_name:
            student_list.remove(s)
            print(f"\nSuccess: Record for '{s['name']}' has been removed.")
            return
            
    print(f"\n[Result] Student matching '{search_name}' was not found.")

def main():
    running = True
    while running:
        choice = display_menu()
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            calculate_class_average(students)
        elif choice == '4':
            find_student(students)
        elif choice == '5':
            remove_student(students)
        elif choice == '6':
            print("\nExiting program.")
            running = False
        else:
            print("\n[Error] Invalid option. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main()