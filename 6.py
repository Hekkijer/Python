# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 17:50:28 2020

@author: user
"""

# Jegor Skorikov, 03.11, task6

print("Add time in minutes")
time=int(input())
hours=int(time/60)
print(hours)
minutes=time-hours*60
print(minutes)

print("it is",hours,"hours and",minutes,"minutes")