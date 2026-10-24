def place_order(item):
    print(f"Order placed: Your order is {item}")

#eggs => 4
#tot = (base_price + 4) * 0.15
def calculate_total(item):
    base_price = 25.5
    VAT = 0.15
    total = (base_price + len(item)) * VAT
    return total

def get_order():
    print("Preparing order ...")
    return "Collect your order!"

myFood = input("What would you like? ")
place_order(myFood)

print(get_order())

order_total = calculate_total(myFood)
#print(f"Your order costs: R{order_total:.2f}")
print(f"Your order costs: R{round(order_total,2)}")

