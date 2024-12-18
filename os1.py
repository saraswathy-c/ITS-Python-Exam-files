# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 19:43:37 2024

@author: saras
"""

import os

print("Current working directory: ", os.getcwd())
# os.rmdir("test1")
os.mkdir("test1")
os.rename("test1", "test")
print("List of all files and sub-directories in current directory: ", os.listdir("."))
print("Current directory symbol used by OS: ", os.path.curdir)
print("File size in Bytes :", os.path.getsize("os1.py"))
print("List of all files and sub-directories in the Parent directory (1 level up):")
for i in os.listdir(".."):
    print(i)
    
#Instead of loops, you could use 
print(os.listdir(".."))

print("Current (Absolute) path: ", os.getcwd())

relative_path = os.path.relpath("Alex", os.getcwd())
print("Relative path:", relative_path)

