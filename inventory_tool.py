"""
Midterm Practical Exam — Network Device Inventory Tool
Student: [Mercado, John Andhrie M.]
"""

devices = []  # starts empty — the user adds devices as the program runs

def display_menu():
    print("\n=== Network Device Inventory ===")
    print("1. Add a device")
    print("2. View all devices")
    print("3. Count active vs inactive devices")
    print("4. Find a device by name")
    print("5. Remove a device (Bonus)")
    print("6. Exit")

    return input("Choose an option: ").strip()

def add_device(device_list):
    name = input("What is the name of the device? ").strip()
    ip = input("What is the IP address? ").strip()
    status = input("What is the status (Active/Inactive)? ").strip().capitalize()
    
    # Store device as a dictionary
    device = {
        "name": name,
        "ip": ip,
        "status": status if status in ["Active", "Inactive"] else "Active"
    }
    device_list.append(device)
    print(f"Success: Device '{name}' added to the inventory!")
    
def view_devices(device_list):
    # Loop through and print every device — handle empty list
    if not device_list:
        print("\n[Notice] No devices found in the inventory yet.")
        return
        
    print("\n--- Current Device Inventory ---")
    for index, device in enumerate(device_list, start=1):
        print(f"{index}. Name: {device['name']} | IP: {device['ip']} | Status: {device['status']}")

def count_active_inactive(device_list):
    # Loop through, count Active vs Inactive, return both
    if not device_list:
        print("\n[Notice] Inventory is empty.")
        return 0, 0
        
    active_count = sum(1 for d in device_list if d['status'].lower() == 'active')
    inactive_count = sum(1 for d in device_list if d['status'].lower() == 'inactive')
    
    print(f"\n--- Device Status Summary ---")
    print(f"Active Devices: {active_count}")
    print(f"Inactive Devices: {inactive_count}")
    return active_count, inactive_count

def find_device(device_list):
    # Ask for a name, search the list, print result or "not found"
    if not device_list:
        print("\n[Notice] Inventory is empty.")
        return
        
    search_name = input("Enter the name of the device to find: ").strip().lower()
    found_devices = [d for d in device_list if search_name in d['name'].lower()]
    
    if found_devices:
        print("\n--- Search Results ---")
        for device in found_devices:
            print(f"Name: {device['name']} | IP: {device['ip']} | Status: {device['status']}")
    else:
        print(f"\n[Result] Device matching '{search_name}' was not found.")

# BONUS (optional)
def remove_device(device_list):
    if not device_list:
        print("\n[Notice] Inventory is empty. Nothing to remove.")
        return
        
    search_name = input("Enter the exact name of the device to remove: ").strip().lower()
    for device in device_list:
        if device['name'].lower() == search_name:
            device_list.remove(device)
            print(f"Success: Device '{device['name']}' has been removed.")
            return
            
    print(f"\n[Result] Device matching '{search_name}' was not found.")

def main():
    running = True
    while running:
        choice = display_menu()
        
        # Use if/elif to call the right function based on choice
        if choice == '1':
            add_device(devices)
        elif choice == '2':
            view_devices(devices)
        elif choice == '3':
            count_active_inactive(devices)
        elif choice == '4':
            find_device(devices)
        elif choice == '5':
            remove_device(devices)
        elif choice == '6':
            print("\nExiting program.")
            running = False  # Set running = False when the user picks Exit
        else:
            print("\n[Error] Invalid option. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main()

