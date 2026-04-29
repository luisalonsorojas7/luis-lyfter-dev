'''6. Cree un pseudocódigo que le pida un precio de producto al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:
Si el precio es menor a 100, el descuento es del 2%.
Si el precio es mayor o igual a 100, el descuento es del 10%.
'''

product_price = float(input("Please enter the product price to calculate the discount: \n")) 
discount_amount = 0
final_price = 0

if product_price >= 100:
    discount_amount = product_price * 0.10
else:
    discount_amount = product_price * 0.02

final_price = product_price - discount_amount

print(f"Product price with discount is: {final_price}")