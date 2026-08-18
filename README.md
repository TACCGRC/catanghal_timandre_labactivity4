# Lab Activity 4 - Design Pattern Implementation & Unit Testing

**Student Name:** Tim Andre Catanghal  
**Course:** CPE106L-4

## Overview
This project implements a **Shipping Cost Calculation System** demonstrating the **Strategy Design Pattern** in Python. The system defines a family of interchangeable rate calculation algorithms (`StandardShipping`, `ExpressShipping`, `OvernightShipping`) and uses a context manager (`ShippingCalculator`) to apply the appropriate calculation dynamically at runtime without modifying client code.

## Why the Strategy Pattern Fits the Problem
1. **Open/Closed Principle (OCP):** New shipping tiers (e.g., `InternationalShipping`, `DroneDelivery`) can be added by creating new subclasses derived from `ShippingStrategy` without modifying existing calculation logic.
2. **Elimination of Conditional Logic:** Removes brittle `if-elif-else` chains inside order processing methods, delegating cost calculation directly to dedicated strategy objects.
3. **Runtime Interchangeability:** The shipping method on `ShippingCalculator` can be swapped dynamically as user selections change during checkout.
4. **Isolated Testability:** Each shipping algorithm is encapsulated in its own class and can be independently verified via automated unit tests.

## Project Structure
* **`src/main.py`**: Contains the core Strategy Pattern classes (`ShippingStrategy`, concrete strategies, `ShippingCalculator`) and an interactive CLI test runner.
* **`tests/test_shipping.py`**: Automated unit test suite using Python's built-in `unittest` module.

## How to Run

### 1. Run Interactive CLI
```bash
1. python3 src/main.py
2. python -m unittest src/test/test_shipping.py -v