from warehouse_classes import Person, Supplier, Customer, InventoryItem, Warehouse, Order
import time

def main_menu():
    warehouse = Warehouse()

    while True:
        print("\n--- Main Menu ---")
        print("1. Customer Login")
        print("2. Admin Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            customer_login(warehouse)
        elif choice == "2":
            admin_login(warehouse)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

def customer_login(warehouse):
    while True:
        print("\n--- Customer Login ---")
        print("1. Sign In")
        print("2. Sign Up")
        print("0. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            customer_id = input("Enter your customer ID: ")
            customer = warehouse.get_customer(customer_id)
            if customer:
                customer_menu(warehouse, customer)
            else:
                print("Customer not found. Please sign up.")
        elif choice == "2":
            name = input("Enter your name: ")
            contact_number = input("Enter your contact number: ")
            contact_email = input("Enter your contact email: ")
            customer_id = input("Enter your customer ID: ")

            customer = Customer(name, contact_number, contact_email, customer_id)
            warehouse.add_customer(customer)
            print("Customer registered successfully.")
            customer_menu(warehouse, customer)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")

def customer_menu(warehouse, customer):
    while True:
        print("\n--- Customer Menu ---")
        print("1. View Inventory")
        print("2. Place Order")
        print("3. View Order History")
        print("0. Back to Customer Login")

        choice = input("Choose an option: ")

        if choice == "1":
            view_inventory(warehouse)
        elif choice == "2":
            place_order(warehouse, customer)
        elif choice == "3":
            view_order_history(customer)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")

def admin_login(warehouse):
    while True:
        print("\n--- Admin Menu ---")
        print("1. Manage Suppliers")
        print("2. Manage Warehouse Stock")
        print("3. View Warehouse Balance")
        print("4. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            manage_suppliers(warehouse)
        elif choice == "2":
            manage_warehouse_stock(warehouse)
        elif choice == "3":
            print(f"Warehouse Balance: £{warehouse.balance:.2f}")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

def manage_suppliers(warehouse):
    while True:
        print("\n--- Manage Suppliers ---")
        print("1. Add Supplier")
        print("2. Update Supplier")
        print("3. Delete Supplier")
        print("4. View Supplier Order History")
        print("5. Add Item to Supplier")
        print("6. Back to Admin Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            add_supplier(warehouse)
        elif choice == "2":
            update_supplier(warehouse)
        elif choice == "3":
            delete_supplier(warehouse)
        elif choice == "4":
            view_supplier_order_history(warehouse)
        elif choice == "5":
            add_item_to_supplier(warehouse)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")

def manage_warehouse_stock(warehouse):
    while True:
        print("\n--- Manage Warehouse Stock ---")
        print("1. Add Inventory Item")
        print("2. Order from Supplier")
        print("3. View Inventory")
        print("4. Back to Admin Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            add_inventory_item(warehouse)
        elif choice == "2":
            order_from_supplier(warehouse)
        elif choice == "3":
            view_inventory(warehouse)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

def add_supplier(warehouse):
    name = input("Enter supplier name: ")
    contact_number = input("Enter supplier contact number: ")
    contact_email = input("Enter supplier contact email: ")
    supplier_id = input("Enter supplier ID: ")

    supplier = Supplier(name, contact_number, contact_email, supplier_id)
    warehouse.add_supplier(supplier)
    print("Supplier added successfully.")

def update_supplier(warehouse):
    supplier_id = input("Enter supplier ID to update: ")
    contact_number = input("Enter new contact number: ")
    contact_email = input("Enter new contact email: ")

    warehouse.update_supplier(supplier_id, contact_number, contact_email)
    print("Supplier updated successfully.")

def delete_supplier(warehouse):
    supplier_id = input("Enter supplier ID to delete: ")

    warehouse.delete_supplier(supplier_id)
    print("Supplier deleted successfully.")

def view_supplier_order_history(warehouse):
    supplier_id = input("Enter supplier ID to view order history: ")
    supplier = warehouse.get_supplier(supplier_id)

    if supplier:
        print(f"Order History for {supplier.name}:")
        for order in supplier.order_history:
            print(order)
    else:
        print("Supplier not found.")

def add_item_to_supplier(warehouse):
    supplier_id = input("Enter supplier ID: ")
    supplier = warehouse.get_supplier(supplier_id)
    if supplier:
        item_id = input("Enter item ID: ")
        name = input("Enter item name: ")
        description = input("Enter item description: ")
        price = float(input("Enter item price (£/per): "))
        item = InventoryItem(item_id, name, description, price)
        supplier.add_inventory_item(item)
        print("Item added to supplier inventory.")
    else:
        print("Supplier not found.")

def add_inventory_item(warehouse):
    item_id = input("Enter item ID: ")
    name = input("Enter item name: ")
    description = input("Enter item description: ")
    quantity = int(input("Enter item quantity: "))
    low_stock_threshold = int(input("Enter low stock threshold: "))

    item = InventoryItem(item_id, name, description, quantity, low_stock_threshold)
    warehouse.add_inventory_item(item)
    print("Inventory item added successfully.")

def order_from_supplier(warehouse):
    supplier_id = input("Enter supplier ID: ")
    item_id = input("Enter item ID: ")
    amount = int(input("Enter amount to order: "))

    warehouse.order_from_supplier(supplier_id, item_id, amount)

def view_inventory(warehouse):
    print("\n--- Inventory ---")
    for item_id, item in warehouse.inventory.items():
        details = item.get_item_details()
        print(f"Item ID: {details['Item ID']}, Name: {details['Name']}, Quantity: {details['Quantity']}, Low Stock Alert: {details['Low Stock Alert']}")

def place_order(warehouse, customer):
    item_id = input("Enter item ID: ")
    amount = int(input("Enter amount to order: "))

    warehouse.place_customer_order(customer, item_id, amount)

def view_order_history(customer):
    print("\n--- Order History ---")
    for order in customer.purchase_history:
        print(f"Item: {order.item.name}, Amount: {order.amount}, Status: {order.status}")

if __name__ == "__main__":
    main_menu()