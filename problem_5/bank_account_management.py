def get_balance(account_number: str) -> float:
    with open('problem_5/accounts.txt', 'r') as file:
        for line in file:
            acc_num, balance = line.strip().split(',')
            if acc_num == account_number:
                return float(balance)
    return None

def update_account(account_number: str, balance: float):
    lines = []
    found = False
    with open('problem_5/accounts.txt', 'r') as file:
        for line in file:
            acc_num, bal = line.strip().split(',')
            if acc_num == account_number:
                lines.append(f"{acc_num},{balance}\n")
                found = True
            else:
                lines.append(line)
    if not found:
        lines.append(f"{account_number},{balance}\n")
    with open('problem_5/accounts.txt', 'w') as file:
        file.writelines(lines)

def deposit(account_number: str, amount: float):
    balance = get_balance(account_number)
    balance += amount
    update_account(account_number, balance)

def withdraw(account_number: str, amount: float):
    balance = get_balance(account_number)
    if balance >= amount:
        balance -= amount
        update_account(account_number, balance)
    else:
        print("Insufficient balance.")

# Example usage:
# Assume 'accounts.txt' contains "12345,1000\n67890,1500"
print(get_balance('12345'))  # Output: 1000.0
deposit('12345', 500)
print(get_balance('12345'))  # Output: 1500.0
withdraw('12345', 300)
print(get_balance('12345'))  # Output: 1200.0
