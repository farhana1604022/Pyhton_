# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 11:56:42 2021

@author: ASUS
"""

input = input("Enter your value: ")


stack = []

def push(c):
   stack.append(c)
   
def remove():
   stack.pop()
   
def error():
   print("syntax error")

input = input + "$"
length= len(input)
push('$')
push('E')
for i in input:
    
    if(i=='$' and stack[-1]=='$'):
        print('accepted')
        break
        
    elif( i ==stack[-1]):
        print("match of "+ i)
        remove()
    else:
        if(stack[-1]=='E' and (i=='i' or i=='(')):
            print("\nE-> Te")
            remove()
            push('A')
            push('T')
              
        elif( stack[-1]=='A' and i =='+'):
            print("\ne-> +Te")
            remove()
            push('A')
            push('T')
            push('+')
    
        elif(stack[-1]=='A' and (i==')' or i=='$')):
            print("\ne-> 0")
            remove()

        elif(stack[-1]=='T' and (i=='i' or i=='(')):
            print("\nT-> Ft")
            remove()
            push('B');
            push('F');
        elif(stack[-1]=='B' and (i=='+' or i==')' or i=='$')):
            print(stack)
            print("\nt-> 0")
            remove()
        elif(stack[-1]=='B' and (i=='*' )):
            print("\nt-> *Ft")
            remove()
            push('B');
            push('F');
            push('*');

        elif(stack[-1]=='F' and (i=='i' )): 
            print("\nF-> i")
            remove()
            push('i');

        elif(stack[-1]=='F' and i=='(' ):
            print("\nF-> (E)")
            remove()
            push(')');
            push('E');
            push('(');

        else:
            error();