class BankAccount:
    
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited")
        else:
            print("invalid amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("invalid amount.")

        elif amount > self.balance:
            print("insufficient balance.")

        else:
            self.balance -= amount
            print("Amount withdraw.")

    def show_balance(self):
        print("Account holder:", self.name)
        print("balance:", self.balance)


name = input("Enter your name: ")


account = BankAccount(name)

while True:
    print("\n--- BANKING SYSTEM ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")


    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.show_balance()

    elif choice == "4":
        break
