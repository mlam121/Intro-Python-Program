qty_item1 = int(input("Enter quantity of item 1: "))
price_item1 = float(input("Enter price of item 1: "))
qty_item2 = int(input("Enter quantity of item 2: "))
price_item2 = float(input("Enter price of item 2: "))

subtotal = qty_item1 * price_item1 + qty_item2 * price_item2
tax = subtotal * 0.07
grand_total = subtotal + tax

print("Subtotal: ${:.2f}".format(subtotal))
print("Tax: ${:.2f}".format(tax))
print("Grand Total: ${:.2f}".format(grand_total))