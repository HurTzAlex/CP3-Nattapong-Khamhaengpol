print("Enter your Username and Password")
userInput = input("Username : ")  # admin
passInput = input("Password : ")  # 1234

if userInput == "admin" and passInput == "1234":
    print("----- Welcome to Ma-Aow-Rai Coffee Shop -----")
    print("--------------------------------------------")
    print("What would you like to drink today?")
    print("-------------------- Menu ------------------")
    print("             1. Americano 100B")
    print("             2. Latte 120B")
    print("             3. Cappuccino 120B")
    print("             4. Mocha 130B")
    print("             5. Macchiato 130")
    print("             6. Thai tea 55")
    print("             7. Green tea 55")
    print("             8. Lemon tea 65")
    print("             9. Chocolate 120")
    print("----------- What would you like ? ------------")
    print("----------------------------------------------")

    listSelected = int(input("INPUT NUMBER : "))

    if listSelected == 1:
        orderName = "Americano"
        orderPrice = 100
        print("How many items do u want?")
        item = int(input(": "))
        total = orderPrice * item
    elif listSelected == 2:
        orderName = "Latte"
        orderPrice = 120
        print("How many items do u want?")
        item = int(input(": "))
        total = orderPrice * item
    elif listSelected == 3:
        orderName = "Cappuccino"
        orderPrice = 120
        print("How many items do u want?")
        item = int(input(": "))
        total = orderPrice * item
    elif listSelected == 4:
        orderName = "Mocha"
        orderPrice = 130
        print("How many items do u want?")
        item = int(input(": "))
        total = orderPrice * item
    elif listSelected == 5:
        orderName = "Macchiato"
        orderPrice = 130
        print("How many items do u want?")
        item = int(input(": "))
        total = orderPrice * item
    elif listSelected == 6:
        orderName = "Thai tea"
        orderPrice = 55
        print("How many items do u want?")
        item = int(input(": "))
        total = orderPrice * item
    elif listSelected == 7:
        orderName = "Green tea"
        orderPrice = 55
        print("How many items do u want?")
        item = int(input(": "))
        total = orderPrice * item
    elif listSelected == 8:
        orderName = "Lemon tea"
        orderPrice = 65
        print("How many items do u want?")
        item = int(input(": "))
        total = orderPrice * item
    elif listSelected == 9:
        orderName = "Chocolate"
        orderPrice = 120
        print("How many items do u want?")
        item = int(input(": "))
        total = orderPrice * item

    print(orderName, orderPrice, "x", item)
    print("Your order is ", orderName, orderPrice, "x", item, " = ", total, "Baht")
    print("----------------------------------------------")
    print("---------------- Thank you -------------------")
    print("-------------- Enjoy your day ----------------")
    print("----------------------------------------------")

else:
    print("Invalid")