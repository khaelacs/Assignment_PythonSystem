# Import the class for the cellphone load wallet.
from load_wallet import LoadWallet


# Ask for a valid amount.
def get_amount(message, allow_zero=False):
    while True:
        text = input(message).strip().replace("₱", "").replace("P", "").replace("p", "")
        try:
            amount = float(text)
            if amount > 0 or (allow_zero and amount == 0):
                return amount
            print("Please enter a valid amount.")
        except ValueError:
            print("Please enter a number, like 50 or P50.")


# Get the subscriber information.
owner = input("Enter owner name: ")
mobile_number = input("Enter mobile number: ")
balance = get_amount("Enter starting balance: ", True)
wallet = LoadWallet(owner, mobile_number, balance)

# Display the menu.
print("\n----- MENU -----")
print("1. Top Up Load")
print("2. Send Load (same network)")
print("3. Send Load (other network, with fee)")
print("4. Show Balance")
print("5. Exit")

# Keep the menu running until the user exits.
while True:
    choice = input("\nChoose an option (1-5): ")

    if choice == "1":
        amount = get_amount("Enter top-up amount: ")
        wallet.top_up(amount)
    elif choice == "2":
        number = input("Enter recipient number: ")
        amount = get_amount("Enter load amount: ")
        wallet.send_load(number, amount)
    elif choice == "3":
        number = input("Enter recipient number: ")
        amount = get_amount("Enter load amount: ")
        wallet.send_with_fee(number, amount)
    elif choice == "4":
        wallet.show_balance()
    elif choice == "5":
        print("Thank you for using Cellphone Load Wallet!")
        break
    else:
        print("Invalid option. Please choose 1 to 5.")
