# Pyhton Gui library # * means You can only use functions and properties your program can access (use)
from tkinter import *
from PIL import ImageTk, Image  # immage library , use to set a image #pillow

# These four global varrible -- We can access anywhere
global e1
global e2
global taxText
global nsalText


root = Tk()  # 'Tk()' use to display the root (main) window and manages all the other components of the tkinter application
# *******************************
root.configure(bg='yellow')
# # ********************************
# imgTemp = Image.open("bg.png")
# img2 = imgTemp.resize((1300, 800))
# img = ImageTk.PhotoImage(img2)

# label = Label(root, image=img)

# label.pack(pady=5)


def calculate(amount, percent):
    percent_tax.set(percent)
    return (amount * percent) / 100


def Ok():
    total_income = float(e2.get())

    if total_income <= 250000:
        t_tax = 0
    elif total_income <= 500000:
        t_tax = calculate(total_income -
                          250000, 5)
    elif total_income <= 750000:
        t_tax = calculate(total_income -
                          500000, 10) + 12500
    elif total_income <= 1000000:
        t_tax = calculate(total_income -
                          750000, 15) + 37500
    elif total_income <= 1250000:
        t_tax = calculate(total_income -
                          1000000, 20) + 75000
    elif total_income <= 1500000:
        t_tax = calculate(total_income -
                          1250000, 25) + 125000
    else:
        t_tax = calculate(total_income -
                          1500000, 30) + 187500

    if total_income > 250000:

        total_tax = (t_tax+(t_tax*4)/100)
        taxText.set(total_tax)
        nsalText.set(total_income-total_tax)

    # ****************************************************************
    #     Output of the event(action) And Where should display, use to display
        Label(root, text="\t\t\t\t\t", bg='yellow', fg="white",
              font='Arial 17 bold').place(x=500, y=330)

        Label(root, text="Tax in percentage (%) ", bg="Green",
              fg="white", relief=RIDGE, font='Arial 17 bold').place(x=500, y=270)

        Label(root, text=r"Taxable Income + 4% cess ", bg="Green",
              fg="white", relief=RIDGE, font='Arial 17 bold').place(x=500, y=390)
        Label(root, text="After deduction of Taxable Income ", bg="Green",
              fg="white", relief=RIDGE, font='Arial 17 bold').place(x=500, y=510)
#       ************************************************************

        Label(text="", textvariable=percent_tax, width=20,
              font=('Arial 14')).place(x=525, y=330)
        Label(text="", textvariable=taxText, width=20,
              font=('Arial 14')).place(x=525, y=450)
        Label(text="", textvariable=nsalText, width=20,
              font=('Arial 14')).place(x=525, y=570)


#   *******************************************
    else:
        Label(root, text="\t\t\t\t\t", bg='yellow', fg="white",
              font='Arial 17 bold').place(x=500, y=270)
        Label(root, text="\t\t\t\t\t", bg='yellow', fg="white",
              font='Arial 17 bold').place(x=500, y=390)
        Label(root, text="\t\t\t\t\t", bg='yellow', fg="white",
              font='Arial 17 bold').place(x=500, y=510)
        Label(root, text="\t\t\t\t\t", bg='yellow', fg="white",
              font='Arial 17 bold').place(x=525, y=330)
        Label(root, text="\t\t\t\t\t", bg='yellow', fg="white",
              font='Arial 17 bold').place(x=525, y=450)
        Label(root, text="\t\t\t\t\t", bg='yellow', fg="white",
              font='Arial 17 bold').place(x=525, y=570)
# **********************************
        Label(root, text=" YOU ARE NOT UNDER THE TAX SLAB ", bg="Green",
              fg="white", relief=RIDGE, font='Arial 17 bold').place(x=500, y=330)


# ?************************************************************

def quit():
    root.destroy()  # Exit the main screen
    # **************************************


percent_tax = StringVar()
taxText = StringVar()
nsalText = StringVar()


# *******************************************
root.title("Employee salary Tax calculator system")  # Title of Gui
root.geometry("1500x1000")  # Size of that GUI
root.resizable(0, 0)

# ***********************************************
# Some Attributes which should be display o the screen...
Label(root, text=" Name ", bg="blue",
      fg="white", relief=RIDGE, font='Arial 17 bold').place(x=550, y=30)
Label(root, text="Income ", bg="blue",
      fg="white", relief=RIDGE, font='Arial 17 bold').place(x=550, y=130)

# /////////////////////////********************************

e1 = Entry(root, width=20, font=('Arial 14'))  # Taking Input from user
e1.place(x=500, y=90)  # Where e1 should display
e2 = Entry(root, width=20, font=('Arial 14'))
e2.place(x=500, y=190)
# **************************************************

# for calculate tax, after clicking it wil call ok() function
Button(root, text="Calculate", command=Ok, font='Arial 17 bold',
       height=3, width=10, bg="blue",
       fg="white", relief=RAISED).place(x=750, y=110)

# ****************************************************
# After clicke on QUITE button, exit from entire screen, by calling QUIT() finction
Button(root, text="QUIT",  font='Arial 17 bold', command=quit,
       height=2, width=5, bg="red",
       fg="white", relief=RAISED).place(x=350, y=110)
#  ************************************
Label(root, text=" INCOME TAX CALCULATOR ", bg="blue",
      fg="white", relief=RIDGE, font='Arial 25 bold').place(x=500, y=700)
#   *************************************************
# tells Python to run the Tkinter event (action) in loop ----AND----- use listens(Taking input) for events, such as button clicks or Input etc.
root.mainloop()  # use to hold the screen
