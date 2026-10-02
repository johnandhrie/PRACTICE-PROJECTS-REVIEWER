"""
Practical Exam Practice — Personal Expense Tracker
Student: [Mercado, John Andhrie M.]
"""

expenses = []

def display_menu():
    print("\n=== Personal Expense Tracker ===")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. Calculate total spending")
    print("4. View expenses by category")
    print("5. Exit")
    return input("Choose an option: ").strip()

def add_expense(exp_list):
    desc = input("Enter expense description (e.g., Lunch, Bus): ").strip()
    category = input("Enter category (Food, Transport, Bills): ").strip().capitalize()
    try:
        amount = float(input("Enter amount ($): "))
        if amount < 0:
            print("\n[Error] Amount cannot be negative.")
            return
    except ValueError:
        print("\n[Error] Please enter a valid number for the amount.")
        return
        
    expense = {
        "description": desc,
        "category": category,
        "amount": amount
    }
    exp_list.append(expense)
    print(f"\nSuccess: Added ${amount:.2f} for '{desc}'!")

def view_expenses(exp_list):
    if not exp_list:
        print("\n[Notice] No expenses recorded yet.")
        return
        
    print("\n--- Expense History ---")
    for i, e in enumerate(exp_list, start=1):
        print(f"{i}. Desc: {e['description']} | Category: {e['category']} | Amount: ${e['amount']:.2f}")

def calculate_total(exp_list):
    if not exp_list:
        print("\n[Notice] No expenses to calculate.")
        return
        
    total = sum(e['amount'] for e in exp_list)
    print(f"\n--- Financial Summary ---")
    print(f"Total Money Spent: ${total:.2f}")

def filter_by_category(exp_list):
    if not exp_list:
        print("\n[Notice] No expenses recorded.")
        return
        
    target_cat = input("Enter category to filter by (Food, Transport, Bills): ").strip().capitalize()
    matches = [e for e in exp_list if e['category'] == target_cat]
    
    if matches:
        print(f"\n--- Expenses in Category: {target_cat} ---")
        cat_total = 0
        for e in matches:
            print(f"- {e['description']}: ${e['amount']:.2f}")
            cat_total += e['amount']
        print(f"Total for {target_cat}: ${cat_total:.2f}")
    else:
        print(f"\n[Result] No expenses found under category '{target_cat}'.")

def main():
    running = True
    while running:
        choice = display_menu()
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            calculate_total(expenses)
        elif choice == '4':
            filter_by_category(expenses)
        elif choice == '5':
            print("\nExiting program. You've got this tomorrow!")
            running = False
        else:
            print("\n[Error] Invalid option. Please choose 1-5.")

if __name__ == "__main__":
    main()