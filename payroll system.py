"""
Practical Exam Practice — Employee Payroll System
Student: [Mercado, John Andhrie M.]
"""

employees = []

def display_menu():
    print("\n=== Employee Payroll System ===")
    print("1. Add employee record")
    print("2. View all employees")
    print("3. Calculate weekly payroll for everyone")
    print("4. Search employee by name")
    print("5. Exit")
    return input("Choose an option: ").strip()

def add_employee(emp_list):
    name = input("Enter employee full name: ").strip()
    try:
        hours = float(input("Enter hours worked this week: "))
        rate = float(input("Enter hourly wage rate ($): "))
        if hours < 0 or rate < 0:
            print("\n[Error] Hours and rate cannot be negative.")
            return
    except ValueError:
        print("\n[Error] Please enter valid numbers for hours and rate.")
        return
        
    employee = {
        "name": name,
        "hours": hours,
        "rate": rate
    }
    emp_list.append(employee)
    print(f"\nSuccess: Employee '{name}' added to payroll!")

def view_employees(emp_list):
    if not emp_list:
        print("\n[Notice] No employee records found.")
        return
        
    print("\n--- Employee Roster ---")
    for i, emp in enumerate(emp_list, start=1):
        print(f"{i}. Name: {emp['name']} | Hours: {emp['hours']} | Rate: ${emp['rate']:.2f}/hr")

def calculate_payroll(emp_list):
    if not emp_list:
        print("\n[Notice] No employees to calculate payroll for.")
        return
        
    print("\n--- Weekly Payroll Breakdown ---")
    total_payroll = 0
    for emp in emp_list:
        gross_pay = emp['hours'] * emp['rate']
        total_payroll += gross_pay
        print(f"Employee: {emp['name']} | Gross Pay: ${gross_pay:.2f}")
    print(f"\nTotal Company Payroll Outflow: ${total_payroll:.2f}")

def search_employee(emp_list):
    if not emp_list:
        print("\n[Notice] Payroll system is empty.")
        return
        
    query = input("Enter employee name to search: ").strip().lower()
    matches = [emp for emp in emp_list if query in emp['name'].lower()]
    
    if matches:
        print("\n--- Search Results ---")
        for emp in matches:
            gross = emp['hours'] * emp['rate']
            print(f"Name: {emp['name']} | Hours: {emp['hours']} | Rate: ${emp['rate']} | Weekly Pay: ${gross:.2f}")
    else:
        print("\n[Result] Employee not found.")

def main():
    running = True
    while running:
        choice = display_menu()
        if choice == '1':
            add_employee(employees)
        elif choice == '2':
            view_employees(employees)
        elif choice == '3':
            calculate_payroll(employees)
        elif choice == '4':
            search_employee(employees)
        elif choice == '5':
            print("\nExiting program.")
            running = False
        else:
            print("\n[Error] Invalid option. Pick 1-5.")

if __name__ == "__main__":
    main()