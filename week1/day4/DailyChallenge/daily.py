# You were hired to help a small coffee shop manage their product menu using Python.
# Write a program that:

#1. Stores the coffee shop menu in memory
#2. Lets the user:

# Create a new item
# Read (view) all items
# Update an item’s price
# Delete an item
# Exit
# Your program must be organized with functions.
# Do not write all the logic in one giant while loop.
# You should split behavior into reusable functions.
# 1. Data structure
# We will represent the menu using a dictionary called menu.
# The key is the drink name (string)
# The value is the price (float)
# Example starting data (you MUST start with this so tests are consistent):
#
# menu = {
#    "espresso": 7.0,
#    "latte": 12.0,
#    "cappuccino": 10.0
#}
#2. Required functions
# You must implement the following functions.
# a) show_menu(menu_dict)
# Input: the dictionary
# Output: prints all items in the format drink - price₪
# If the menu is empty, print: "The menu is empty."
# Example:
# 
# Current menu:
# espresso - 7.0₪
# latte - 12.0₪
# cappuccino - 10.0₪
# This function only prints. It does not return anything.
# b) add_item(menu_dict)
# Ask the user for:
# drink name
# price
# Add it to the dictionary.
# If the drink already exists, print "Item already exists!" and do not change the price.
# Example interaction:
# Enter new drink name: mocha
# Enter price: 14
# "mocha" added!
# This function mutates the dictionary. It does not return anything.
# c) update_price(menu_dict)
# Ask the user which drink they want to update.
# If it exists:
# ask for the new price
# update it
# print: "Price updated!"
# If it doesn’t exist:
# print: "Item not found."
# d) delete_item(menu_dict)
# Ask the user which drink to remove.
# If it exists:
# delete it from the dict
# print: "Item deleted."
# Otherwise:
# print: "Item not found."
# e) show_options()
# Prints the main menu of actions for the user:
# What would you like to do?
# 1. Show menu
# 2. Add item
# 3. Update price
# 4. Delete item
# 5. Exit
# Only prints. Doesn’t return anything.

#f) run_coffee_shop()
#This is the main controller of the program.

#Behavior:
#Keep running in a loop.
#Show options.
# Ask the user to choose (1-5).
# Depending on the choice, call the correct function.
# Rules:
# Invalid choice → print "Invalid choice, try again."
# Choice 5 stops the loop and prints "Goodbye!"

# Initial data
menu = {
    "espresso": 7.0,
    "latte": 12.0,
    "cappuccino": 10.0
}

def show_menu(menu_dict):
    """Print all drinks and prices."""
    print("Current menu:")
    for item, price in menu.items():
        print(f"{item} - {price}₪")

def add_item(menu_dict):
    """Add a new drink to the menu."""
    print("Enter new drink name: ", end="")
    drink_name = input().strip()
    if drink_name in menu_dict:
        print("Item already exists!")
        return
    print("Enter price: ", end="")
    try:
        price = float(input().strip())
    except ValueError:
        print("Invalid price. Item not added.")
        return
    menu[drink_name] = price
    print(f'"{drink_name}" added!')


def update_price(menu_dict):
    """Change the price of an existing drink."""
    print("Enter drink name to update: ", end="")
    drink_name = input().strip()
    if drink_name not in menu_dict:
        print("Item not found.")
        return
    print("Enter new price: ", end="")
    try:
        new_price = float(input().strip())
        if new_price < 0:
            raise ValueError
    except ValueError:
        print("Invalid price. Price not updated.")
        return
    menu[drink_name] = new_price
    print("Price updated!")


def delete_item(menu_dict):
    """Remove a drink from the menu."""
    print("Enter drink name to delete: ", end="")
    drink_name = input().strip()
    if drink_name not in menu_dict:
        print("Item not found.")
        return
    del menu[drink_name]
    print("Item deleted.")

def search_item(menu_dict, drink_name):
    """Check if a drink exists in the menu."""
    if drink_name in menu_dict:
        print(f"{drink_name} is available at {menu_dict[drink_name]}₪")
    else:
        print("Item not found.")

def show_options():
    """Print the available actions."""
    print("What would you like to do?"
          "\n1. Show menu"
          "\n2. Add item"
          "\n3. Update price"
          "\n4. Delete item"
          "\n5. Exit"
          "\n6. Search item")


def run_coffee_shop():
    """Main loop of the program."""
    # TODO
    while True:
    # Steps:
        show_options()
    #   get user choice
        command = input("Enter your choice (1-6): ")
    #   if 5 -> print("Goodbye!") and break
        if command == '5':
            print("Goodbye!")
            break
    #   elif 1,2,3,4 -> call the corresponding function
        elif command in ['1', '2', '3', '4','6']:
            if command == '1':
                show_menu(menu)
            elif command == '2':
                add_item(menu)
            elif command == '3':
                update_price(menu)
            elif command == '4':
                delete_item(menu)
            elif command == '6': 
                print("Enter drink name to search: ", end="")
                drink_name = input().strip()
                search_item(menu, drink_name)
    #   else -> print invalid choice
        else:
            print("Invalid choice, try again.")
            


# Start the program
run_coffee_shop()