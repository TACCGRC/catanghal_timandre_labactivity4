# Lab Activity 3 - Object-Oriented Design and Implementation

**Student Name:** Tim Andre Catanghal  
**Course:** CPE106L-4

## Overview
This project sets up an object-oriented inventory monitoring mini-system in Python. It demonstrates core OOP principles—such as encapsulation, composition, and state-aware data handling—by modeling distinct entities (`Item`), stock-tracking wrappers (`ItemCounter`), and a central management system (`ItemManagement`) to handle adding, reducing, deleting, and displaying inventory records in a structured tabular format.

## Project Structure
The repository is modularly organized into three main components:
* **Source Code (`src/`)**: Contains the core business logic, including the object definitions (`Item`, `ItemCounter`, `ItemManagement`) and the interactive console menu script (`main.py`).
* **Test Suite (`tests/`)**: Contains automated `unittest` scripts that programmatically verify item creation, duplicate counting, stock reduction, and edge cases.
* **Virtual Environment (`environment/`)**: Houses the local Python environment to isolate project dependencies.

## How to Run Tests
Run the following commands from the root directory:
1. Activate the virtual environment: `source environment/bin/activate`
2. Run Script: `python3 src/main.py`
3. Run Unit Tests: `python3 -m unittest discover -s tests -p "test_*.py"`