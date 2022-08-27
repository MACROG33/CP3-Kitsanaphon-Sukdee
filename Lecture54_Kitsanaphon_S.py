def login():
    print("Please, Enter your Username and Password")
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "MACROG" and passwordInput == "321":
        return True
    else:
        return False
def showMenu():
    print("----Nothing shop----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userSelected = int(input(">>"))
    return userSelected
def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def priceCalculate():
    price1 = int(input("First ProductPrice : "))
    price2 = int(input("Second ProductPrice : "))
    return vatCalculate(price1 + price2)

if login() == True:
    showMenu()
    result = menuSelect()
    if result ==  1:
        totalPrice = int(input("Total Price:"))
        print("Total Price Include Vat :", vatCalculate(totalPrice))
    elif result ==  2:
        print("Price Calculate Include Vat :",priceCalculate())
else:
    print("Incorrect Username or Password")
print("-------THANK YOU--------")


