# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 22:37:23 2024

@author: saras
"""

'''
Program to read an existing text file , and print the contents. 
the file name must be accepted from the console
'''
try:
    fname=input("Enter the file to be read:")

    fp =open(fname,"r")

    text = fp.read()

    print(text)
    fp.close()

except FileNotFoundError:
    print("Invalid path for the file.")
