# restaurant_order.py
# Refactored restaurant ordering program using functions

TAX_RATE = 0.07  # 7% sales tax


def display_menu(menu):
    """Print the menu items and their prices."""
    print("Welcome to the Restaurant!")
    print("Here is the menu:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")


def take_order(menu):
    """Collect user order and return a dictionary of items to quantities."""
    order = {}

    while True:
        choice = input("\nEnter an item to order (or 'done' to finish): ").title()
        
        if choice == "Done":
            break
        elif choice in menu:
            qty = input(f"How many {choice}s would you like? ")
            
            if qty.isdigit():
                qty = int(qty)
                if choice in order:
                    order[choice] += qty
                else:
                    order[choice] = qty
                print(f"Added {qty} {choice}(s) to your order.")
            else:
                print("Please enter a valid number.")
        else:
            print("Sorry, that item is not on the menu.")

    return order


def calculate_total(order, menu):
    """Calculate subtotal, tax, and total."""
    subtotal = 0.0
    for item, qty in order.items():
        subtotal += menu[item] * qty

    tax = subtotal * TAX_RATE
    total = subtotal + tax

    return subtotal, tax, total


def print_receipt(order, menu, subtotal, tax, total):
    """Print the receipt."""
    print("\n------ Receipt ------")
    for item, qty in order.items():
        print(f"{item} x{qty} = ${menu[item] * qty:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")
    print("---------------------")
    print("Thank you for dining with us!")


def main():
    menu = {
        "Burger": 8.50,
        "Fries": 3.00,
        "Salad": 4.75,
        "Soda": 1.50,
        "Ice Cream": 2.75
    }

    display_menu(menu)
    order = take_order(menu)
    subtotal, tax, total = calculate_total(order, menu)
    print_receipt(order, menu, subtotal, tax, total)


# Run the program
main()