class ContactManager:
    def __init__(self):
        self.contacts = [
            ["Guido van Rossum", "guido@python.org", "+31 10 123 4567"],
            ["Eric Idle", "eric@ericidle.com", "+44 20 7946 0958"]
        ]

    def display_contacts(self):
        print("Command: list")
        for i, contact in enumerate(self.contacts, 1):
            print(f"{i}. {contact[0]}")

    def view_contact(self, contact_number):
        try:
            contact_number = int(contact_number)
            contact = self.contacts[contact_number - 1]
            print(f"Command: view\nNumber: {contact_number}\nName: {contact[0]}\nEmail: {contact[1]}\nPhone: {contact[2]}")
        except (ValueError, IndexError):
            print("Invalid contact number. Please try again.")

    def add_contact(self, name, email, phone):
        self.contacts.append([name, email, phone])
        print(f"Command: add\nName: {name} was added.")

    def delete_contact(self, contact_number):
        try:
            contact_number = int(contact_number)
            deleted_contact = self.contacts.pop(contact_number - 1)
            print(f"Command: del\nNumber: {contact_number}\n{deleted_contact[0]} was deleted.")
        except (ValueError, IndexError):
            print("Invalid contact number. Please try again.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Manager\nCOMMAND MENU\nlist - Display all contacts\nview - View a contact\nadd  - Add a contact\ndel  - Delete a contact\nexit - Exit program")
        command = input("Command: ")

        if command == 'list':
            contact_manager.display_contacts()
        elif command == 'view':
            number = input("Number: ")
            contact_manager.view_contact(number)
        elif command == 'add':
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            contact_manager.add_contact(name, email, phone)
        elif command == 'del':
            number = input("Number: ")
            contact_manager.delete_contact(number)
        elif command == 'exit':
            print("Bye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
