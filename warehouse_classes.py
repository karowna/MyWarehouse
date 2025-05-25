from datetime import datetime, timedelta

class Person:
    """Base class representing a person with contact details."""
    def __init__(self, name, contact_number, contact_email):
        self._name = name
        self._contact_number = contact_number
        self._contact_email = contact_email
        self._order_history = []

    @property
    def name(self):
        return self._name

    @property
    def contact_number(self):
        return self._contact_number

    @property
    def contact_email(self):
        return self._contact_email

    @property
    def order_history(self):
        return self._order_history

    def add_order(self, order):
        self._order_history.append(order)

    def set_contact_details(self, contact_number, contact_email):
        self._contact_number = contact_number
        self._contact_email = contact_email


class Supplier(Person):
    """Represents a supplier, inheriting from Person."""
    def __init__(self, name, contact_number, contact_email, supplier_id):
        super().__init__(name, contact_number, contact_email)
        self._supplier_id = supplier_id
        self._inventory = {}

    @property
    def supplier_id(self):
        return self._supplier_id

    @property
    def inventory(self):
        return self._inventory

    def add_inventory_item(self, item):
        self._inventory[item.item_id] = item


class Customer(Person):
    """Represents a customer, inheriting from Person."""
    def __init__(self, name, contact_number, contact_email, customer_id):
        super().__init__(name, contact_number, contact_email)
        self._customer_id = customer_id
        self._purchase_history = []
        self._balance = 0.0

    @property
    def customer_id(self):
        return self._customer_id

    @property
    def purchase_history(self):
        return self._purchase_history

    @property
    def balance(self):
        return self._balance

    def deduct_balance(self, amount):
        self._balance -= amount

    def add_purchase(self, purchase):
        self._purchase_history.append(purchase)

    def get_formatted_purchase_history(self):
        if not self._purchase_history:
            return "No purchases found."
        return "\n".join(f"{i+1}. {purchase}" for i, purchase in enumerate(self._purchase_history))

class InventoryItem:
    """Represents an item in the inventory with stock management capabilities"""

    def __init__(self, item_id, name, description, price, quantity=0, low_stock_threshold=None):
        self._item_id = item_id
        self._name = name
        self._description = description
        self._price = price
        self._quantity = quantity
        self._low_stock_threshold = low_stock_threshold

    @property
    def item_id(self):
        return self._item_id

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @property
    def low_stock_threshold(self):
        return self._low_stock_threshold

    def receive_stock(self, amount):
        """Add new stock to inventory"""
        if amount > 0:
            self._quantity += amount
            return f"Received {amount} units of '{self._name}'. New quantity: {self._quantity}"
        else:
            raise ValueError("Invalid stock amount. Must be greater than 0.")

    def reduce_stock(self, amount):
        """Reduce stock when items are sold or used"""
        if 0 < amount <= self._quantity:
            self._quantity -= amount
            return f"Reduced {amount} units of '{self._name}'. Remaining quantity: {self._quantity}"
        else:
            raise ValueError("Invalid reduction amount or insufficient stock.")

    def is_low_stock(self):
        """Check if stock is below the low stock threshold"""
        if self._low_stock_threshold is not None:
            return self._quantity <= self._low_stock_threshold
        return False

    def get_item_details(self):
        """Return item details"""
        return {
            "Item ID": self._item_id,
            "Name": self._name,
            "Description": self._description,
            "Price": self._price,
            "Quantity": self._quantity,
            "Low Stock Threshold": self._low_stock_threshold,
            "Low Stock Alert": self.is_low_stock()
        }


class Warehouse:
    """Represents the warehouse that manages inventory and supplier interactions"""
    def __init__(self):
        self._inventory = {}
        self._suppliers = {}
        self._customers = {}
        self._balance = 0.0

    @property
    def inventory(self):
        return self._inventory

    @property
    def suppliers(self):
        return self._suppliers

    @property
    def customers(self):
        return self._customers

    @property
    def balance(self):
        return self._balance

    def deduct_balance(self, amount):
        self._balance -= amount

    def add_supplier(self, supplier):
        self._suppliers[supplier.supplier_id] = supplier

    def update_supplier(self, supplier_id, contact_number, contact_email):
        if supplier_id in self._suppliers:
            self._suppliers[supplier_id].set_contact_details(contact_number, contact_email)

    def delete_supplier(self, supplier_id):
        if supplier_id in self._suppliers:
            del self._suppliers[supplier_id]

    def get_supplier(self, supplier_id):
        return self._suppliers.get(supplier_id)

    def add_customer(self, customer):
        self._customers[customer.customer_id] = customer

    def get_customer(self, customer_id):
        return self._customers.get(customer_id)

    def order_from_supplier(self, supplier_id, item_id, amount):
        supplier = self.get_supplier(supplier_id)
        if supplier:
            item = supplier.inventory.get(item_id)
            if item:
                total_cost = item.price * amount
                self.deduct_balance(total_cost)
                if item_id not in self._inventory:
                    self._inventory[item_id] = InventoryItem(item_id, item.name, item.description, item.price)
                self._inventory[item_id].receive_stock(amount)
                supplier.add_order(f"Order for {amount} units of {item.name} at £{item.price} each")
                return f"Ordered {amount} units of {item.name} from {supplier.name} for £{total_cost:.2f}"
            else:
                return "Item not found in supplier's inventory."
        else:
            return "Supplier not found."

    def place_customer_order(self, customer, item_id, amount):
        item = self._inventory.get(item_id)
        if item and item.quantity >= amount:
            total_cost = item.price * amount
            item.reduce_stock(amount)
            customer.deduct_balance(total_cost)
            order = Order(customer, item, amount)
            customer.add_purchase(order)
            return f"Order placed for {amount} units of {item.name} at £{item.price} each. Total: £{total_cost:.2f}"
        else:
            return "Insufficient stock or item not found."

    def quick_financial_overview(self):
        total_spent = sum(item.price * item.quantity for item in self._inventory.values())
        total_sales = sum(order.item.price * order.amount for customer in self._customers.values() for order in customer.purchase_history)
        profit = total_sales - total_spent

        return {
            "Total Spent by Warehouse": total_spent,
            "Total Sales to Customers": total_sales,
            "Total Profit": profit
        }

    def create_in_depth_financial_report(self):
        report = {
            "Warehouse Transactions": [],
            "Customer Transactions": []
        }

        for supplier in self._suppliers.values():
            for order in supplier.order_history:
                report["Warehouse Transactions"].append(order)

        for customer in self._customers.values():
            for order in customer.purchase_history:
                report["Customer Transactions"].append({
                    "Customer": customer.name,
                    "Item": order.item.name,
                    "Amount": order.amount,
                    "Price": order.item.price,
                    "Status": order.status
                })

        return report


class Order:
    """Represents an order placed by a customer"""
    def __init__(self, customer, item, amount):
        self._customer = customer
        self._item = item
        self._amount = amount
        self._status = "processing"
        self._timestamp = datetime.now()

    @property
    def customer(self):
        return self._customer

    @property
    def item(self):
        return self._item

    @property
    def amount(self):
        return self._amount

    @property
    def status(self):
        self.update_status()
        return self._status
    
    def __str__(self):
        return (
            f"Item: {self._item.name}, "
            f"Amount: {self._amount}, "
            f"Status: {self.status}, "
            f"Date: {self._timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
        )

    def update_status(self):
        elapsed_time = datetime.now() - self._timestamp
        if elapsed_time > timedelta(minutes=3):
            self._status = "delivered"
        elif elapsed_time > timedelta(minutes=2):
            self._status = "dispatched"
        elif elapsed_time > timedelta(minutes=1):
            self._status = "processed"