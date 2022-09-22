# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 11:07:05 2022

@author: ASUS
"""

from tkinter import*
class Regsiter:
    def __init__(self,root):
        self.root=root
        self.root.title("Sign up page")
        self.root.geometry("1350*700+0+0")

root=Tk()
obj=Register(root)
root.mainloop()