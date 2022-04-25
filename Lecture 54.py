def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    while usernameInput != "admin" or passwordInput != "1234":
        print("Login agin")
        usernameInput = input("Username : ")
        passwordInput = input("Password : ")
    return showMenu()
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return print(selectMenu())
def selectMenu():
    userSelected = int(input(">>"))
    if userSelected==1:
        print(vatCalculate())
    elif userSelected == 2:
        print(priceCalculate())
    return userSelected
def vatCalculate(price):
    vat = 7
    return price + (price * vat / 100) # result = price + (price * vat / 100)
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return print(vatCalculate(price1 + price2))

print(login())

