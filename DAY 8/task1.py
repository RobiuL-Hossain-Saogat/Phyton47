def tax_calculator(S,TR):
    Tax_Amount=S*TR
    return Tax_Amount

Salary=float(input("Enter the salary : "))
Tax_Rate=float(input("Enter the Tax Rate : "))

print(tax_calculator(Salary,Tax_Rate))