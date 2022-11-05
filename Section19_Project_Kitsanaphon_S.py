from tkinter import *


def clear():
    global expression
    global label_show_cal
    result = "0"
    expression = ""
    label_show_cal.set(result)

def press(number):
    global expression
    global label_show_cal
    expression = expression + number
    label_show_cal.set(expression)

def equal():
    try:
        global expression
        global label_show_cal
        result = str(eval(expression))
        label_show_cal.set(result)
    except:
        result = "Error"
        expression = ""
    label_show_cal.set(result)


main_windows = Tk()
main_windows.option_add("*font", "consolas 30")
main_windows.configure(background="black")
main_windows.title("Calculator")
label_show_cal = StringVar()
label_show_cal.set(0)
expression = ""


Label(main_windows, textvariable=label_show_cal).grid(row=0, column=0, columnspan=4)
Button(main_windows, text="clear",bg ="#9E9E9E",fg = "white",command=clear).grid(row=1, column=0, columnspan=4, sticky="news")

Button(main_windows, text="7",bg ="black",fg = "white", command=lambda: press("7")).grid(row=2, column=0)
Button(main_windows, text="8",bg ="black",fg = "white", command=lambda: press("8")).grid(row=2, column=1)
Button(main_windows, text="9",bg ="black",fg = "white", command=lambda: press("9")).grid(row=2, column=2)
Button(main_windows, text="÷",bg ="#DC7633",fg = "white", command=lambda: press("/")).grid(row=2, column=3)

Button(main_windows, text="4",bg ="black",fg = "white", command=lambda: press("4")).grid(row=3, column=0)
Button(main_windows, text="5",bg ="black",fg = "white", command=lambda: press("5")).grid(row=3, column=1)
Button(main_windows, text="6",bg ="black",fg = "white", command=lambda: press("6")).grid(row=3, column=2)
Button(main_windows, text="x",bg ="#DC7633",fg = "white", command=lambda: press("*")).grid(row=3, column=3)

Button(main_windows, text="1",bg ="black",fg = "white", command=lambda: press("1")).grid(row=4, column=0)
Button(main_windows, text="2",bg ="black",fg = "white", command=lambda: press("2")).grid(row=4, column=1)
Button(main_windows, text="3",bg ="black",fg = "white", command=lambda: press("3")).grid(row=4, column=2)
Button(main_windows, text="-",bg ="#DC7633",fg = "white", command=lambda: press("-")).grid(row=4, column=3)

Button(main_windows, text="0",bg ="black",fg = "white", command=lambda: press("0")).grid(row=5, column=1, columnspan=2, sticky="news")
Button(main_windows, text=".",bg ="black",fg = "white", command=lambda: press(".")).grid(row=5, column=0)
Button(main_windows, text="+",bg ="#DC7633",fg = "white", command=lambda: press("+")).grid(row=5, column=3)

Button(main_windows, text="=",bg ="#9E9E9E",fg = "white", command=equal).grid(row=6, column=0, columnspan=4, sticky="news")

main_windows.mainloop()


