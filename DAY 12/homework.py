quantity1=float(input("Enter the first product quantity (KG): "))
quantity2=float(input("Enter the second product quantity (KG): "))
quantity3=float(input("Enter the third product quantity (KG): "))
quantity4=float(input("Enter the fourth product quantity (KG): "))
quantity5=float(input("Enter the fifth product quantity (KG): "))

shoping_cart1=[quantity1,quantity2,quantity3,quantity4,quantity5]
my_quantity=0

for quantity in shoping_cart1:
    my_quantity=my_quantity+quantity

print("The total quantity of the product : ",my_quantity)


price1=float(input("Enter the first product price : "))
price2=float(input("Enter the second product price : "))
price3=float(input("Enter the third product price : "))
price4=float(input("Enter the fourth product price : "))
price5=float(input("Enter the fifth product price : "))

shoping_cart2=[price1,price2,price3,price4,price5]
my_price=0

for price in shoping_cart2:
    my_price=my_price+price

print("The total price of the product without TAX : ",my_price)

def tax_calculator(tp,tr):
    result=tp*tr
    return result

