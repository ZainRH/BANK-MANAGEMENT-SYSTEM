import random

class bankmangementsystem():
    def __init__(self, filename="accounts.txt"):
        self.filename = filename
        # Create the file if it doesn't exist
        try:
            with open(self.filename, 'x'): #file check kr rha
                pass
        except FileExistsError:
            pass

    def create_account(self, name, pin):
        account_number = random.randint(100000, 999999)  # Generate a 6-digit account number
        while self.account_exists(account_number):
            account_number = random.randint(100000, 999999) #  Bug resolved by AI
        with open(self.filename, "a") as file:
            file.write(f"{account_number},{name},{pin},0\n")
        print(f"Account created successfully! Your account number is: {account_number}")
        return account_number

    def account_exists(self, account_number):
        with open(self.filename, "r") as file:
            for line in file:
                if line.startswith(f"{account_number},"):
                    return True
        return False

    def get_account(self, account_number, pin=None):
        with open(self.filename, "r") as file:
            for line in file:
                acc_number, name, acc_pin, balance = line.strip().split(",")
                if int(acc_number) == account_number:
                    if pin is None or acc_pin == pin:
                        return {"account_number": acc_number, "name": name, "pin": acc_pin, "balance": float(balance)}
        return None

    def update_account(self, account_number, updated_account):
        lines = []
        with open(self.filename, "r") as file:
            lines = file.readlines()
        with open(self.filename, "w") as file:
            for line in lines:
                acc_number, *_ = line.strip().split(",")
                if int(acc_number) == account_number:
                    file.write(f"{updated_account['account_number']},{updated_account['name']},{updated_account['pin']},{updated_account['balance']}\n")
                else:
                    file.write(line)

#==========================================================================================================================


    def deposit(self, account_number, pin, amount):
        account = self.get_account(account_number, pin)  #account for updation of account
        if account:
            account["balance"] += amount
            self.update_account(account_number, account)
            print(f"Deposited {amount}. New balance: {account['balance']}")
        else:
            print("Invalid account or PIN.")

    def withdraw(self, account_number, pin, amount):
        account = self.get_account(account_number, pin)#poora account return horha get account mein ooper
        if account:
            if account["balance"] >= amount:
                account["balance"] -= amount
                self.update_account(account_number, account)
                print(f"Withdrew {amount}. Remaining balance: {account['balance']}")
            else:
                print("Insufficient balance!")
        else:
            print("Invalid account or PIN.")


    def show_balance(self, account_number, pin):
        account = self.get_account(account_number, pin)
        if account:
            print(f"Your current balance is: {account['balance']}")
        else:
            print("Invalid account or PIN.")

            #Executions
atm = bankmangementsystem()

print("Welcome to the ATM!")
while True:

    
    print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter your name: ")
        pin = input("Set a 4-digit PIN: ")
        if len(pin) == 4 and pin.isdigit():
            atm.create_account(name, pin)
        else:
            print("Invalid PIN format. Please use a 4-digit number.")

    elif choice == "2":
        account_number = int(input("Enter your account number: "))
        pin = input("Enter your PIN: ")
        amount = float(input("Enter amount to deposit: "))
        atm.deposit(account_number, pin, amount)

    elif choice == "3":
        account_number = int(input("Enter your account number: "))
        pin = input("Enter your PIN: ")
        amount = float(input("Enter amount to withdraw: "))
        atm.withdraw(account_number, pin, amount)

    elif choice == "4":
        account_number = int(input("Enter your account number: "))
        pin = input("Enter your PIN: ")
        atm.show_balance(account_number, pin)

    elif choice == "5":
        print("Thank you for using the ATM! Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
