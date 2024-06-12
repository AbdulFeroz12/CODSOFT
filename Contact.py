class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if self.contacts:
            print("Contact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}")
        else:
            print("Contact list is empty.")

    def search_contact(self, keyword):
        found_contacts = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                found_contacts.append(contact)
        if found_contacts:
            print("Search Results:")
            for contact in found_contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}")
        else:
            print("No matching contacts found.")

    def update_contact(self, name, new_contact):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone_number = new_contact.phone_number
                contact.email = new_contact.email
                contact.address = new_contact.address
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\n---------CONTACT MANAGEMENT -------------------")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone_number, email, address)
            contact_manager.add_contact(contact)
            print("Contact added successfully.")
        elif choice == '2':
            contact_manager.view_contacts()
        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            contact_manager.search_contact(keyword)
        elif choice == '4':
            name = input("Enter name of contact to update: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_manager.update_contact(name, new_contact)
        elif choice == '5':
            name = input("Enter name of contact to delete: ")
            contact_manager.delete_contact(name)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
