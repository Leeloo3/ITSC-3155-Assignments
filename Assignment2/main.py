# Created by Jaden Shaw 801292597

import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def main():
    while True:
        sandwich_size = input("What size sandwich would you like? (small/medium/large) or type 'end' to exit: ").lower()
        
        if sandwich_size == "end":
            print("Thank you for your business. Goodbye!")
            break
        
        if sandwich_size in recipes:
            cost = recipes[sandwich_size]["cost"]
            print(f"The cost of a {sandwich_size} sandwich is ${cost:.2f}.")
            
            coins = cashier_instance.process_coins()
            if cashier_instance.transaction_result(coins, cost):
                ingredients = recipes[sandwich_size]["ingredients"]
                if sandwich_maker_instance.check_resources(ingredients):
                    sandwich_maker_instance.make_sandwich(sandwich_size, ingredients)
                    print(f"Enjoy your {sandwich_size} sandwich!")
                else:
                    print("Sorry, we don't have enough ingredients to make that sandwich.")
            else:
                print("Insufficient funds. Please try again.")
        else:
            print("Invalid sandwich size. Please choose small, medium, or large.")

if __name__ == "__main__":
    main()
