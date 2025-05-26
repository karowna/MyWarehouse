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
