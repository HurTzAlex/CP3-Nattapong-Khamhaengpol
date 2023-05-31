# Dictionary > Total Price

systemMenu = {"ข้าวมันไก่ต้ม": 20, "ข้าวมันไก่ทอด": 20, "ข้าวมันไก่ผสม": 30, "ไก่ต้ม": 40, "ไก่ทอด": 40}
menuList = []

def showBill():
    print("----- Midnight Kao man Kai -----")
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])

    totalPrice = 0
    for total in menuList:
        totalPrice += total[1]
    print("Total :",totalPrice)

while True:
    menuName = input("Insert menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        if (menuName in systemMenu):
            menuList.append([menuName, systemMenu[menuName]])
        else:
            print("Menu not found!")
showBill()