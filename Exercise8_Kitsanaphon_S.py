print("Please, Enter your Username and Password")
usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "MACROG" and passwordInput == "321":
    print("----Welcome to Nothing shop----")
    print("Please select a product")
    Pepsi = 15
    CocaCola = 10
    Orange = 20
    print(" Product 1  =   Pepsi    x 1  :", Pepsi,    "THB")
    print(" Product 2  =   CocaCola x 1  :", CocaCola, "THB")
    print(" Product 3  =   Orange  x 1  :",  Orange,   "THB")
    SelectedProduct = int(input("SelectedProduct >> "))

    if SelectedProduct == 1:
        Product = "Pepsi"
        number = int(input("Enter number of item : "))
        total = Pepsi * number
    elif SelectedProduct == 2:
        Product = "CocaCola"
        number = int(input("Enter number of item :"))
        total = CocaCola * number
    elif SelectedProduct == 3:
        Product = "Orange"
        number = int(input("Enter number of item :"))
        total = Orange * number
    else:
        Product = "Not found"
        number = 0
        total = 0
    print(Product, "x", number, "total =", total, "THB")
    print("----------THANK YOU----------")
