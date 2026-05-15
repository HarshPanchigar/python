import random

print("🎯 Number Guessing Game")
level = input("Choose difficulty (Easy/Hard): ").lower()
if level == "easy":
    max_num = 50
else:
    max_num = 100

num = random.randint(1,max_num)
count = 0
while True:
    count += 1
    gusse = int(input(f"Enter number (1-{max_num}): "))
    if gusse < num:
        print("Too short")
    elif gusse > num:
        print("Too High")
    else:
        print("🎉 Correct!")
        print("Number was:", num)
        print(f"You took {count} attempts")
        break