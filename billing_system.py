import random

finalitem = []

def Item(name):
    if name == "paneer":
        w = float(input("Enter quantity (kg): "))
        finalitem.append({"name": "Paneer", "qty": f"{w} kg", "mrp": "₹250/kg", "total": w * 250})

    elif name == "milk":
        w = float(input("Enter quantity (litre): "))
        finalitem.append({"name": "Milk", "qty": f"{w} L", "mrp": "₹60/L", "total": w * 60})

    elif name == "rice":
        w = float(input("Enter quantity (kg): "))
        finalitem.append({"name": "Rice", "qty": f"{w} kg", "mrp": "₹50/kg", "total": w * 50})

    elif name == "wheat":
        w = float(input("Enter quantity (kg): "))
        finalitem.append({"name": "Wheat", "qty": f"{w} kg", "mrp": "₹40/kg", "total": w * 40})

    elif name == "sugar":
        w = float(input("Enter quantity (kg): "))
        finalitem.append({"name": "Sugar", "qty": f"{w} kg", "mrp": "₹45/kg", "total": w * 45})

    elif name == "salt":
        w = float(input("Enter quantity (kg): "))
        finalitem.append({"name": "Salt", "qty": f"{w} kg", "mrp": "₹20/kg", "total": w * 20})

    elif name == "oil":
        w = float(input("Enter quantity (litre): "))
        finalitem.append({"name": "Oil", "qty": f"{w} L", "mrp": "₹120/L", "total": w * 120})

    elif name == "egg":
        w = float(input("Enter quantity (pieces): "))
        finalitem.append({"name": "Egg", "qty": f"{w} pcs", "mrp": "₹6/pc", "total": w * 6})

    elif name == "bread":
        w = float(input("Enter quantity (packet): "))
        finalitem.append({"name": "Bread", "qty": f"{w} pkt", "mrp": "₹30/pkt", "total": w * 30})

    elif name == "butter":
        w = float(input("Enter quantity (packet): "))
        finalitem.append({"name": "Butter", "qty": f"{w} pkt", "mrp": "₹55/pkt", "total": w * 55})

    else:
        print("Item not available")

while True:
    x = input("Enter item name (or press Enter to stop): ").lower()
    if x == "":
        break
    Item(x)

a = random.randint(1000, 9999)

y = input("Enter the name of customer: ")
z = input("Enter the date: ")
p = input("Enter the month: ")
q = input("Enter the year: ")

print("_______________________________________________________")
print("""
        Green Valley
        SUPERMARKET
J.T. Road, Thalassery-670102
Phone: 0490 23 44588 903 73 44588
Form B under KVAT Rules 2005
TIN: 32120893203
FSSAI: 11314013001023

        RETAIL INVOICE
""")

print("Sold To:", y)
print("Date:", z, "/", p, "/", q, "   ", "Bill No:", a)
print("--------------------------------------------")
print(f"{'Item_Name':<15}{'Qty':<10}{'MRP':<10}{'Total':<10}")
print("--------------------------------------------")

total = 0

for item in finalitem:
    print(f"{item['name']:<15}{item['qty']:<10}{item['mrp']:<10}{item['total']:<10.2f}")
    total += item['total']

print("--------------------------------------------")
print(f"{'Grand Total':<35}{total:.2f}")