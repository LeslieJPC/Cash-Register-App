import pickle


class RetailItem:
    def __init__(self, item, description, units_in_inventory, price):
        self.item = item
        self.description = description
        self.units_in_inventory = units_in_inventory
        self.price = price

    
class CashRegister:
    def __init__(self):
        self.item_dict = {
            1: RetailItem("Item #1", "Jacket", 12, 59.95),
            2: RetailItem("Item #2", "Designer Jeans", 40, 34.95),
            3: RetailItem("Item #3", "Shirt", 20, 24.95)
        }  # Initialize a dictionary to store RetailItem objects

    def purchase_item(self, item_number):
        """
        Add a RetailItem object to the Cash Register's item dictionary.
        
        Args:
            item_number (int): The item number to add to the dictionary.
        """
        if item_number in self.item_dict:
            retail_item = self.item_dict[item_number]
            self.show_item(retail_item)
        else:
            print("Invalid item number.")

    def get_total(self):
        """
        Calculate and return the total price of all items in the Cash Register.
        
        Returns:
            float: The total price of all items.
        """
        total_price = sum(item.price for item in self.item_dict.values())
        return total_price

    def show_items(self):
        print("Items in Cash Register:")
        for item_number, retail_item in self.item_dict.items():
            self.show_item(retail_item)

    def show_item(self, retail_item):
        """Display data about a RetailItem object."""
        print(f"Item: {retail_item.item}")
        print(f"Description: {retail_item.description}")
        print(f"Units in Inventory: {retail_item.units_in_inventory}")
        print(f"Price: ${retail_item.price:.2f}")
        print("---")

    def clear(self):
        self.item_dict = {}  # Clear the Cash Register's item

    def load_items(self, filename):
        """
        Load the item dictionary from a file using pickle.

        Args:
            filename (str): The name of the file to load the data from.
        """
        try:
            with open(filename, "rb") as file:
                self.item_dict = pickle.load(file)
        except FileNotFoundError:
            self.item_dict = {}

    def save_items(self, filename):
        """
        Save the item dictionary to a file using pickle.

        Args:
            filename (str): The name of the file to save the data.
        """
        with open(filename, "wb") as file:
            pickle.dump(self.item_dict, file)    

def main():
    cash_register = CashRegister()

    while True:
        print("\nAvailable Items: ")
        for item_number, retail_item in cash_register.item_dict.items():
            print(f"{item_number}. {retail_item.description}")
        print("Enter 'done' to Checkout")
        print("---")
        item_selection = input("Select an Item Number (or enter 'done' to Checkout): ")
        
        if item_selection.lower() == "done":
            break

        try:
            item_number = int(item_selection)
            cash_register.purchase_item(item_number)
        except ValueError:
            print("Invalid input. Please enter a valid item number.")

    # Display items in the Cash Register and calculate the total price
    cash_register.show_items()
    total_price = cash_register.get_total()
    print(f"Total Price: ${total_price:.2f}")

    # Clear the Cash Register (if needed)
    cash_register.clear()
    
    # Save the item list when done
    cash_register.save_items("cash_register_items.pickle")
    
if __name__ == "__main__":
    main()
