systemMenu = {"ข้าวไก่ทอด":40,"ข้าวไข่เจียว":30,"ข้าวหน้าเนื้อ":60,"ข้าวหน้าปลาไหล":60}
menuList = []
def showBill():
    total = 0
    print("----Nothing Shop----")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        total += int(menuList[number][1])
    print("Total :",total,"THB")
while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])
showBill()
print("-----THANK YOU-----")

