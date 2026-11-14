# Import the class used to record transactions.
from transaction import LoadTransaction


# This class manages the cellphone load wallet.
class LoadWallet:
    # Save the owner, number, balance, and transactions.
    def __init__(self, owner, mobile_number, balance):
        self.owner = owner
        self.mobile_number = mobile_number
        self.__balance = balance
        self.transactions = []

    # Add load to the wallet.
    def top_up(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
        else:
            self.__balance += amount
            transaction = LoadTransaction("Top Up", amount)
            self.transactions.append(transaction)
            print(f"New balance: P{self.__balance:.2f}")

    # Send load to a number on the same network.
    def send_load(self, number, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            transaction = LoadTransaction("Send", amount, number)
            self.transactions.append(transaction)
            transaction.display()
            print(f"New balance: P{self.__balance:.2f}")

    # Send load to another network with a service fee.
    def send_with_fee(self, number, amount):
        fee = 5
        transaction = LoadTransaction("Send", amount, number, fee)
        if amount <= 0:
            print("Amount must be greater than zero.")
        elif transaction.total_cost() > self.__balance:
            print("Insufficient balance to cover the load and fee.")
        else:
            self.__balance -= transaction.total_cost()
            self.transactions.append(transaction)
            transaction.display()
            print(f"New balance: P{self.__balance:.2f}")

    # Show the subscriber information and balance.
    def show_balance(self):
        print(f"Owner         : {self.owner}")
        print(f"Mobile Number : {self.mobile_number}")
        print(f"Balance       : P{self.__balance:.2f}")

    # Show all successful transactions.
    def show_history(self):
        if not self.transactions:
            print("No transactions yet.")
        else:
            for transaction in self.transactions:
                transaction.display()
