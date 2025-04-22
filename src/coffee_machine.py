from dataclasses import dataclass
from typing import Dict, Optional

@dataclass
class Coffee:
    name: str
    water: int  # ml
    milk: int   # ml
    coffee: int # g
    price: float

class CoffeeMachine:
    def __init__(self):
        # Initialize resources
        self.water = 300  # ml
        self.milk = 200   # ml
        self.coffee = 100 # g
        self.money = 0.0  # dollars
        
        # Define coffee types
        self.menu = {
            "espresso": Coffee("espresso", 50, 0, 18, 1.50),
            "latte": Coffee("latte", 200, 150, 24, 2.50),
            "cappuccino": Coffee("cappuccino", 250, 100, 24, 3.00)
        }

    def report(self) -> Dict[str, float]:
        """Return current resource levels."""
        return {
            "water": self.water,
            "milk": self.milk,
            "coffee": self.coffee,
            "money": self.money
        }

    def check_resources(self, drink: Coffee) -> Optional[str]:
        """Check if there are sufficient resources to make the drink."""
        if self.water < drink.water:
            return "Sorry, not enough water."
        if self.milk < drink.milk:
            return "Sorry, not enough milk."
        if self.coffee < drink.coffee:
            return "Sorry, not enough coffee."
        return None

    def process_coins(self) -> float:
        """Process inserted coins and return the total."""
        print("\nPlease insert coins:")
        quarters = int(input("How many quarters? ")) * 0.25
        dimes = int(input("How many dimes? ")) * 0.10
        nickels = int(input("How many nickels? ")) * 0.05
        pennies = int(input("How many pennies? ")) * 0.01
        return quarters + dimes + nickels + pennies

    def make_coffee(self, drink_name: str) -> Optional[str]:
        """Make the coffee if resources are sufficient and payment is valid."""
        if drink_name not in self.menu:
            return "Sorry, that item is not available."
        
        drink = self.menu[drink_name]
        
        # Check resources
        resource_check = self.check_resources(drink)
        if resource_check:
            return resource_check
        
        # Process payment
        print(f"\nPrice: ${drink.price:.2f}")
        payment = self.process_coins()
        
        if payment < drink.price:
            return f"Sorry, that's not enough money. ${payment:.2f} refunded."
        
        change = payment - drink.price
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
        
        # Make coffee
        self.water -= drink.water
        self.milk -= drink.milk
        self.coffee -= drink.coffee
        self.money += drink.price
        
        return f"Here is your {drink_name}. Enjoy!"

    def refill(self, water: int = 0, milk: int = 0, coffee: int = 0):
        """Refill the machine's resources."""
        self.water += water
        self.milk += milk
        self.coffee += coffee
        print("Machine refilled successfully!")

    def get_menu(self) -> Dict[str, Coffee]:
        """Return the available menu items."""
        return self.menu 