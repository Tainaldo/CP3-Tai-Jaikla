menuList = []
priceList = []

def showBill():
    print("---- My Food ----")
    totalPrice = 0
    for food in range(len(menuList)):
        print(menuList[food],priceList[food])
        totalPrice += int(priceList[food])
    print("ราคาทั้งหมด :",totalPrice ,"บาท")

while True: #ให้ผู้ใช้งานพิมพ์มาเรื่อยๆ
    menuName = input("Please Enter Menu :")
    if (menuName.capitalize() == "Exit") : #กรณีที่น่าจะเกิดขึ้น
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()