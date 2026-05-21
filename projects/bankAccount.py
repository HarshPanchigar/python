class BankAccount:
    def __init__(self):
        self.amount = 0
        
    def deposit(self,amount):
        self.amount += amount
        print("Deposite Amount: ",amount)
        print("Current Balance: ", self.amount)
    def withdraw(self,withdraw):
        self.amount -= withdraw
        print("You withdraw amount: ",withdraw)
        print("Current Balance: ", self.amount)

    def show_balance(self):
        print("Your balance is: ",self.amount)

obj = BankAccount()
while True:
    print("\n\n----------Welcome to Bank----------\n")
    print("1. Deposit Amount")
    print("2. Withdraw Amount")
    print("3. Check Balance")
    print("4. Exit")

    choose = int(input("\n--> "))
    if choose == 1:
        deposite = int(input("Enter your deposit amount: "))
        obj.deposit(deposite)

    elif choose == 2:
        withdraw = int(input("How much amount you want to withdraw: "))
        obj.withdraw(withdraw)

    elif choose == 3:
        obj.show_balance()

    elif choose == 4:
        print("Thank You!")
        break
    else:
        print("Invalid choice")