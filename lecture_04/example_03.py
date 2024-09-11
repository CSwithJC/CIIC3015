# Cashier example that keeps track of the total per item and prints out the
# total after you are done scanning everything.

total_price = 0
item_number = 1

while True:
    price = float(input(f"Please enter the price of item {item_number}: "))
    item_number += 1
    total_price += price

    have_more_items = input("Do you have more items to scan? (y/n) ")
    if have_more_items == "n":
        break

print(f"Your total price is {total_price}.")

# Enter a number and print it if it is positive. Otherwise, tell the user to try again. 0 breaks the loop
# and ends the program.
while True:
    number = int(input("Enter a positive number (0 to quit): "))
    if number == 0:
        break
    elif number < 0:
        print("This number is negative, please try again.")
        continue
    print(number)
