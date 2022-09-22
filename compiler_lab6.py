# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 14:11:30 2021

@author: ASUS
"""

x=input().split()
print(x)
list1=[]
pos1=x.index("(")
pos2=x.index(")")
for item in range(len(x)):
    if x[item]=="(":
        #pos1=x.index("(")
        #pos2=x.index(")")
    
        for i in range(pos1,pos2+1):
            
            if x[i] == "+":
                #print(x[i])
                a=int(x[i-1])
                b=int(x[i+1])
               # print(a+b)
                list1.append(a+b)
                
            if x[i] == "*":
               #print(x[i])
               a=int(x[i-1])
               b=int(x[i+1])
               #print(a*b)
               list1.append(a*b)
               
             
            if x[i] == "/":
               #print(x[i])
               a=int(x[i-1])
               b=int(x[i+1])
               #print(a/b)
               list1.append(a/b)
               
            if x[i] == "-":
               #print(x[i])
               a=int(x[i-1])
               b=int(x[i+1])
              # print(a-b)
               list1.append(a-b)
#y=del x[pos1,pos2]
del x[pos1:]
           
print(list1[0])  
print(x)  
if x[-1]=="/":
    list1.append(int(int(x[-2])/list1[0]))
    print(list1[1])  
        
        
elif x[-1]=="*":
    list1.append(int(x[-2])*list1[0])
      
else:
    
    if x[1]=="+" and x[-1]=="+":
        int(x[0])+int(x[2])+list1[0]
    elif x[1]=="+" and x[-1]=="-":
        int(x[0])+int(x[2])-list1[0]
    elif x[1]=="-" and x[-1]=="+":
        int(x[0])-int(x[2])+list1[0]
    elif x[1]=="-" and x[-1]=="-":
    
        int(x[0])-int(x[2])-list1[0]
    
             
del x[-2:] 
print(x)    

if x[1]=="*":
    
    list1.append(int(x[0])*list1[1])
elif x[1]=="/":
    list1.append(int(x[0])/list1[1])
elif x[1]=="+":
    list1.append(int(x[0])+list1[1])
elif x[1]=="-":
    list1.append(int(x[0])-list1[1])
      
            
    
print(list1[-1])    

                            
                
"""   
                res = int(x[i-1]) + int x[i+1]
             
        #res=int(pos1[i+1])+int(pos2[i-1])
print(res)       
        
"""  