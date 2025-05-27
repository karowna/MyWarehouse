from app.item import Item
from app.transaction import Transaction
from app.customer import Customer
from app.supplier import Supplier


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
            self._suppliers[supplier_id].set_contact_details(
                contact_number, contact_email
            )

    def delete_supplier(self, supplier_id):
        if supplier_id in self._suppliers:
            del self._suppliers[supplier_id]

    def get_supplier(self, supplier_id):
        return self._suppliers.get(supplier_id)

    def add_customer(self, customer):
        if customer.customer_id in self._customers:
            return False  # Customer already exists
        self._customers[customer.customer_id] = customer
        return True

    def get_customer(self, customer_id):
        return self._customers.get(customer_id)

    def order_from_supplier(self, supplier_id, item_id, amount):
        supplier = self.get_supplier(supplier_id)
        if not supplier:
            return "Supplier not found."

        item, result = supplier.fulfill_order(item_id, amount)
        if not item:
            return result

        total_cost = item.price * amount
        self.deduct_balance(total_cost)

        if item_id not in self._inventory:
            self._inventory[item_id] = Item(
                item_id, item.name, item.description, item.price
            )

        self._inventory[item_id].receive_stock(amount)

        return f"Ordered {amount} units of {item.name} from {supplier.name} for £{total_cost:.2f}"

    def place_customer_order(self, customer, item_id, amount):
        item = self._inventory.get(item_id)
        if not item:
            return "Item not found in inventory."
        if item.quantity < amount:
            return "Insufficient stock."

        item.reduce_stock(amount)
        transaction = customer.make_purchase(item, amount)
        return f"Order placed for {amount} units of {item.name} at £{item.price} each. Total: £{transaction.price * transaction.quantity:.2f}"

    def quick_financial_overview(self):
        total_spent = sum(
            item.price * item.quantity for item in self._inventory.values()
        )
        total_sales = sum(
            order.price * order.quantity
            for customer in self._customers.values()
            for order in customer.purchase_history
        )
        profit = total_sales - total_spent

        return {
            "Total Spent by Warehouse": total_spent,
            "Total Sales to Customers": total_sales,
            "Total Profit": profit,
        }

    def create_in_depth_financial_report(self):
        report = {"Warehouse Transactions": [], "Customer Transactions": []}

        for supplier in self._suppliers.values():
            for order in supplier.order_history:
                data = order.to_dict()
                data["Supplier"] = supplier.name
                data["Status"] = "delivered"
                report["Warehouse Transactions"].append(data)

        for customer in self._customers.values():
            for order in customer.purchase_history:
                order.update_status()
                data = order.to_dict()
                data["Customer"] = customer.name
                data["Status"] = order.status
                report["Customer Transactions"].append(data)

        return report
