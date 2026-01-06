customer = {}

def add_Customer(account_number, name, balance):
    if account_number in customer:
        print("Customer already exists!")
    else:
        customer[account_number] = {
            "name": name,
            "Balance": balance
        }
        print("Customer added successfully")


def display_customer(account_number):
    if account_number in customer:
        print(f"Account Number : {account_number}")
        print(f"Account Name   : {customer[account_number]['name']}")
        print(f"Balance        : {customer[account_number]['Balance']}")
    else:
        print("Customer not found!")


def update_bal(account_number, amount, transaction_type):
    if account_number in customer:
        if transaction_type == "deposit":
            customer[account_number]["Balance"] += amount
            print("Amount deposited successfully")

        elif transaction_type == "withdraw":
            if customer[account_number]["Balance"] >= amount:
                customer[account_number]["Balance"] -= amount
                print("Amount withdrawn successfully")
            else:
                print("Insufficient balance!")

        else:
            print("Invalid transaction type!")
    else:
        print("Customer not found!")



add_Customer(101, "Rohan", 10000)
display_customer(101)
update_bal(101, 2000, "deposit")
update_bal(101, 3000, "withdraw")
display_customer(101)
