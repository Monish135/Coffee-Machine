class CoffeeMachine:
    def __init__(self):
        """Initialize coffee machine with resources and menu"""
        self.resources = {
            "water": 300,    # ml
            "milk": 200,     # ml
            "coffee": 100,   # g
            "money": 0       # $
        }
        
        self.menu = {
            "espresso": {
                "ingredients": {
                    "water": 50,
                    "coffee": 18,
                },
                "cost": 1.5,
            },
            "latte": {
                "ingredients": {
                    "water": 200,
                    "milk": 150,
                    "coffee": 24,
                },
                "cost": 2.5,
            },
            "cappuccino": {
                "ingredients": {
                    "water": 250,
                    "milk": 100,
                    "coffee": 24,
                },
                "cost": 3.0,
            }
        }

    def report(self):
        """Return a string showing current resource values"""
        return (
            f"Water: {self.resources['water']}ml\n"
            f"Milk: {self.resources['milk']}ml\n"
            f"Coffee: {self.resources['coffee']}g\n"
            f"Money: ${self.resources['money']}"
        )

    def is_resource_sufficient(self, drink_name):
        """Check if there are sufficient resources to make the drink"""
        for item, amount in self.menu[drink_name]["ingredients"].items():
            if self.resources[item] < amount:
                return False
        return True

    def process_coins(self):
        """Process coins inserted and return total"""
        print("Please insert coins.")
        quarters = int(input("How many quarters?: ")) * 0.25
        dimes = int(input("How many dimes?: ")) * 0.1
        nickels = int(input("How many nickels?: ")) * 0.05
        pennies = int(input("How many pennies?: ")) * 0.01
        return quarters + dimes + nickels + pennies

    def make_coffee(self, drink_name):
        """Make the coffee and update resources"""
        for item, amount in self.menu[drink_name]["ingredients"].items():
            self.resources[item] -= amount
        self.resources["money"] += self.menu[drink_name]["cost"] 