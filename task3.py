# Task 3: Bank Account System using Object-Oriented Programming (OOP)

class Customer:
    """Represents a bank customer."""
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id

    def display_customer_info(self):
        print(f"Customer Name : {self.name}")
        print(f"Customer ID   : {self.customer_id}")


class Account:
    """Represents a bank account associated with a customer."""
    def __init__(self, account_number, customer, initial_balance=0.0):
        self.account_number = account_number
        self.customer = customer
        self.balance = float(initial_balance)
        print(f"Account successfully created for {self.customer.name} with Account Number: {self.account_number}")

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited: Rs. {amount:,.2f}")
            print(f"New Balance: Rs. {self.balance:,.2f}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print(f"Transaction failed! Insufficient balance. Available Balance: Rs. {self.balance:,.2f}")
        else:
            self.balance -= amount
            print(f"Successfully withdrawn: Rs. {amount:,.2f}")
            print(f"Remaining Balance: Rs. {self.balance:,.2f}")

    def display_balance(self):
        """Display the current balance and account details."""
        print("-" * 40)
        print("          ACCOUNT DETAILS")
        print("-" * 40)
        self.customer.display_customer_info()
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: Rs. {self.balance:,.2f}")
        print("-" * 40)


def main():
    print("=" * 45)
    print("         Bank Account System Demo")
    print("=" * 45)

    # 1. Create a customer
    customer1 = Customer(name="Ali Khan", customer_id="CUST-1001")

    # 2. Create a customer account
    account1 = Account(account_number="PK-BA-98765", customer=customer1, initial_balance=10000.0)

    # 3. Display initial balance
    print("\n[Step 1: Check Initial Balance]")
    account1.display_balance()

    # 4. Deposit money
    print("\n[Step 2: Deposit Money]")
    account1.deposit(15000.0)

    # 5. Withdraw money
    print("\n[Step 3: Withdraw Money]")
    account1.withdraw(5000.0)

    # 6. Attempt invalid withdrawal (more than balance)
    print("\n[Step 4: Attempt Over-withdrawal]")
    account1.withdraw(50000.0)

    # 7. Display current balance
    print("\n[Step 5: Final Balance Check]")
    account1.display_balance()


if __name__ == "__main__":
    main()
