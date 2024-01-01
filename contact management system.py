# Initialize an empty contact list as a list of dictionaries
contacts = []

def add_contact(name, phone, email):
    contact = {
        'Name': name,
        'Phone': phone,
        'Email': email
    }
    contacts.append(contact)
    print(f"Contact for {name} added successfully!")

def view_contacts():
    if not contacts:
        print("Your contact list is empty.")
    else:
        print("Your Contacts:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}")

def edit_contact(index, name, phone, email):
    if 0 <= index < len(contacts):
        contacts[index]['Name'] = name
        contacts[index]['Phone'] = phone
        contacts[index]['Email'] = email
        print(f"Contact edited successfully!")
    else:
        print("Invalid contact index.")

def delete_contact(index):
    if 0 <= index < len(contacts):
        deleted_contact = contacts.pop(index)
        print(f"Contact {deleted_contact['Name']} deleted successfully!")
    else:
        print("Invalid contact index.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add a new contact")
        print("2. View your contacts")
        print("3. Edit a contact")
        print("4. Delete a contact")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email address: ")
            add_contact(name, phone, email)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            view_contacts()
            index = int(input("Enter the index of the contact to edit: ")) - 1
            if 0 <= index < len(contacts):
                name = input("Enter the new name: ")
                phone = input("Enter the new phone number: ")
                email = input("Enter the new email address: ")
                edit_contact(index, name, phone, email)
            else:
                print("Invalid contact index.")
        elif choice == '4':
            view_contacts()
            index = int(input("Enter the index of the contact to delete: ")) - 1
            delete_contact(index)
        elif choice == '5':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
