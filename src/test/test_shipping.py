import unittest
from src.main import (
    ShippingStrategy,
    StandardShipping,
    ExpressShipping,
    OvernightShipping,
    ShippingCalculator,
)


class TestShippingStrategyPattern(unittest.TestCase):

    def setUp(self):
        """Instantiate strategies and calculator before each test."""
        self.standard = StandardShipping()
        self.express = ExpressShipping()
        self.overnight = OvernightShipping()
        self.calculator = ShippingCalculator()

    # --- Strategy Calculation Tests ---
    def test_standard_shipping(self):
        # Base $5.00 + (10kg * $1.50) = $20.00
        self.assertEqual(self.standard.calculate(10.0), 20.00)

    def test_express_shipping(self):
        # Base $12.00 + (5kg * $3.00) = $27.00
        self.assertEqual(self.express.calculate(5.0), 27.00)

    def test_overnight_shipping(self):
        # Base $25.00 + (2.5kg * $6.00) = $40.00
        self.assertEqual(self.overnight.calculate(2.5), 40.00)

    # --- Base Class & Error Handling Tests ---
    def test_base_class_raises_not_implemented(self):
        base_strategy = ShippingStrategy()
        with self.assertRaises(NotImplementedError):
            base_strategy.calculate(5.0)

    def test_invalid_weight_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.standard.calculate(0.0)
        with self.assertRaises(ValueError):
            self.express.calculate(-3.0)

    # --- Context Delegation & Runtime Swapping Tests ---
    def test_runtime_strategy_swapping(self):
        # Test delegation to Standard
        self.calculator.strategy = self.standard
        self.assertEqual(self.calculator.compute_cost(10.0), 20.00)

        # Dynamically switch strategy to Express
        self.calculator.strategy = self.express
        self.assertEqual(self.calculator.compute_cost(10.0), 42.00)


if __name__ == "__main__":
    unittest.main()