# แบ่งโค้ดออกเป็นฟังก์ชั่นและเรียกการใช้งาน

def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        print("Login Success")
        showMenu()
    else:
        print("Invalid please try again")
        login()
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    print("-----------------")
    userSelect = int(input("Choose 1 or 2 : "))
    menuSelect(userSelect)
def menuSelect(userSelect):
    if userSelect == 1:
        totalPrice = int(input("Enter a price : "))
        print("Total price with VAT is",vatCalculator(totalPrice))
    elif userSelect == 2:
        print("Total product price with VAT is",priceCalculator())
def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

login() # เรียกการใช้งาน