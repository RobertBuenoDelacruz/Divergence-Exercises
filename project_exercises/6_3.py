import csv

FILENAME = "contacts.csv"

def read_contacts_from_file():
    try:
        with open(FILENAME, 'r', newline='') as file:
            reader = csv.reader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []

def write_contacts_to_file(contacts):
    with open(FILENAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

def display_contacts(contacts):
    print("Command: list")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact[0]}")

def view_contact(contacts, contact_number):
    try:
        contact_number = int(contact_number)
        contact = contacts[contact_number - 1]
        print(f"Command: view\nNumber: {contact_number}\nName: {contact[0]}\nEmail: {contact[1]}\nPhone: {contact[2]}")
    except (ValueError, IndexError):
        print("Invalid contact number. Please try again.")

def add_contact(contacts, name, email, phone):
    new_contact = [name, email, phone]
    contacts.append(new_contact)
    write_contacts_to_file(contacts)
    print(f"Command: add\nName: {name} was added.")

def delete_contact(contacts, contact_number):
    try:
        contact_number = int(contact_number)
        deleted_contact = contacts.pop(contact_number - 1)
        write_contacts_to_file(contacts)
        print(f"Command: del\nNumber: {contact_number}\n{deleted_contact[0]} was deleted.")
    except (ValueError, IndexError):
        print("Invalid contact number. Please try again.")

def main():
    contacts = read_contacts_from_file()

    while True:
        print("\nContact Manager\nCOMMAND MENU\nlist - Display all contacts\nview - View a contact\nadd  - Add a contact\ndel  - Delete a contact\nexit - Exit program")
        command = input("Command: ")

        if command == 'list':
            display_contacts(contacts)
        elif command == 'view':
            number = input("Number: ")
            view_contact(contacts, number)
        elif command == 'add':
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            add_contact(contacts, name, email, phone)
        elif command == 'del':
            number = input("Number: ")
            delete_contact(contacts, number)
        elif command == 'exit':
            print("Bye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
