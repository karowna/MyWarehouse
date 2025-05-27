from app.person import Person
from app.transaction import Transaction


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

    def fulfill_order(self, item_id, amount):
        item = self._inventory.get(item_id)
        if not item:
            return None, "Item not found in supplier's inventory."

        transaction = Transaction(item, amount, item.price, self, "restock")
        self.add_order(transaction)
        return item, transaction
