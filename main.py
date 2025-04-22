#!/usr/bin/env python3
"""Main entry point for the Coffee Machine application."""

from src.coffee_machine import CoffeeMachine

def print_menu(machine: CoffeeMachine):
    """Print the available menu items."""
    print("\nAvailable drinks:")
    for name, coffee in machine.get_menu().items():
        print(f"{name.capitalize()}: ${coffee.price:.2f}")

def print_report(machine: CoffeeMachine):
    """Print the current resource levels."""
    resources = machine.report()
    print("\nCurrent resources:")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")

def main():
    machine = CoffeeMachine()
    
    while True:
        print("\n=== Coffee Machine ===")
        print("1. Buy a drink")
        print("2. Check resources")
        print("3. Refill machine")
        print("4. Exit")
        
        choice = input("\nWhat would you like to do? ")
        
        if choice == "1":
            print_menu(machine)
            drink = input("\nWhat would you like? (or 'back' to return): ").lower()
            
            if drink == 'back':
                continue
                
            result = machine.make_coffee(drink)
            print(f"\n{result}")
            
        elif choice == "2":
            print_report(machine)
            
        elif choice == "3":
            print("\nRefill amounts:")
            water = int(input("Water (ml): "))
            milk = int(input("Milk (ml): "))
            coffee = int(input("Coffee (g): "))
            machine.refill(water, milk, coffee)
            
        elif choice == "4":
            print("\nThank you for using the Coffee Machine!")
            break
            
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
