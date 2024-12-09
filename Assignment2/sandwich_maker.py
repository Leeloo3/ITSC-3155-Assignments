import time

class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        for item in ingredients:
            if ingredients[item] > self.machine_resources.get(item, 0):
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"{sandwich_size} sandwich made!")
        time.sleep(2)  # Wait for 2 seconds