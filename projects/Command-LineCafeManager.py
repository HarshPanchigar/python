import random

# Menu dictionary
menu = {
    "pizza": 20.00,
    "burger": 15.25,
    "coffee": 10.00
}

# Cart list
cart = []

# Lambda for formatting price
format_price = lambda x: f"${x:.2f}"


# Calculate subtotal
def calculate_subtotal(cart):
    return sum(cart)


# Apply discount
discount = 10

def apply_discount(subtotal):
    return subtotal - (subtotal * (discount / 100))


# Fibonacci recursion for loyalty points
def fibonacci_points(n):

    if n == 0:
        return 0

    elif n == 1:
        return 1

    return fibonacci_points(n - 1) + fibonacci_points(n - 2)


# Receipt function
def generate_receipt(*args, **kwargs):

    print("\n------ RECEIPT ------")

    print("\nMessages:")

    for message in args:
        print(message)

    print("\nCustomer Details:")

    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Take customer name
customer_name = input("Enter your name: ")

# Random table number
table_number = random.randint(1, 10)

print(f"\nWelcome {customer_name}!")
print(f"Your table number is: {table_number}")


# Main loop
while True:

    print("\nType 'menu' to see options or 'done' to finish.")

    userInput = input().lower()

    if userInput == "menu":

        print("\n------ MENU ------")

        for name, value in menu.items():
            print(f"{name:<10} {format_price(value)}")

        # Take all food names at once
        items = input(
            "\nEnter FOOD NAMES separated by space:\n"
        ).lower().split()

        for itemName in items:

            if itemName in menu:

                cart.append(menu[itemName])

                print(f"{itemName} added to cart!")

            else:
                print(f"{itemName} not found!")

        # Bill section
        subtotal = calculate_subtotal(cart)

        discounted_total = apply_discount(subtotal)

        points = fibonacci_points(len(cart))

        print("\n------ BILL ------")

        print(f"Subtotal: {format_price(subtotal)}")

        print(f"Discounted Total: {format_price(discounted_total)}")

        print(f"Loyalty Points Earned: {points}")

        # Receipt
        generate_receipt(
            "Thank you for coming!",
            "Please leave a review!",
            customer=customer_name,
            table=table_number,
            total_items=len(cart)
        )

        break

    elif userInput == "done":

        print("""
Thank you for coming!
Please leave a review!
""")

        break

    else:
        print("Invalid input!")