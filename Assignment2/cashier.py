import time

class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        total = 0
        total += int(input("How many quarters?: ")) * 0.25
        total += int(input("How many dimes?: ")) * 0.10
        total += int(input("How many nickels?: ")) * 0.05
        total += int(input("How many pennies?: ")) * 0.01
        return total

    def transaction_result(self, coins, cost):
        if coins >= cost:
            change = coins - cost
            if change > 0:
                print(f"Here is ${change:.2f} in change. Your meal will be ready soon!")
            elif change == 0:
                print(f"Exact change paid. Your meal will be ready soon!")
            time.sleep(2)
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False