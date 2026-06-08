class BankAccount:
    def __init__(self,balance = 0):
        self.__balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}$")
        else:
            print("Invalid deposit amount")
    
    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw: {amount}$")
            print(f"account balance : {self.__balance}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance
    

account = BankAccount()

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        depo = int(input("Enter Depisit Amout: "))
        account.deposit(depo)
    elif choice == 2:
        wdw = int(input("Enter Withdraw Amount: "))
        account.withdraw(wdw)
    elif choice == 3:
        print("Current Balance: ",account.get_balance(),"$")
    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid Choice")