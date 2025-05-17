from datetime import datetime, timedelta

class Person:
    """Base class representing a person with contact details."""
    def __init__(self, name, contact_number, contact_email):
        self._name = name
        self._contact_number = contact_number
        self._contact_email = contact_email

    def get_contact_details(self):
        return {
            "name": self._name,
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


class Customer(Person):
    """Represents a customer, inheriting from Person."""
    def __init__(self, name, contact_number, contact_email, customer_id):
        super().__init__(name, contact_number, contact_email)
        self._customer_id = customer_id
        self._purchase_history = []

    def add_purchase(self, purchase):
        self._purchase_history.append(purchase)

    def get_purchase_history(self):
        return self._purchase_history


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


class Warehouse:
    """Represents the warehouse that manages inventory and supplier interactions"""
    def __init__(self):
        self._inventory = {}
        self._suppliers = {}

    def add_supplier(self, supplier):
        self._suppliers[supplier._supplier_id] = supplier

    def update_supplier(self, supplier_id, contact_number, contact_email):
        if supplier_id in self._suppliers:
            self._suppliers[supplier_id].set_contact_details(contact_number, contact_email)

    def delete_supplier(self, supplier_id):
        if supplier_id in self._suppliers:
            del self._suppliers[supplier_id]

    def get_supplier(self, supplier_id):
        return self._suppliers.get(supplier_id)

    def add_inventory_item(self, item):
        self._inventory[item._item_id] = item

    def get_inventory_item(self, item_id):
        return self._inventory.get(item_id)

    def order_from_supplier(self, supplier_id, item_id, amount):
        supplier = self.get_supplier(supplier_id)
        if supplier:
            item = self.get_inventory_item(item_id)
            if item:
                item.receive_stock(amount)
                supplier.add_order(f"Order for {amount} units of {item._name}")
                print(f"Ordered {amount} units of {item._name} from {supplier._name}")
            else:
                print("Item not found in inventory.")
        else:
            print("Supplier not found.")

    def get_inventory(self):
        return self._inventory

    def place_customer_order(self, customer, item_id, amount):
        item = self.get_inventory_item(item_id)
        if item and item.get_stock_level() >= amount:
            item.reduce_stock(amount)
            order = Order(customer, item, amount)
            customer.add_purchase(order)
            print(f"Order placed for {amount} units of {item._name}")
        else:
            print("Insufficient stock or item not found.")

    def view_purchase_history(self, customer):
        return customer.get_purchase_history()


class Order:
    """Represents an order placed by a customer"""
    def __init__(self, customer, item, amount):
        self._customer = customer
        self._item = item
        self._amount = amount
        self._status = "processing"
        self._timestamp = datetime.now()

    def update_status(self):
        elapsed_time = datetime.now() - self._timestamp
        if elapsed_time > timedelta(minutes=3):
            self._status = "delivered"
        elif elapsed_time > timedelta(minutes=2):
            self._status = "dispatched"
        elif elapsed_time > timedelta(minutes=1):
            self._status = "processed"

    def get_status(self):
        self.update_status()
        return self._status
