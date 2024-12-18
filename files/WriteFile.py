# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 22:18:36 2024

@author: saras
"""
'''
Program to create a new text file and store a list of names of friends. Read names from the console; press blank lines to quit.

'''
fp =open("friends.dat","w")
print("Enter names of your friends..Press enter key to exit..")

while True:
    text = input()
    if not text.strip():
        break
    text = text + "\n"
    fp.write(text)

fp.close()
print("friends.dat has been saved.")