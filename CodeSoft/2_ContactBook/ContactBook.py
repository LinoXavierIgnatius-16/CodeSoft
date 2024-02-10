class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return

        print("\n--- Contact List ---")
        for contact in self.contacts:
            print(f"Name: {contact.name}")
            print(f"Phone: {contact.phone}")
            print(f"Email: {contact.email}")
            print(f"Address: {contact.address}")
            print("-------------------")

    def search_contact(self, keyword):
        results = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone:
                results.append(contact)
        return results

    def update_contact(self, old_name, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == old_name.lower():
                self.contacts[i] = new_contact
                print(f"Contact updated: {new_contact.name}")

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name.lower() != name.lower()]
        print(f"Contact deleted: {name}")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone, email, address)
            contact_manager.add_contact(new_contact)
            print(f"Contact added: {name}")

        elif choice == '2':
            contact_manager.view_contacts()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            results = contact_manager.search_contact(keyword)
            if results:
                print("\n--- Search Results ---")
                for result in results:
                    print(f"Name: {result.name}")
                    print(f"Phone: {result.phone}")
                    print(f"Email: {result.email}")
                    print(f"Address: {result.address}")
                    print("-------------------")
            else:
                print("No matching contacts found.")

        elif choice == '4':
            old_name = input("Enter the name of the contact to update: ")
            new_name = input("Enter the new name: ")
            new_phone = input("Enter the new phone number: ")
            new_email = input("Enter the new email: ")
            new_address = input("Enter the new address: ")
            new_contact = Contact(new_name, new_phone, new_email, new_address)
            contact_manager.update_contact(old_name, new_contact)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Management System. Thanks!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
