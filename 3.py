# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 17:35:59 2020

@author: user
"""

# Jegor Skorikov, 03.11, task3

# How much pay
pizza=12.90
tips=110%(12.90)
payment=round(pizza+tips,2)
print("Payment is",payment)

# How much has each one pay
pay=round(payment/3,2)
print("Each one must pay",pay)
