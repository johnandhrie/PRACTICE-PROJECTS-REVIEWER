def todo_app():
    tasks = []
    while True:
        print("\n1. View Tasks\n2. Add Task\n3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        elif choice == '2':
            new_task = input("Enter task: ")
            tasks.append(new_task)
            print("Task added!")
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

# todo_app()