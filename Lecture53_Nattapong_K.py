# Vat Calculate (7%)
# Function return

# Ex.1
def vatCalculate(totalPrice):
    result = totalPrice + (totalPrice*7/100)
    return result
number = float(input("Enter a number : "))
print("The total amount including VAT is", vatCalculate(number))

# Ex.2
def calculate_vat(num):
    vatRate = 0.07
    vat = num * vatRate
    total = num + vat
    return total
num = float(input("Enter a number : "))
total = calculate_vat(num)

print(f"The total amount including VAT is {total}")