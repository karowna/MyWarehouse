class Person: # Create a base class for Person, promotes reusability and encapsulation
    def __init__(self, name, contact_details):
        self._name = name # Make it private
        self._contact_details = contact_details

    def get_contact_details(self):
        return self._contact_details

    def set_contact_details(self, contact_details):
        self._contact_details = contact_details

class Supplier(Person): # Inherit from Person class
    def __init__(self, name, contact_details, supplier_id):
        super().__init__(name, contact_details) 
        self._supplier_id = supplier_id
        self._order_history = []

    def add_order(self, order):
        self._order_history.append(order)

    def get_order_history(self):
        return self._order_history  

if __name__ == "__main__": # Test the classes
    supplier = Supplier("John Doe", "john@example.com", "SUP123")
    supplier.add_order("Order001")
    print(f"Supplier: {supplier._name}, Contact: {supplier.get_contact_details()}")
    print(f"Order History: {supplier.get_order_history()}")

