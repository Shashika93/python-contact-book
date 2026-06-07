print("=====================================")
print("        MY DIGITAL CONTACT BOOK      ")
print("=====================================")

# Initialize an empty dictionary to store contacts
contact_book = {}

while True:
    print("\n--- MENU ---")
    print("1. Add a new contact")
    print("2. Search for a contact")
    print("3. View all contacts")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        # ADD CONTACT
        name = input("Enter contact name: ").strip()
        phone = input("Enter phone number: ").strip()
        
        # This adds the name as a KEY and pairs it with the phone number as the VALUE
        contact_book[name] = phone
        print(f"Success! {name} has been added to your contacts.")
        
    elif choice == "2":
        # SEARCH CONTACT
        search_name = input("Enter the name to search for: ").strip()
        
        # The 'in' keyword checks if a KEY exists inside our dictionary
        if search_name in contact_book:
            print(f"Found! {search_name}'s phone number is: {contact_book[search_name]}")
        else:
            print(f"Contact '{search_name}' not found.")
            
    elif choice == "3":
        # VIEW ALL CONTACTS
        print("\n--- ALL CONTACTS ---")
        if not contact_book:
            print("[Your contact book is empty.]")
        else:
            # .items() lets us loop through both keys (names) and values (numbers) at the same time
            for name, phone in contact_book.items():
                print(f"👤 {name}: {phone}")
                
    elif choice == "4":
        # EXIT
        print("\nClosing Contact Book. Goodbye!")
        break
        
    else:
        print("Invalid choice! Please type a number from 1 to 4.")