# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 20:16:19 2022

@author: ASUS
"""

from tkinter import*


root= Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")


Label(root,text="SIGN UP FORM", font="arial 16 bold").grid(row=0,column=3) 
name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")

name.grid(row="1",column="3")
phone.grid(row="2",column="3")
gender.grid(row="3",column="3")

namevalue=StringVar
phonevalue=StringVar
gendervalue=StringVar
checkvalue=IntVar

nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)



nameentry.grid(row=1,column=4)
phoneentry.grid(row=2,column=4)
genderentry.grid(row=3,column=4)

checkbtn=Checkbutton(text="remember me?",variable=checkvalue)
checkbtn.grid(row=4,column=4)

Button(text="Submit", command=getvals).grid(row=5,column=4)

root.mainloop()