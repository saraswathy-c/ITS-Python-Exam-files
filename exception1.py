# -*- coding: utf-8 -*-
# Program to find the volume of a box, length and breadth, height must be accepted from the console

import sys

try:
    volume = float(sys.argv[1]) * float(sys.argv[2]) * float(sys.argv[3]) 
    print("Volume = ", volume)
    
except ValueError:
    print("Non-numeric data entered!")
    
except IndexError:
    print("Too few arguments..!!")

