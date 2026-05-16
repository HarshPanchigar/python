def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

while True:
    print("Choose calculation")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit\n")

    try:
        cal = int(input("What do you want to perform? "))
    except ValueError:
        print("Please enter numbers only")
        continue

    if cal == 5:
        break
    elif cal not in [1,2,3,4,5]:
        print("Invalid number")
        print("\n")
        continue

    try:
        num1 = int(input("Enter First Number: "))
        num2 = int(input("Enter Second Number: "))
    except ValueError:
        print("Please enter valid numbers\n")
        continue

    if cal == 1:
        result = add(num1, num2)
        print("Result:", result)
        print("\n")
    elif cal == 2:
        result = subtract(num1,num2)
        print("Result:",result)
        print("\n")
    elif cal == 3:
        result = multiply(num1,num2)
        print("Result:",result)
        print("\n")
    elif cal == 4:
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            result = divide(num1,num2)
            print("Result:",result)
        print("\n")