class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Add product to",self.name,self.lastname,"s cart")

customer1 = Customer()
customer1.name = "Kitsanaphon"
customer1.lastname = "Sukdee"
customer1.addCart()
customer2 = Customer()
customer2.name = "Kittipong"
customer2.lastname ="laiwong"
customer2.addCart()
customer3 = Customer()
customer3.name = "Palm"
customer3.lastname ="lnWza"
customer3.addCart()
customer4 = Customer()
customer4.name = "Kirito"
customer4.lastname ="007"
customer4.addCart()