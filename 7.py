# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 17:53:14 2020

@author: user
"""

# Jegor Skorikov, 03.11, task7

print("Add straight number")
ten=int(input())
list=[]
 #Binary
while ten!=0:
    ten=int(ten)
    subten=int(ten/2)
    ostatok=ten-subten*2
    list.append(ostatok)
    ten=subten
print(list)
print("this is your number in binary")
list.clear()

# 16-ndary
print()
print() 

print("Add your number again")
six=int(input())
list=[]

while six!=0:
    six=int(six)
    subsix=int(six/16)
    ostatok2=six-subsix*16
    if ostatok2==10:
        ostatok2="A"
    elif ostatok2==11:
        ostatok2="B"
    elif ostatok2==12:
        ostatok2="C"
    elif ostatok2==13:
        ostatok2="D"
    elif ostatok2==14:
        ostatok2="E"
    elif ostatok2==15:
        ostatok2="F"
    list.append(ostatok2)
    six=subsix
subsix=int(six/16)
ostatok2=six-subsix*16
list.append(ostatok2)

print(list)
print("this is your number in 16-ndary")



    


