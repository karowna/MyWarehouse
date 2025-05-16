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


if __name__ == "__main__":
    # Create a Supplier instance and test functionality
    supplier = Supplier("John Doe", "+1234567890", "john@example.com", "SUP123")
    supplier.add_order("Order001")

    contact = supplier.get_contact_details()
    print(f"Supplier: {supplier._name}")
    print(f"Contact Email: {contact['email']}")
    print(f"Contact Phone: {contact['phone']}")
    print(f"Order History: {supplier.get_order_history()}")
