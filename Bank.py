class Bank_v1:
    # Class attributes
    bank_name = "ABC Bank"
    rate_of_interest = 6.5
    branch_name = "Hyderabad"

    # Instance attributes
    def __init__(self, cust_name, cust_age, acc_no, balance):
        self.cust_name = cust_name
        self.cust_age = cust_age
        self.acc_no = acc_no
        self.balance = balance

    # Instance method
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Current balance: {self.balance}")

    # Instance method
    def customer_det(self):
        print("\n--- Customer Details ---")
        print(f"Name: {self.cust_name}")
        print(f"Age: {self.cust_age}")
        print(f"Account No: {self.acc_no}")
        print(f"Balance: {self.balance}")

    # Class method
    @classmethod
    def bank_det(cls):
        print("\n--- Bank Details ---")
        print(f"Bank: {cls.bank_name}")
        print(f"Branch: {cls.branch_name}")
        print(f"Rate of Interest: {cls.rate_of_interest}%")

    # Instance method
    def withdraw(self):
        amount = self.get_int_value("Enter withdrawal amount: ")
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful! Remaining balance: {self.balance}")
        else:
            print("Insufficient funds!")

    # Static method
    @staticmethod
    def get_int_value(prompt="Enter a number: "):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input! Please enter a valid integer.")


# Derived Class
class Bank_v2(Bank_v1):
    # New Class attributes
    branch_name = "Mumbai"
    bank_mobile = "9876543210"

    # Extended __init__
    def __init__(self, cust_name, cust_age, acc_no, balance, pin):
        super().__init__(cust_name, cust_age, acc_no, balance)
        self.pin = pin

    # Overridden method
    def customer_det(self):
        super().customer_det()
        print(f"PIN: {self.pin}")

    # Overridden method
    @classmethod
    def bank_det(cls):
        super().bank_det()
        print(f"Bank Mobile: {cls.bank_mobile}")

    # Overridden withdraw with PIN validation
    def withdraw(self):
        entered_pin = self.get_int_value("Enter your PIN: ")
        if entered_pin == self.pin:
            super().withdraw()
        else:
            print("Invalid PIN!")


# ---------------- DEMONSTRATION ----------------
if __name__ == "__main__":
    # Create one object of Bank_v2
    cust1 = Bank_v2("John Doe", 30, "1234567890", 1000, 1234)
    # Show details
    cust1.customer_det()
    cust1.bank_det()

    # Deposit example
    cust1.deposit(500)

    # Withdraw example
    cust1.withdraw()
