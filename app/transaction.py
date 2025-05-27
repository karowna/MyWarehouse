from datetime import datetime, timedelta


class Transaction:
    """Represents a transaction involving an item"""

    def __init__(self, item, quantity, price, party, transaction_type, status=None):
        self._item = item
        self._quantity = quantity
        self._price = price
        self._party = party
        self._transaction_type = transaction_type
        self._timestamp = datetime.now()
        self._status = status or (
            "delivered" if transaction_type == "restock" else "processing"
        )

    @property
    def item(self):
        return self._item

    @property
    def quantity(self):
        return self._quantity

    @property
    def price(self):
        return self._price

    @property
    def party(self):
        return self._party

    @property
    def transaction_type(self):
        return self._transaction_type

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def status(self):
        return self._status

    @property
    def total_cost(self):
        return self._price * self._quantity

    def __str__(self):
        return (
            f"{self._transaction_type.capitalize()} by {self._party.name}: {self._item.name}, "
            f"Quantity: {self._quantity}, Price: £{self._price:.2f}, "
            f"Date: {self._timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
        )

    def update_status(self):
        if self._transaction_type == "purchase":
            elapsed_time = datetime.now() - self._timestamp
            if elapsed_time > timedelta(minutes=3):
                self._status = "delivered"
            elif elapsed_time > timedelta(minutes=2):
                self._status = "dispatched"
            elif elapsed_time > timedelta(minutes=1):
                self._status = "processed"

    def to_dict(self):
        return {
            "Item": self._item.name,
            "Quantity": self._quantity,
            "Price": self._price,
            "Party": self._party.name,
            "Type": self._transaction_type,
            "Timestamp": self._timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        }
