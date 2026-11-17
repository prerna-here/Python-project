ATM Management System

Project Description

The ATM Management System is a menu-driven Python 3 application that simulates basic ATM operations. It allows users to log in using a PIN and perform banking operations such as checking balance, depositing money, withdrawing money, and viewing a mini statement.

Features

- PIN-based login authentication.
- Maximum 3 attempts for entering the correct PIN.
- Check account balance.
- Deposit money into the account.
- Withdraw money from the account.
- View mini statement.
- Validate user inputs and handle invalid entries.
- Store account balance and transaction details in a file.
- Handle exceptions using try-except.

Technologies Used

- Python 3
- File Handling
- Conditional Statements
- Loops
- Functions
- Exception Handling

Default Account Details

- Default PIN: 1234
- Opening Balance: ₹10,000
- Data File: atm.txt

How to Run the Project

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Make sure Python 3 is installed.
4. Open the terminal.
5. Run the following command:

python atm.py

Test Cases

The project is tested using the following scenarios:

1. Normal Input: Deposit ₹5,000 and check the updated balance.
2. Boundary Input: Withdraw the entire available balance.
3. Invalid Input: Enter an incorrect PIN three times.
4. Different Valid Scenarios: Test invalid withdrawal amounts, successful withdrawals, and mini statements.

Expected Outcome

The system successfully performs ATM operations, validates user inputs, maintains account balance, and records transactions in a file.

Author

Developed as a Python 3 academic project.
