import pytest
from src.coffee_machine import CoffeeMachine, Coffee

@pytest.fixture
def machine():
    return CoffeeMachine()

def test_initialization(machine):
    assert machine.water == 300
    assert machine.milk == 200
    assert machine.coffee == 100
    assert machine.money == 0.0
    assert len(machine.menu) == 3

def test_report(machine):
    report = machine.report()
    assert report["water"] == 300
    assert report["milk"] == 200
    assert report["coffee"] == 100
    assert report["money"] == 0.0

def test_check_resources(machine):
    # Test with espresso (should have enough resources)
    espresso = machine.menu["espresso"]
    assert machine.check_resources(espresso) is None
    
    # Test with insufficient resources
    big_coffee = Coffee("big", 400, 300, 50, 5.00)
    assert "water" in machine.check_resources(big_coffee)

def test_make_coffee(machine, monkeypatch):
    # Mock coin input
    inputs = iter(["4", "0", "0", "0"])  # $1.00 in quarters
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    # Try to make espresso
    result = machine.make_coffee("espresso")
    assert "not enough money" in result
    assert machine.money == 0.0
    
    # Mock sufficient payment
    inputs = iter(["6", "0", "0", "0"])  # $1.50 in quarters
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    result = machine.make_coffee("espresso")
    assert "Enjoy" in result
    assert machine.money == 1.50
    assert machine.water == 250
    assert machine.coffee == 82

def test_refill(machine):
    initial_water = machine.water
    initial_milk = machine.milk
    initial_coffee = machine.coffee
    
    machine.refill(water=100, milk=50, coffee=25)
    
    assert machine.water == initial_water + 100
    assert machine.milk == initial_milk + 50
    assert machine.coffee == initial_coffee + 25

def test_invalid_drink(machine):
    result = machine.make_coffee("unicorn_frappuccino")
    assert "not available" in result

def test_get_menu(machine):
    menu = machine.get_menu()
    assert "espresso" in menu
    assert "latte" in menu
    assert "cappuccino" in menu
    assert isinstance(menu["espresso"], Coffee) 