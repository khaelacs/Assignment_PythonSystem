# This class stores the details of one load transaction.
class LoadTransaction:
    # Save the transaction type, amount, recipient, and fee.
    def __init__(self, transaction_type, amount, recipient="", fee=0):
        self.transaction_type = transaction_type
        self.amount = amount
        self.recipient = recipient
        self.fee = fee

    # Calculate the amount to deduct from the wallet.
    def total_cost(self):
        return self.amount + self.fee

    # Display the details of a transaction.
    def display(self):
        if self.transaction_type == "Top Up":
            print(f"Top Up: P{self.amount:.2f}")
        else:
            print(f"P{self.amount:.2f} sent to {self.recipient}.")
            if self.fee > 0:
                print(f"Service fee: P{self.fee:.2f}")
