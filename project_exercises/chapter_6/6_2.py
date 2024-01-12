MAX_ITEMS = 4

def show(items):
    if not items:
        print("There is no list to show.\n")
    else:
        for i, item in enumerate(items, start=1):
            print(f"{i}. {item}")
    print()

def grab(items):
    if len(items) >= MAX_ITEMS:
        print("You can't carry any more items. Drop something first.\n")
    else:
        item_name = input("Name: ")
        items.append(item_name)
        print(f"{item_name} was added.\n")

def edit(items):
    show(items)
    if not items:
        return

    try:
        index = int(input("Number: ")) - 1
        if 0 <= index < len(items):
            new_name = input("Updated name: ")
            items[index] = new_name
            print(f"Item number {index + 1} was updated.\n")
        else:
            print("Invalid number. Please try again.\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")

def drop(items):
    show(items)
    if not items:
        return

    try:
        index = int(input("Number: ")) - 1
        if 0 <= index < len(items):
            dropped_item = items.pop(index)
            print(f"{dropped_item} was dropped.\n")
        else:
            print("Invalid number. Please try again.\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")

def display_menu():
    print("The Wizard Inventory program")
    print("COMMAND MENU")
    print("show - Show all items")
    print("grab - Grab an item")
    print("edit - Edit an item")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()

def main():
    items = ["wooden staff", "wizard hat", "cloth shoes"]

    display_menu()

    while True:
        command = input("Command: ")
        if command.lower() == "show":
            show(items)
        elif command.lower() == "grab":
            grab(items)
        elif command.lower() == "edit":
            edit(items)
        elif command.lower() == "drop":
            drop(items)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")

    print("Bye!")

if __name__ == "__main__":
    main()
