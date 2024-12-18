# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 11:26:07 2024

@author: saras
"""

'''Program to find the sum of all the command line arguments,
ignore all the non-numeric values while finding the sum
'''
import sys

total =0

for i in range(1, len(sys.argv)):
    try:
        total = total + float(sys.argv[i])
    except ValueError:
        pass

print("Sum of all cmd-line arguments is :", round(total,2))
    
    