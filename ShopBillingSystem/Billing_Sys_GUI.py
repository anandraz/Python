from tkinter import *
import datetime


root = Tk()
root.geometry("800x500")   #Screen  Size
root.title("Shop Billing system")

root.configure(background='Grey') # Change Creen background color 

####################################################################################
######################### Customer Info ############################################
Label (text = "Customer Details", bg="white", fg="green").grid(row=1, column = 1)

#Entry box name
Label (text = "Customer Name").grid(row=2, column = 1)
Label (text = "Contact No.").grid(row=2, column = 3)
Label (text = "Bill No.").grid(row=2, column = 5)

# Define Input value of Entry box
CustomerNameEntry = Entry(root, textvariable=StringVar(), width=20)
ContactEntry = Entry(root, textvariable=StringVar(), width=10)
BillEntry = Entry(root, textvariable=StringVar(), width= 10)

# Entry Box alignment   
CustomerNameEntry.grid(row=2, column=2, padx= 10, pady=10)
ContactEntry.grid(row=2, column=4, padx=10, pady=10)
BillEntry.grid(row=2, column=6, padx= 10, pady=10)

####################################################################################
######################### Products Info ################################################
Label (text = "Product Details", bg= "White", fg="green").grid(row=3, column = 1)

root.mainloop()



