num1 =float(input("the price of each shirts = "))
num2 =float(num1 * 3)
print("the price of total shirts = ", num2)

num3 =float(input("the price of each T-shirts = "))
num4 =float(num3 * 2)
print("the price of total T-shirts = ", num4)

num5 =float(input("the price of 1 pair of shoes = "))
num6 =float(input("the price of a punjabi = "))

num7 = num2+num4+num5+num6

print("the total price without shoes = ", num2+num4+num6 )
print("the total price of all products = ", num7 )

num8 = float(num7 * 0.03)
print("the discount amount = ", num8)

print("the total paymet after discount = ", num7-num8)
