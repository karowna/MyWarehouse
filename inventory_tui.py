
from inventory_classes import Person, Supplier, InventoryItem

def main_menu():
    supplier = Supplier("John Doe", "+1234567890", "john@example.com", "SUP123")
    item = InventoryItem("ITEM001", "BRICKS", "BUILD BUILD", 50, 10)

    while True:
        print("\n--- Main Menu ---")
        print("1. View Supplier Contact")
        print("2. Update Supplier Contact")
        print("3. View Order History")
        print("4. View Inventory Item")
        print("5. Receive Stock")
        print("6. Reduce Stock")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            contact = supplier.get_contact_details()
            print(f"Name: {supplier._name}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
        elif choice == "2":
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            supplier.set_contact_details(phone, email)
            print("Contact updated.")
        elif choice == "3":
            print("Order History:", supplier.get_order_history())
        elif choice == "4":
            for k, v in item.get_item_details().items():
                print(f"{k}: {v}")
        elif choice == "5":
            try:
                amount = int(input("Enter amount to receive: "))
                item.receive_stock(amount)
            except ValueError:
                print("Invalid input.")
        elif choice == "6":
            try:
                amount = int(input("Enter amount to reduce: "))
                item.reduce_stock(amount)
            except ValueError:
                print("Invalid input.")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
