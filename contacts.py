import json

print("=====================================")
print("  PERSISTENT DIGITAL CONTACT BOOK   ")
print("=====================================")

FILENAME = "contacts.json"

# 1. LOAD EXIST CONTACTS FROM FILE WHEN THE APP STARTS
try:
    with open(FILENAME, "r") as file:
        # Load the JSON file data back into our live dictionary
        contact_book = json.load(file)
except FileNotFoundError:
    # If the file doesn't exist yet, start with a fresh empty dictionary
    contact_book = {}

while True:
    print("\n--- MENU ---")
    print("1. Add a new contact")
    print("2. Search for a contact")
    print("3. View all contacts")
    print("4. Save and Exit")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        name = input("Enter contact name: ").strip()
        phone = input("Enter phone number: ").strip()
        
        contact_book[name] = phone
        print(f"Success! {name} has been added to your temporary list.")
        
    elif choice == "2":
        search_name = input("Enter the name to search for: ").strip()
        if search_name in contact_book:
            print(f"Found! {search_name}'s phone number is: {contact_book[search_name]}")
        else:
            print(f"Contact '{search_name}' not found.")
            
    elif choice == "3":
        print("\n--- ALL CONTACTS ---")
        if not contact_book:
            print("[Your contact book is empty.]")
        else:
            for name, phone in contact_book.items():
                print(f"👤 {name}: {phone}")
                
    elif choice == "4":
        # 2. SAVE THE DICTIONARY TO THE FILE BEFORE EXITING
        with open(FILENAME, "w") as file:
            # json.dump takes our dictionary and converts it into structured text inside the file
            # indent=4 makes the file look beautifully organized and readable to humans
            json.dump(contact_book, file, indent=4)
            
        print("\nAll contacts saved securely to contacts.json!")
        print("Closing Contact Book. Goodbye!")
        break
        
    else:
        print("Invalid choice! Please type a number from 1 to 4.")