import unittest
from unittest.mock import patch
from coffee_machine import CoffeeMachine

class TestCoffeeMachine(unittest.TestCase):
    def setUp(self):
        """Set up a new CoffeeMachine instance for each test"""
        self.machine = CoffeeMachine()

    def test_initial_resources(self):
        """Test that the machine starts with correct initial resources"""
        self.assertEqual(self.machine.resources["water"], 300)
        self.assertEqual(self.machine.resources["milk"], 200)
        self.assertEqual(self.machine.resources["coffee"], 100)
        self.assertEqual(self.machine.resources["money"], 0)

    def test_menu_items(self):
        """Test that the menu contains all required items"""
        self.assertIn("espresso", self.machine.menu)
        self.assertIn("latte", self.machine.menu)
        self.assertIn("cappuccino", self.machine.menu)

    def test_resource_sufficiency(self):
        """Test resource sufficiency checks"""
        # Test with sufficient resources
        self.assertTrue(self.machine.is_resource_sufficient("espresso"))
        
        # Test with insufficient water
        self.machine.resources["water"] = 10
        self.assertFalse(self.machine.is_resource_sufficient("espresso"))
        
        # Test with insufficient coffee
        self.machine.resources["water"] = 300
        self.machine.resources["coffee"] = 10
        self.assertFalse(self.machine.is_resource_sufficient("espresso"))

    def test_make_coffee(self):
        """Test making coffee deducts resources and adds money"""
        initial_water = self.machine.resources["water"]
        initial_coffee = self.machine.resources["coffee"]
        initial_money = self.machine.resources["money"]
        
        self.machine.make_coffee("espresso")
        
        self.assertEqual(self.machine.resources["water"], 
                        initial_water - self.machine.menu["espresso"]["ingredients"]["water"])
        self.assertEqual(self.machine.resources["coffee"], 
                        initial_coffee - self.machine.menu["espresso"]["ingredients"]["coffee"])
        self.assertEqual(self.machine.resources["money"], 
                        initial_money + self.machine.menu["espresso"]["cost"])

    @patch('builtins.input', side_effect=['4', '0', '0', '0'])  # 4 quarters = $1.00
    def test_process_coins(self, mock_input):
        """Test coin processing with mocked input"""
        total = self.machine.process_coins()
        self.assertEqual(total, 1.0)

    def test_report(self):
        """Test the report method returns correct string format"""
        report = self.machine.report()
        self.assertIn("Water: 300ml", report)
        self.assertIn("Milk: 200ml", report)
        self.assertIn("Coffee: 100g", report)
        self.assertIn("Money: $0", report)

if __name__ == '__main__':
    unittest.main() 