# Created by Jaden Shaw 801292597

# Imports
import time

# Data
recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}

# Functions
class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input."""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        for item in ingredients:
            if ingredients[item] > self.machine_resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        print("Please insert coins.")
        total = 0
        total += int(input("how many large dollars?: ")) * 1
        total += int(input("how many half dollars?: ")) * 0.5
        total += int(input("how many quarters?: ")) * 0.25
        total += int(input("how many nickels?: ")) * 0.05
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

    def make_sandwich(self, sandwich_size, ingredients):
        for item in ingredients:
            self.machine_resources[item] -= ingredients[item]
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")

machine = SandwichMachine(resources)

while True:
    choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()
    if choice == "off":
        break
    elif choice == "report":
        for resource, amount in machine.machine_resources.items():
            print(f"{resource.capitalize()}: {amount} slice(s)" if resource != "cheese" else f"{resource.capitalize()}: {amount} ounce(s)")
    elif choice in recipes:
        ingredients = recipes[choice]["ingredients"]
        if machine.check_resources(ingredients):
            cost = recipes[choice]["cost"]
            print(f"The cost is ${cost:.2f}")
            coins = machine.process_coins()
            if machine.transaction_result(coins, cost):
                machine.make_sandwich(choice, ingredients)