
from ctypes import alignment
from tkinter import*
from PIL import Image,ImageTk # to deal jpg file in python
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Sign up page")  
        self.root.geometry("1500x1000")
        
        self.root.config(bg="#1FC2CC")   
        
        img=Image.open(r"C:\Users\ASUS\.spyder-py3\signup\images\file1.jpg")
        img=img.resize((150,50),Image.ANTIALIAS)
        
        
        self.up=ImageTk.PhotoImage(img)
        up=Label(self.root,image=self.up,bg="white").place(x=0,y=0,width=150,height=50)  
        
        frame2=Frame(self.root,bg="white")
        frame2.place(x=150,y=0,width=1400,height=50)
        
        hbtn=Button(frame2, text="HOME",bg="white",fg="blue" ,bd=0,activeforeground="white",activebackground="white",relief=RAISED,font="arial 12 bold")
        hbtn.place(x=650,y=0,width=50,height=20)
        
        hbtn=Button(frame2, text="SEMINAR",bg="white",fg="blue" ,bd=0,activeforeground="white",activebackground="white",relief=RAISED,font="arial 12 bold")
        hbtn.place(x=800,y=0,width=90,height=20)
        
        hbtn=Button(frame2, text="INFORMATION",bg="white",fg="blue" ,bd=0,activeforeground="white",activebackground="white",relief=RAISED,font="arial 12 bold")
        hbtn.place(x=790,y=30,width=120,height=20)
        
        dbtn=Button(frame2, text="DASHBOARD",bg="white",fg="blue" ,bd=0,activeforeground="white",activebackground="white",relief=RAISED,font="arial 12 bold")
        dbtn.place(x=1000,y=0,width=120,height=20)
        
        
        frame1=Frame(self.root,bg="#1FC2CC")
        frame1.place(x=0,y=50,width=800,height=950)
        title=Label(frame1,text="SIGN UP FORM",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=400,y=50)
        
        img1=Image.open(r"C:\Users\ASUS\.spyder-py3\signup\images\side.jpg")
        img1=img1.resize((700,950),Image.ANTIALIAS)
        
        self.right=ImageTk.PhotoImage(img1)
        right=Label(self.root,image=self.right).place(x=950,y=50,width=700,height=900)
        
        name=Label(frame1,text="Name",font=("times new roman",18,"bold"),bg="#1FC2CC",fg="black").place(x=100,y=100)
       
        txt_fname=Entry(frame1,font=("times new roman",18),bg="white").place(x=290,y=100,width=1000)
        
        gender=Label(frame1,text="Gender",font=("times new roman",18,"bold"),bg="#1FC2CC",fg="black").place(x=100,y=150)
        var1 = IntVar()
        radiobtn1=Radiobutton(frame1,text="Male",variable =var1,value=1,font=("times new roman",15,"bold"),fg="black").place(x=290,y=150)
        radiobtn2=Radiobutton(frame1,text="Female",variable =var1,value=2,font=("times new roman",15,"bold"),fg="black").place(x=490,y=150)
        
        #radio button frame2
        
        frame3=Frame(self.root,bg="#1FC2CC")
        frame3.place(x=0,y=250,width=700,height=40)
        var2 = IntVar()
        ms=Label(frame3,text="Marital Status",font=("times new roman",18,"bold"),bg="#1FC2CC",fg="black").place(x=100,y=5)
        radiobtn3=Radiobutton(frame3,text="Married",variable =var2,value="rad3",font=("times new roman",15,"bold"),fg="black").place(x=290,y=5)
        radiobtn4=Radiobutton(frame3,text="Unmarried",variable =var2,value="rad4",font=("times new roman",15,"bold"),fg="black").place(x=490,y=5)
        
        email=Label(frame1,text="Email Id",font=("times new roman",18,"bold"),bg="#1FC2CC",fg="black").place(x=100,y=260)
        txt_email=Entry(frame1,font=("times new roman",18),bg="white").place(x=290,y=260,width=1000) 
        
        adress=Label(frame1,text="Address",font=("times new roman",18,"bold"),bg="#1FC2CC",fg="black").place(x=100,y=310)
        txt_adress=Entry(frame1,font=("times new roman",18,),bg="white").place(x=290,y=310,width=1000)
        
        organization=Label(frame1,text="Organization",font=("times new roman",18,"bold"),bg="#1FC2CC",fg="black").place(x=100,y=360)
        txt_org=Entry(frame1,font=("times new roman",18,),bg="white").place(x=290,y=360,width=1000)
        
        designation=Label(frame1,text="Designation",font=("times new roman",18,"bold"),bg="#1FC2CC",fg="black").place(x=100,y=410)
        txt_desg=Entry(frame1,font=("times new roman",18,),bg="white").place(x=290,y=410,width=1000)
        
        dob=Label(frame1,text="DOB",font=("times new roman",18,"bold"),bg="#1FC2CC",fg="black").place(x=100,y=460)
        txt_dob=Entry(frame1,font=("times new roman",18,),bg="white").place(x=290,y=460,width=1000)
        
        mobile_no=Label(frame1,text="Mobile No.",font=("times new roman",18,"bold"),bg="#1FC2CC",fg="black").place(x=100,y=510)
        txt_mobile_no=Entry(frame1,font=("times new roman",18,),bg="white").place(x=290,y=510,width=1000)
    
    
        img_button=Button(frame1,text="Take Image",font=("times new roman",18,"bold"),bd=0,bg="white",fg="black").place(x=290,y=560)
        
        sub_button=Button(frame1,text="Submit",font=("times new roman",18,"bold"),bd=0,bg="white",fg="blue").place(x=590,y=560)
        
  #self.bg is obj of class
        
  
root=Tk()
obj=Register(root)

root.mainloop()
