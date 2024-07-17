import os

class contacts:
    def __init__(self):
        self.contacts = {}
    def add_contact(self, name, phone, email, additional):
        self.contacts[phone] = {'name': name, 'phone': phone, 'email': email, 'additional': additional}
    def edit_contact(self, email, name, phone, additional):
        self.contacts[phone] = {'name': name, 'phone': phone, 'email': email, 'additional': additional}
    def delete_contact(self, phone):
        self.contacts.pop(phone, None)
    def search_contact(self, phone):
        return self.contacts[phone]
    def display_contacts(self):
        return self.contacts
    def export_contacts(self, filename):
        if os.path.exists(filename):
            print("File already exists. Please choose a different filename.")
            with open(filename, 'w') as file:
                for email, contact in self.contacts.items():
                    file.write(f"{email}: {contact}\n")
    def import_contacts(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                for line in file:
                    phone, contact = line.strip().split(': ')
                    self.contacts[phone] = eval(contact)
        else:
            print("File does not exist.")
    def __str__(self):
        return str(self.contacts)
    
def main():
    contact_manager = contacts()
    while True:
        print("\nMenu:")
        print("1. Add new contact")
        print("2. Edit existing contact")
        print("3. Delete contact")
        print("4. Search contacts")
        print("5. Display all contacts")
        print("6. Export contacts to a text file")
        print("7. Import contacts from a text file")
        print("8. Quit")
        choice = input("Enter your choice number: ")
        if choice == '1':
            name = input("Enter the contact's name: ")
            phone = input("Enter the contact's phone number: ")
            email = input("Enter the contact's email address: ")
            additional = input("Enter any additional information: ")
            contact_manager.add_contact(name, phone, email, additional)
        elif choice == '2':
            phone = input("Enter the phone number of the contact to edit: ")
            name = input("Enter the new name: ")
            email = input("Enter the new email address: ")
            additional = input("Enter the new additional information: ")
            contact_manager.edit_contact(email, name, phone, additional)
        elif choice == '3':
            phone = input("Enter the phone number of the contact to delete: ")
            contact_manager.delete_contact(phone)
        elif choice == '4':
            phone = input("Enter the phone number of the contact to search for: ")
            print(contact_manager.search_contact(phone))
        elif choice == '5':
            print(contact_manager.display_contacts())
        elif choice == '6':
            filename = input("Enter the filename to export contacts to: ")
            contact_manager.export_contacts(filename)
        elif choice == '7':
            filename = input("Enter the filename to import contacts from: ")
            contact_manager.import_contacts(filename)
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")
    print("Goodbye!")

if __name__ == '__main__':
    main()
    

