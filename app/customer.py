from app.person import Person
from app.transaction import Transaction

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

    def make_purchase(self, item, amount):
        total_cost = item.price * amount
        self.deduct_balance(total_cost)
        transaction = Transaction(item, amount, item.price, self, "purchase")
        self.add_purchase(transaction)
        return transaction
