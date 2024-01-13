import random

INVENTORY_FILE = "wizard_inventory.txt"
ALL_ITEMS_FILE = "wizard_all_items.txt"

def load_inventory():
    try:
        with open(INVENTORY_FILE, 'r') as file:
            return [item.strip() for item in file.readlines()]
    except FileNotFoundError:
        return []

def save_inventory(inventory):
    with open(INVENTORY_FILE, 'w') as file:
        for item in inventory:
            file.write(f"{item}\n")

def load_all_items():
    try:
        with open(ALL_ITEMS_FILE, 'r') as file:
            return [item.strip() for item in file.readlines()]
    except FileNotFoundError:
        return []

def show_inventory(inventory):
    if not inventory:
        print("Your inventory is empty.")
    else:
        for i, item in enumerate(inventory, 1):
            print(f"{i}. {item}")

def walk(inventory):
    all_items = load_all_items()
    new_items = [item for item in all_items if item not in inventory]

    if not new_items:
        print("You've already found all available items.")
        return

    random_item = random.choice(new_items)
    print(f"While walking down a path, you see {random_item}. Do you want to grab it? (y/n): ", end='')
    choice = input().lower()

    if choice == 'y':
        if len(inventory) == 4:
            print("You can't carry any more items. Drop something first.")
        else:
            inventory.append(random_item)
            print(f"You picked up {random_item}.")
            save_inventory(inventory)

def drop(inventory):
    show_inventory(inventory)
    if not inventory:
        return

    try:
        item_number = int(input("Number: "))
        if 1 <= item_number <= len(inventory):
            dropped_item = inventory.pop(item_number - 1)
            print(f"You dropped {dropped_item}.")
            save_inventory(inventory)
        else:
            print("Invalid item number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid item number.")

def main():
    inventory = load_inventory()

    while True:
        print("\nThe Wizard Inventory program\nCOMMAND MENU\nwalk - Walk down the path\nshow - Show all items\ndrop - Drop an item\nexit - Exit program")
        command = input("Command: ")

        if command == 'walk':
            walk(inventory)
        elif command == 'show':
            show_inventory(inventory)
        elif command == 'drop':
            drop(inventory)
        elif command == 'exit':
            print("Bye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
