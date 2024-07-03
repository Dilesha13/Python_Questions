#Problem 5: Bank Account Management

def get_balance(account_number: str) -> float:
    # Define a function to get the balance of an account
    with open('problem_5/accounts.txt', 'r') as file:
        # Open the accounts file in read mode
        for line in file:
            # Iterate over each line in the file
            acc_num, balance = line.strip().split(',')
            # Split each line into account number and balance
            if acc_num == account_number:
                # Check if the account number matches the given account number
                return float(balance)
                # Return the balance as a float
    return None
    # If the account number is not found, return None

def update_account(account_number: str, balance: float):
    # Define a function to update the balance of an account
    lines = []
    # Initialize an empty list to store the updated lines
    found = False
    # Initialize a flag to check if the account number is found
    with open('problem_5/accounts.txt', 'r') as file:
        # Open the accounts file in read mode
        for line in file:
            # Iterate over each line in the file
            acc_num, bal = line.strip().split(',')
            # Split each line into account number and balance
            if acc_num == account_number:
                # Check if the account number matches the given account number
                lines.append(f"{acc_num},{balance}\n")
                # Update the balance and add the line to the list
                found = True
            else:
                lines.append(line)
                # Add the line to the list if the account number does not match
    if not found:
        # If the account number is not found, add a new line
        lines.append(f"{account_number},{balance}\n")
    with open('problem_5/accounts.txt', 'w') as file:
        # Open the accounts file in write mode
        file.writelines(lines)
        # Write the updated lines back to the file

def deposit(account_number: str, amount: float):
    # Define a function to deposit money into an account
    balance = get_balance(account_number)
    # Get the current balance of the account
    balance += amount
    # Add the deposit amount to the balance
    update_account(account_number, balance)
    # Update the account with the new balance

def withdraw(account_number: str, amount: float):
    # Define a function to withdraw money from an account
    balance = get_balance(account_number)
    # Get the current balance of the account
    if balance >= amount:
        # Check if the balance is sufficient for the withdrawal
        balance -= amount
        # Subtract the withdrawal amount from the balance
        update_account(account_number, balance)
        # Update the account with the new balance
    else:
        print("Insufficient balance.")
        # Print an error message if the balance is insufficient

# Example usage:
print(get_balance('12345'))  # Output: 1000.0
# Get the balance of account 12345
deposit('12345', 500)
# Deposit 500 into account 12345
print(get_balance('12345'))  # Output: 1500.0
# Get the updated balance of account 12345
withdraw('12345', 300)
# Withdraw 300 from account 12345
print(get_balance('12345'))  # Output: 1200.0
# Get the updated balance of account 12345

