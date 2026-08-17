class ShippingStrategy:
    """Base class defining the calculation interface."""
    def calculate(self, weight_kg: float) -> float:
        raise NotImplementedError("Subclasses must implement calculate().")


class StandardShipping(ShippingStrategy):
    """Standard ground delivery: $5.00 base + $1.50 per kg."""
    def calculate(self, weight_kg: float) -> float:
        if weight_kg <= 0:
            raise ValueError("Weight must be greater than zero.")
        return round(5.00 + (1.50 * weight_kg), 2)


class ExpressShipping(ShippingStrategy):
    """Express air delivery: $12.00 base + $3.00 per kg."""
    def calculate(self, weight_kg: float) -> float:
        if weight_kg <= 0:
            raise ValueError("Weight must be greater than zero.")
        return round(12.00 + (3.00 * weight_kg), 2)


class OvernightShipping(ShippingStrategy):
    """Overnight priority delivery: $25.00 base + $6.00 per kg."""
    def calculate(self, weight_kg: float) -> float:
        if weight_kg <= 0:
            raise ValueError("Weight must be greater than zero.")
        return round(25.00 + (6.00 * weight_kg), 2)


class ShippingCalculator:
    """Context class that delegates calculation to the chosen strategy."""
    def __init__(self, strategy: ShippingStrategy = None):
        self.strategy = strategy

    def compute_cost(self, weight_kg: float) -> float:
        if not self.strategy:
            raise ValueError("No shipping strategy has been selected.")
        return self.strategy.calculate(weight_kg)


def run_interactive_menu():
    calculator = ShippingCalculator()
    
    # Map user choices to concrete strategy instances
    strategies = {
        "1": ("Standard Shipping ($5.00 base + $1.50/kg)", StandardShipping()),
        "2": ("Express Shipping  ($12.00 base + $3.00/kg)", ExpressShipping()),
        "3": ("Overnight Shipping ($25.00 base + $6.00/kg)", OvernightShipping())
    }

    print("=" * 40)
    print("  Shipping Cost Calculator (Strategy Pattern)")
    print("=" * 40)

    test_case_count = 1

    while True:
        print(f"\n--- Test Run #{test_case_count} ---")
        print("Select Shipping Method:")
        print("1. Standard Shipping")
        print("2. Express Shipping")
        print("3. Overnight Shipping")
        print("4. Exit Program")

        choice = input("\nEnter choice (1-4): ").strip()

        if choice == "4":
            print("\nExiting calculator. Goodbye!")
            break

        if choice not in strategies:
            print("[Error] Invalid selection. Please enter 1, 2, 3, or 4.")
            continue

        try:
            weight_input = input("Enter package weight in kg: ").strip()
            weight = float(weight_input)

            # Assign selected strategy and calculate cost
            strategy_name, selected_strategy = strategies[choice]
            calculator.strategy = selected_strategy
            
            cost = calculator.compute_cost(weight)

            # Display formatted result
            print("\n" + "=" * 40)
            print(f"Method Selected : {strategy_name}")
            print(f"Package Weight  : {weight:.2f} kg")
            print(f"Total Shipping  : ${cost:.2f}")
            print("=" * 40)

            test_case_count += 1

        except ValueError as e:
            # Catches non-numeric inputs or negative/zero weights
            print(f"\n[Error] Invalid input: {e}")


if __name__ == "__main__":
    run_interactive_menu()