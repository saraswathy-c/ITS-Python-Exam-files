# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 11:35:16 2024

@author: saras
"""

import sys

try:
    a = int(sys.argv[1])
    b = 10/a
    print("b is ",b)
except ValueError:
    print("Enter valid data")
except ZeroDivisionError:
    print("Division by zero encountered")
except NameError:
    print("b not found!!")
except IndexError:
    print("Too few parameters!")
finally:
    print("Exit")