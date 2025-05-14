products = []
prices = []
total = 0

while True:
    product = input("Enter the product (Enter E to Escape): ")
    if product.upper() == "E":
        break
    else:
        price = float(input(f"Please enter the price of {product}: "))
        products.append(product)
        prices.append(price)


    
if len(products) > 1:
    print("\n*****YOUR ITEMS*****\n")

else:
    print("\n*****YOUR ITEM*****")
    
    
for i in range(len(products)):
    print(f"{i+1}. {products[i]} - {prices[i]} Rs")

for price in prices:
    total += price

points = total/100

print(f"\nYour total is {total}")
print(f"Total points earned {points}")
print("\n*** THANK YOU ***")