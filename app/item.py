class Item:
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
