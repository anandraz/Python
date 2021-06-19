from tkinter import *
from datetime import date

root = Tk()  # Create object from tkinter
root.geometry("500x300")   #Screen  Size
root.title("Age Calculator")

# Enable below commented code to add image as Logo on Top of screen
"""
photo = PhotoImage(file="AgeCalculator/Age_Grow.png")
Label(image=photo).grid(row=0, column=1) 
"""
def calculateAge():
    today = date.today()
    birthDate = date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))
    age= today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    Label(text=f"Your Age is : {age}", bg="Yellow").grid(row=7, column=1)

Label(text="|| Age Caluculator ||", font=('Helvetica', 18, 'bold'), bg='#fff', fg='green').grid(row=1, column=1)

#Entry box name
Label(text="| Date Of Birth |").grid(row=2, column=0)
Label(text="Day [DD]").grid(row=3, column=0)
Label(text="Month [MM]").grid(row=3, column=1)
Label(text="Year [YYYY]").grid(row=3, column=2)

# Define Input value of Entry box
yearEntry = Entry(root, textvariable=StringVar(), width=10)
monthEntry = Entry(root, textvariable=StringVar(), width=10)
dayEntry = Entry(root, textvariable=StringVar(), width=10)

# Entry Box alignment                          
dayEntry.grid(row=4, column=0, pady=10)
monthEntry.grid(row=4, column=1, pady=10)
yearEntry.grid(row=4, column=2, pady=10)

Button(text="Calculate", command= calculateAge).grid(row=6, column=1, pady=10)
    
root.mainloop()
