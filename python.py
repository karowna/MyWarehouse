class Person:
    """Base class representing a person with contact details."""
    def __init__(self, name, contact_number, contact_email):
        self._name = name
        self._contact_number = contact_number
        self._contact_email = contact_email

    def get_contact_details(self):
        return {
            "phone": self._contact_number,
            "email": self._contact_email
        }

    def set_contact_details(self, contact_number, contact_email):
        self._contact_number = contact_number
        self._contact_email = contact_email


class Supplier(Person):
    """Represents a supplier, inheriting from Person."""
    def __init__(self, name, contact_number, contact_email, supplier_id):
        super().__init__(name, contact_number, contact_email)
        self._supplier_id = supplier_id
        self._order_history = []

    def add_order(self, order):
        self._order_history.append(order)

    def get_order_history(self):
        return self._order_history

class InventoryItem:
    """Represents an item in the inventory with stock management capabilities"""

    def __init__(self, item_id, name, description, quantity, low_stock_threshold):
        self._item_id = item_id
        self._name = name
        self._description = description
        self._quantity = quantity
        self._low_stock_threshold = low_stock_threshold

    def receive_stock(self, amount):
        """Add new stock to inventory"""
        if amount > 0:
            self._quantity += amount
            print(f"Received {amount} units of '{self._name}'. New quantity: {self._quantity}")
        else:
            print("Invalid stock amount. Must be greater than 0.")

    def reduce_stock(self, amount):
        """Reduce stock when items are sold or used"""
        if 0 < amount <= self._quantity:
            self._quantity -= amount
            print(f"Reduced {amount} units of '{self._name}'. Remaining quantity: {self._quantity}")
        else:
            print("Invalid reduction amount or insufficient stock.")

    def get_stock_level(self):
        """Return current stock quantity."""
        return self._quantity

    def is_low_stock(self):
        """Check if stock is below the low stock threshold"""
        return self._quantity <= self._low_stock_threshold

    def get_item_details(self):
        """Return item details"""
        return {
            "Item ID": self._item_id,
            "Name": self._name,
            "Description": self._description,
            "Quantity": self._quantity,
            "Low Stock Threshold": self._low_stock_threshold,
            "Low Stock Alert": self.is_low_stock()
        }

if __name__ == "__main__":
    # Create a Supplier instance and test functionality
    supplier = Supplier("John Doe", "+1234567890", "john@example.com", "SUP123")
    supplier.add_order("Order001")

    contact = supplier.get_contact_details()
    print(f"Supplier: {supplier._name}")
    print(f"Contact Email: {contact['email']}")
    print(f"Contact Phone: {contact['phone']}")
    print(f"Order History: {supplier.get_order_history()}")
