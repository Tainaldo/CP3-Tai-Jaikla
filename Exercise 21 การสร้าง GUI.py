from tkinter import *
import math

def leftClickButton(event):
    return Fresult()

def Fresult():
    result = float(textBoxWeight.get())/math.pow(float(textBoxHight.get())/100,2)
    if result > 30 :
        print("อ้วนมาก")
        textresult = "อ้วนมาก"
    elif result >= 25 and result < 29.9:
        textresult = "อ้วน"
    elif result >= 23 and result < 24.9:
       textresult = "น้ำหนักเกิน"
    elif result >= 18.6 and result < 22.9:
        textresult = "น้ำหนักปกติ เหมาะสม"
    else:
        print("ผอมเกินไป") 
        textresult = "ผอมเกินไป"
    labelResult.configure(text=textresult)


MainWindow = Tk()
labelHight = Label(MainWindow,text="ส่วนสูง(cm)")
labelHight.grid(row=0,column=0)
textBoxHight = Entry(MainWindow)
textBoxHight.grid(row=0,column=1)
labelWeight = Label(MainWindow,text="น้ำหนัก(Kg)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text="คำนวน")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)
MainWindow.mainloop()