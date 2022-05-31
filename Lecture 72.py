menuList = []

def showBill():
    totalPrice = 0
    print("---- My Food ----")
    for food in range(len(menuList)):
        print(menuList[food][0],menuList[food][1])
        totalPrice += int(menuList[food][1])
    print("ราคาทั้งหมด :",totalPrice,"บาท")

while True: 
    menuName = input("Please Enter Menu :")
    if (menuName.capitalize() == "Exit"): 
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName,menuPrice])
print(menuList)
showBill()