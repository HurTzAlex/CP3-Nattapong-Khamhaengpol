menuList = []
priceList = []

def showBill():
    resName = "Sawasdee Restaurant"
    print(resName.center(27,"-"))

    for number in range(len(menuList)):
        print(menuList[number],":" ,priceList[number])

def totalPrice():
    total = 0
    for price in priceList:
        total += price
    return total

while True:
    menuName = input("Enter your menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()
print("-".center(27,"-"))
print("Total :", totalPrice(),"Baht")
print("-".center(27,"-"))
