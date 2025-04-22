# Coffee Machine

A Python implementation of a coffee machine that can make various types of coffee drinks, manage resources, and handle monetary transactions.

## Features

- Makes three types of coffee:
  - Espresso ($1.50)
  - Latte ($2.50)
  - Cappuccino ($3.00)
- Manages resources:
  - Water (ml)
  - Milk (ml)
  - Coffee beans (g)
  - Money ($)
- Processes coins (quarters, dimes, nickels, pennies)
- Reports current resource levels
- Checks resource sufficiency before making drinks

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/coffee-machine.git
cd coffee-machine
```

2. No additional dependencies required - uses only Python standard library.

## Usage

```python
from coffee_machine import CoffeeMachine

# Create a new coffee machine instance
machine = CoffeeMachine()

# Check resources
print(machine.report())

# Make a coffee (if resources are sufficient)
if machine.is_resource_sufficient("espresso"):
    payment = machine.process_coins()
    if payment >= machine.menu["espresso"]["cost"]:
        machine.make_coffee("espresso")
```

## Testing

Run the tests using:
```bash
python3 -m unittest test_coffee_machine.py -v
```

## Project Structure

- `coffee_machine.py`: Main implementation of the CoffeeMachine class
- `test_coffee_machine.py`: Unit tests for the CoffeeMachine class
- `README.md`: Project documentation

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 