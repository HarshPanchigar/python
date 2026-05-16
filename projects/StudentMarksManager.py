# Features:
# Student name
# marks input
# total
# percentage
# pass/fail

# Learn:
# variables
# maths
# conditions


# Function For Student Name
def stdDetails():
    name = input("Enter Student Name: ")
    return name


# Function For Student Marks
def marks(b):
    stdMarks = []

    for i in range(b):
        mark = int(input(f"Enter Subject {i+1} Marks : "))
        stdMarks.append(mark)

    return stdMarks


# Function For Total
def totalMarks(stdMarks):
    total = sum(stdMarks)
    return total


# Function For Percentage
def percentage(total, totalSubjects):
    per = (total / (totalSubjects * 100)) * 100
    return per


# Function For Pass/Fail
def passFail(per):
    if per >= 33:
        return "Pass"
    else:
        return "Fail"


# Main Program
while True:

    print("\n===== Student Marks Manager =====")
    print("1. Student Name")
    print("2. Marks Input")
    print("3. Student Marks Total")
    print("4. Student Percentage")
    print("5. Pass/Fail Student")
    print("6. Exit")

    try:
        num = int(input("Enter Task No: "))
    except ValueError:
        print("Please enter numbers only")
        continue

    # Exit
    if num == 6:
        print("Program Ended...")
        break

    # Invalid Input
    elif num not in (1, 2, 3, 4, 5, 6):
        print("Invalid Choice...")
        continue

    # Student Name
    elif num == 1:

        name = stdDetails()

        print("\nStudent Name:", name)

    # Marks Input
    elif num == 2:

        subjects = int(input("How Many Subjects: "))

        studentMarks = marks(subjects)

        print("\nStudent Marks:")
        print(studentMarks)

    # Total Marks
    elif num == 3:

        total = totalMarks(studentMarks)

        print("\nTotal Marks:", total)

    # Percentage
    elif num == 4:

        per = percentage(total, subjects)

        print("\nPercentage:", per, "%")

    # Pass / Fail
    elif num == 5:

        result = passFail(per)

        print("\nResult:", result)