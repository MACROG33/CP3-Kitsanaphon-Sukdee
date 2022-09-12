from tkinter import *
import math

def leftClickButton(event):
    print(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    labelResult.configure(text=(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)))
    BMI =(float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2))
    ShowValue = ""

    if float(BMI) <= 18.5:
        ShowValue = "ผอมเกินไป"

    elif float(BMI) > 18.5 and float(BMI) <= 22.9:
        ShowValue = "น้ำหนักปกติ เหมาะสม"

    elif float(BMI) >= 23 and float(BMI) <= 24.9:
        ShowValue = "น้ำหนักเกิน"

    elif float(BMI) >= 25 and float(BMI) <= 29.9:
        ShowValue = "อ้วน"

    elif float(BMI) >= 30:
        ShowValue = "อ้วนมาก"

    labelResult.configure(text=ShowValue)

MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.bind("<Button-1>",leftClickbutton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow, text="ผลลัพธ์")
labelResult.grid(row=2,column=1)
MainWindow.mainloop()