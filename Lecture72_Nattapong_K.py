# Bill > List in List

menuList = []

def showBill():
    print("------ FOOD ------")
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])

while True:
    menuName = input("Please insert food menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append([menuName, menuPrice])

showBill()