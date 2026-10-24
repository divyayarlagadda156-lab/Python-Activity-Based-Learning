# ============================================================
# Case Study 9: E-Commerce Orders Processing
# Roll: 26000985 | Section: CSM2
# Name: Yarlagadda Divya Sita Maha Lakshmi
# ============================================================
# Problem Statement:
# Process e-commerce orders and calculate final billing
# Apply discounts, GST, and generate invoice report
#
# Objectives: Use nested lists, dictionary, loops, functions
# Algorithm:
# 1. Start
# 2. Initialize product catalog as dictionary {ID: [Name, Price]}
# 3. Initialize orders as nested list [OrderID, ProductID, Qty]
# 4. For each order, find product price from catalog
# 5. Calculate subtotal = price * qty
# 6. Apply discount: 10% if qty>2, 15% if qty>5
# 7. Apply GST 18% on discounted price
# 8. Calculate final total and store in invoice list
# 9. Display invoice report with grand total
# 10. Stop
#
# Flowchart: Start -> Catalog -> Orders Loop -> Price Calc -> Discount -> GST -> Invoice -> Stop
# ============================================================

def calculate_discount(qty, amount):
    """Function to calculate discount based on quantity"""
    if qty > 5:
        return amount * 0.15
    elif qty > 2:
        return amount * 0.10
    else:
        return 0

def main():
    # Product Catalog - Dictionary with list values
    catalog = {
        "P101": ["Python Book", 450],
        "P102": ["Laptop Bag", 1200],
        "P103": ["Wireless Mouse", 650],
        "P104": ["Keyboard", 1100],
        "P105": ["USB Drive 64GB", 350]
    }

    # Orders - Nested List [OrderID, ProductID, Quantity, Customer]
    orders = [
        ["ORD001", "P101", 2, "Divya_26000985"],
        ["ORD002", "P102", 1, "Rahul"],
        ["ORD003", "P103", 4, "Priya"],
        ["ORD004", "P105", 6, "Anjali"],
        ["ORD005", "P104", 3, "Karthik"]
    ]

    print("===== E-Commerce Orders - 26000985 =====")
    print(f"{'OrderID':<10} {'Product':<18} {'Qty':<5} {'Price':<7} {'SubTotal':<10} {'Disc':<7} {'GST':<7} {'Final'}")
    print("-" * 95)

    grand_total = 0
    invoices = []

    for order in orders:
        order_id, prod_id, qty, customer = order  # List unpacking

        if prod_id not in catalog:
            print(f"{order_id:<10} Product not found")
            continue

        prod_name, prod_price = catalog[prod_id]

        subtotal = prod_price * qty
        discount = calculate_discount(qty, subtotal)
        after_discount = subtotal - discount
        gst = after_discount * 0.18
        final_amount = after_discount + gst

        grand_total += final_amount
        invoices.append([order_id, prod_name, qty, final_amount])

        print(f"{order_id:<10} {prod_name:<18} {qty:<5} {prod_price:<7} {subtotal:<10} {discount:<7.0f} {gst:<7.0f} {final_amount:.0f}")

    print("-" * 95)
    print(f"Grand Total of All Orders: Rs. {grand_total:.2f}")

    print(f"\n--- Customer Wise Summary ---")
    for order in orders:
        print(f"  {order[3]} ordered {order[2]} x {catalog[order[1]][0]}")

    print(f"\n--- High Value Orders (>2000) ---")
    for inv in invoices:
        if inv[3] > 2000:
            print(f"  {inv[0]}: {inv[1]} - Rs.{inv[3]:.0f}")

if __name__ == "__main__":
    main()
