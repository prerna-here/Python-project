import os

PIN = "1234"
DEFAULT_BALANCE = 10000


BALANCE_FILE = "atm.txt"
TRANSACTION_FILE = "transactions.txt"



def load_balance():
    try:
        if os.path.exists(BALANCE_FILE):
            with open(BALANCE_FILE, "r") as file:
                return float(file.read())
        else:
            return DEFAULT_BALANCE

    except (ValueError, OSError):
        print("Error reading balance file.")
        return DEFAULT_BALANCE


def save_balance(balance):
    try:
        with open(BALANCE_FILE, "w") as file:
            file.write(str(balance))
    except OSError:
        print("Error saving balance.")



def save_transaction(message):
    try:
        with open(TRANSACTION_FILE, "a") as file:
            file.write(message + "\n")
    except OSError:
        print("Error saving transaction.")



def check_balance(balance):
    print("Your current balance is:", balance)
    save_balance(balance)



def deposit(balance):
    try:
        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            print("Please enter a valid amount.")
        else:
            balance += amount
            print("Deposit successful. New Balance:", balance)

            save_balance(balance)
            save_transaction("Deposited: " + str(amount))

    except ValueError:
        print("Invalid amount. Please enter numbers only.")

    return balance


def withdraw(balance):
    try:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Please enter a valid amount.")

        elif amount > balance:
            print("Insufficient balance.")

        else:
            balance -= amount
            print("Withdrawal successful. New Balance:", balance)

            save_balance(balance)
            save_transaction("Withdrawn: " + str(amount))

    except ValueError:
        print("Invalid amount. Please enter numbers only.")

    return balance


def mini_statement():
    print("\n----- MINI STATEMENT -----")

    try:
        if os.path.exists(TRANSACTION_FILE):
            with open(TRANSACTION_FILE, "r") as file:
                transactions = file.readlines()

            if transactions:
                for transaction in transactions[-5:]:
                    print(transaction.strip())
            else:
                print("No transactions found.")
        else:
            print("No transactions found.")

    except OSError:
        print("Error reading transaction file.")



def main():

    balance = load_balance()

    print("================================")
    print("       WELCOME TO ATM")
    print("================================")

    attempts = 3
    login = False

    while attempts > 0:

        entered_pin = input("Enter your PIN: ")

        if entered_pin == PIN:
            print("Login successful!")
            login = True
            break

        else:
            attempts -= 1
            print("Invalid PIN. Attempts left:", attempts)

    if not login:
        print("Account locked. Exiting...")
        return


    while True:

        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Mini Statement")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(balance)

        elif choice == "2":
            balance = deposit(balance)

        elif choice == "3":
            balance = withdraw(balance)

        elif choice == "4":
            mini_statement()

        elif choice == "5":
            save_balance(balance)
            print("Thank you for using ATM.")
            print("Please visit again!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()