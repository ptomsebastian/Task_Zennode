import math
products={"Product A": 20, "Product B": 40, "Product C": 50}
cart=[]
subtotal=0
total_quantity=0
gift_wrap_fee=0
shipping_fee=0
discount=None

for product, price in products.items():
    quantity= int(input(f"Enter quantity for {product}: "))
    gift_wrap= input(f"Do you want gift wrap for {product} [yes/no] ").lower() == 'yes' #returns True or False

    item ={"product": product, "quantity": quantity, "total_price": price * quantity, "gift_wrap": gift_wrap}
    cart.append(item) #updating cart
    # print('Cart', cart)
    subtotal+=item["total_price"]
    total_quantity+=quantity
    # print('sub_tot', subtotal)
    # print('tot_qu', total_quantity)


tiered_50 = False
for i in cart:
    if total_quantity > 30 and i["quantity"] > 15:
        tiered_50 = True
        break

if tiered_50:
    discount = ("tiered_50_discount", subtotal * 0.5)
elif total_quantity > 20:
    discount = ("bulk_10_discount", 10)
elif total_quantity > 10:
    # print("bulk_5_discount applied")
    discount = ("bulk_5_discount", subtotal * 0.05)
elif subtotal > 200:
    discount = ("flat_10_discount", 10)

# print(discount)

for i in cart:
    if i["gift_wrap"]:
        gift_wrap_fee+=1  #$1 for each giftwrap


shipping_fee = math.ceil(total_quantity / 10) * 5 #$5 per package

print("\nOrder History:\n--------------")
for i in cart:
    print(f"You ordered {i['quantity']} {i['product']} => Total: ${i['total_price']}")

print(f"\nSubtotal=> ${subtotal}")
if discount:
    print(f"Discount Applied=> {discount[0]} -> Amount: ${discount[1]}")

print(f"Gift Wrap Fee=> ${gift_wrap_fee}")
print(f"Shipping Fee=> ${shipping_fee}")

total= subtotal - (discount[1] if discount else 0) + gift_wrap_fee + shipping_fee
print("-----------------------")
print(f"Total Amount=> ${total}")
