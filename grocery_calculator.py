qty_Item1 = int(input("Enter quantity of item 1: "))
price_Item1 = float(input("Enter price of item 1: "))
qty_Item2 = int(input("Enter quantity of item 2: "))
price_Item2 = float(input("Enter price of item 2: "))

subtotal = qty_Item1 * price_Item1 + qty_Item2 * price_Item2
tax = subtotal * 0.07
grand_total = subtotal + tax

print("Subtotal: ${:.2f}".format(subtotal))
print("Tax: ${:.2f}".format(tax))
print("Grand Total: ${:.2f}".format(grand_total))