from cgi import test


username = input("Username : ")
password = input("Password : ")

if (username=="1" and password=="123456"):
    print("\nWelcome!!!\n")
    print("----------TJK Shop----------\n")
    print("1. กล้วย   10 บาท")
    print("2. ส้ม      5 บาท")
    print("3. แอปเปิ้ล 20 บาท")
    want = input("\nสิ้นค้าที่ต้องการ :")
    if (want == "1"):
        banana = int(input("กล้วย จำนวน "))
        print("กล้วย x",banana,"=",banana*10,"บาท") # *10 คือ 10บาท
    elif (want == "2"):
        orange = int(input("ส้ท จำนวน "))
        print("ส้ม x",orange,"=",orange*5,"บาท") 
    elif (want == "3"):
        apple = int(input("แอปเปิ้ล จำนวน "))
        print("แอปเปิ้ล x",apple,"=",apple*20,"บาท")
    print("\nTank you!")
else:
    print("รหัสผ่านผิด")
