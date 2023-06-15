class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Added product to "+self.name,self.lastname+"'s Cart")

customer1 = Customer()
customer1.name = "Alex"
customer1.lastname = "K"

customer2 = Customer()
customer2.name = "Charles"
customer2.lastname = "M"

customer3 = Customer()
customer3.name = "Steward"
customer3.lastname = "A"

customer4 = Customer()
customer4.name = "Tony"
customer4.lastname = "Z"

customer1.addCart()
customer2.addCart()
customer3.addCart()
customer4.addCart()