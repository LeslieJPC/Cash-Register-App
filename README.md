# Cash Register Application

## Overview
The **Cash Register Application** is a Python program that simulates a simple cash register system. It allows users to purchase items, display the total price of items, and save/load item data using pickle.

## Features
- Add items to the cash register.
- Display all items in the cash register.
- Calculate the total price of all items.
- Clear the cash register.
- Save item data to a file.
- Load item data from a file.

## Code Structure
The application is developed in Python and consists of two main classes: `RetailItem` and `CashRegister`. The program is executed through the `main` function.

### Classes

#### RetailItem
Represents a retail item with the following attributes:
- `item`: The item identifier.
- `description`: A description of the item.
- `units_in_inventory`: The number of units available in inventory.
- `price`: The price of the item.

#### CashRegister
Manages the cash register operations, including adding items, displaying items, calculating total price, and saving/loading item data.

##### Methods
- `__init__()`: Initializes the cash register with predefined items.
- `purchase_item(item_number)`: Adds an item to the cash register based on the item number.
- `get_total()`: Calculates and returns the total price of all items in the cash register.
- `show_items()`: Displays all items in the cash register.
- `show_item(retail_item)`: Displays details of a specific retail item.
- `clear()`: Clears all items from the cash register.
- `load_items(filename)`: Loads item data from a file using pickle.
- `save_items(filename)`: Saves item data to a file using pickle.

### Functions

#### main()
Executes the main program logic:
- Displays available items to the user.
- Prompts the user to select items to purchase.
- Displays the total price of selected items.
- Clears the cash register.
- Saves item data to a file when the program ends.

## Getting Started

### Prerequisites
- Python 3.x

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/CashRegisterApp.git
    ```
2. Navigate to the project directory:
    ```sh
    cd CashRegisterApp
    ```
3. Run the application:
    ```sh
    python cash_register.py
    ```

### Usage
1. The application will display a list of available items.
2. Enter the item number to add an item to the cash register.
3. Enter 'done' to checkout.
4. The application will display all items in the cash register and the total price.
5. The application will save the item data to a file named `cash_register_items.pickle`.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

Feel free to reach out for any questions or contributions. Happy coding!

---

### Note
This application is a sample project intended for learning and demonstration purposes. It may require further enhancements and testing for production use.
