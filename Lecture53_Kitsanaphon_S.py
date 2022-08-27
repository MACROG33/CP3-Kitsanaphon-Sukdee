price = int(input("Price: "))
def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
print(vatCalculate(price))
print("-------successfully-------")