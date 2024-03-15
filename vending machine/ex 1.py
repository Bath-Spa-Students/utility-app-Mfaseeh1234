class VendingMachine:
    def __init__(self):
        self.menu = {
            'Snacks': {'Chips': {'price': 1.50, 'quantity': 10},
                       'Chocolate': {'price': 1.00, 'quantity': 8},
                       'Candy Bar': {'price': 1.25, 'quantity': 12},
                       'Pretzels': {'price': 1.75, 'quantity': 5},
                       'Granola Bar': {'price': 2.00, 'quantity': 7}},
            'Drinks': {'Water': {'price': 1.00, 'quantity': 15},
                       'Soda': {'price': 1.50, 'quantity': 10},
                       'Juice': {'price': 2.00, 'quantity': 8},
                       'Coffee': {'price': 2.50, 'quantity': 6},
                       'Tea': {'price': 1.75, 'quantity': 9}}
        }
        self.balance = 0.0

    def display_menu(self):
        print("=== Vending Machine Menu ===")
        for category, items in self.menu.items():
            print(f"\n{category}:")
            for item, details in items.items():
                price = details['price']
                quantity = details['quantity']
                availability = f" (Available: {quantity})"
                status = "" if quantity > 0 else " - Sold Out"
                print(f"{item}: AED{price:.2f}{availability}{status}")

    def insert_money(self):
        while True:
            try:
                money = float(input("Insert money (in DHS): "))
                if money >= 0:
                    self.balance += money
                    print(f"Current balance: AED{self.balance:.2f}")
                    break
                else:
                    print("Please enter a valid amount.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def select_item(self):
        while True:
            self.display_menu()
            choice = input("Enter the name of the item you want to purchase (or 'exit' to end): ").capitalize()

            if choice == 'Exit':
                break

            found_item = False
            for category, items in self.menu.items():
                if choice in items:
                    found_item = True
                    details = items[choice]
                    price = details['price']
                    quantity = details['quantity']

                    try:
                        requested_quantity = int(input(f"How many {choice}s do you want to buy? Enter quantity: "))
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                        continue

                    if quantity >= requested_quantity and self.balance >= price * requested_quantity:
                        self.balance -= price * requested_quantity
                        self.menu[category][choice]['quantity'] -= requested_quantity
                        print(f"\nYou purchased {requested_quantity} {choice}s for AED{price * requested_quantity:.2f}.")
                        print(f"Remaining balance: AED{self.balance:.2f}")
                    elif quantity == 0:
                        print(f"Sorry, {choice} is sold out. Please choose another item.")
                    elif quantity < requested_quantity:
                        print(f"Sorry, only {quantity} {choice}s are available.")
                    else:
                        print("Insufficient funds. Please insert more money.")
                    break

            if not found_item:
                print("Invalid item. Please choose from the menu.")

    def return_change(self):
        if self.balance > 0:
            print(f"\nReturning change: AED{self.balance:.2f}")
            self.balance = 0.0
        print("\nThank you for using the vending machine!")


def main():
    vending_machine = VendingMachine()
    vending_machine.insert_money()
    vending_machine.select_item()
    vending_machine.return_change()


if __name__ == "__main__":
    main()