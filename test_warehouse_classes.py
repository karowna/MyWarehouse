import unittest
from warehouse_classes import Warehouse, Supplier, InventoryItem

class TestWarehouse(unittest.TestCase):
    def test_inventory_item_duplication(self):
        warehouse = Warehouse()
        supplier = Supplier("Acme Supplies", "1234567890", "acme@example.com", "SUP001")
        item = InventoryItem("ITEM001", "Widget", "A useful widget", 10.0, quantity=100, low_stock_threshold=10)
        supplier.add_inventory_item(item)
        warehouse.add_supplier(supplier)

        # First order
        warehouse.order_from_supplier("SUP001", "ITEM001", 10)
        self.assertIn("ITEM001", warehouse.inventory)
        self.assertEqual(warehouse.inventory["ITEM001"].quantity, 10)

        # Second order (should not duplicate item, just increase quantity)
        warehouse.order_from_supplier("SUP001", "ITEM001", 5)
        self.assertEqual(len(warehouse.inventory), 1)  # Still only one item
        self.assertEqual(warehouse.inventory["ITEM001"].quantity, 15)

        print("Test passed: No duplication and quantity updated correctly.")

if __name__ == "__main__":
    unittest.main()


