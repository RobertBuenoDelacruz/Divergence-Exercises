import csv

def read_contacts_from_file(filename):
    contacts = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            contacts.append({'Name': row[0], 'Email': row[1], 'Phone': row[2]})
    return contacts

def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for contact in contacts:
            writer.writerow([contact['Name'], contact['Email'], contact['Phone']])

def display_contacts(contacts):
    print("Command: list")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['Name']}")

def view_contact(contacts, number):
    if 1 <= number <= len(contacts):
        contact = contacts[number - 1]
        print(f"Command: view\nName: {contact['Name']}\nEmail: {contact['Email']}\nPhone: {contact['Phone']}")
    else:
        print("Invalid contact number. Please enter a valid number.")

def add_contact(contacts):
    print("Command: add")
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    
    new_contact = {'Name': name, 'Email': email, 'Phone': phone}
    contacts.append(new_contact)
    
    print(f"{name} was added.")
    write_contacts_to_file('contacts.csv', contacts)

def delete_contact(contacts, number):
    if 1 <= number <= len(contacts):
        deleted_contact = contacts.pop(number - 1)
        print(f"Command: del\n{deleted_contact['Name']} was deleted.")
        write_contacts_to_file('contacts.csv', contacts)
    else:
        print("Invalid contact number. Please enter a valid number.")

def main():
    contacts = read_contacts_from_file('contacts.csv')

    while True:
        print("Contact Manager\nCOMMAND MENU\nlist - Display all contacts\nview - View a contact\nadd  - Add a contact\ndel  - Delete a contact\nexit - Exit program")
        command = input("Command: ").lower()

        if command == 'list':
            display_contacts(contacts)
        elif command == 'view':
            number = int(input("Number: "))
            view_contact(contacts, number)
        elif command == 'add':
            add_contact(contacts)
        elif command == 'del':
            number = int(input("Number: "))
            delete_contact(contacts, number)
        elif command == 'exit':
            print("Bye!")
            break
        else:
            print("Invalid command. Please enter a valid command.")

if __name__ == "__main__":
    main()
