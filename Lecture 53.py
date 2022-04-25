def vatCalculate(totalPrice):
    result=totalPrice+(totalPrice*7/100)
    return result

money = int(input("จำนวนเงิน :"))
print(vatCalculate(money))