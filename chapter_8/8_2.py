import random
import os

def read_inventory_file():
    try:
        with open("wizard_all_items.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("Could not find inventory file!")
        return []

def read_current_inventory():
    try:
        with open("wizard_inventory.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("Inventory file not found. Starting with no inventory.")
        return []

def write_inventory(items):
    with open("wizard_inventory.txt", "w") as file:
        for item in items:
            file.write(item + '\n')

def wizard_inventory():
    all_items = read_inventory_file()
    current_inventory = read_current_inventory()

    while True:
        print("\nThe Wizard Inventory program")
        print("COMMAND MENU")
        print("walk - Walk down the path")
        print("show - Show all items")
        print("drop - Drop an item")
        print("exit - Exit program")

        command = input("Command: ").lower()

        if command == "walk":
            remaining_items = [item for item in all_items if item not in current_inventory]
            if not remaining_items:
                print("You've grabbed all available items!")
            else:
                random_item = random.choice(remaining_items)
                print(f"While walking down a path, you see a {random_item}.")
                grab = input("Do you want to grab it? (y/n): ").lower()
                if grab == "y":
                    current_inventory.append(random_item)
                    print(f"You picked up a {random_item}.")
                    write_inventory(current_inventory)

        elif command == "show":
            for i, item in enumerate(current_inventory, 1):
                print(f"{i}. {item}")

        elif command == "drop":
            try:
                item_number = int(input("Number: "))
                if item_number < 1 or item_number > len(current_inventory):
                    print("Invalid item number.")
                    continue

                dropped_item = current_inventory.pop(item_number - 1)
                print(f"You dropped {dropped_item}.")
                write_inventory(current_inventory)

            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        elif command == "exit":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    wizard_inventory()
