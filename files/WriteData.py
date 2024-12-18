# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 22:46:05 2024

@author: saras
"""

'''
Program to accept the name and marks in 3 subjects
for a set of students , store them into a list and
save the data into a file
List: ['aaru,23,45,66\n', 'paru,56,67,54\n', 'deepu,78,65,43\n']
'''

stud_list =[]
while True:
    try:
        name = input("Enter your name:")
        m1 = int(input("What is your Math marks?"))
        if m1<0 or m1>100:
            raise ValueError
        m2 = int(input("What is your Science marks?"))
        if m2<0 or m2>100:
            raise ValueError
        m3 = int(input("What is your English marks?"))
        if m3<0 or m3>100:
            raise ValueError
        stud_list.append(name +"," + str(m1) +"," + str(m2) + "," + str(m3) +"\n")
    except ValueError:
        print("Pls enter valid integer marks...")
    ch = input("Any more data?..")
    if ch.upper()!="Y":
        break
    
print("List:", stud_list)
    
fp = open("student.dat","a")
fp.writelines(stud_list)
fp.close()
print("Student details added to the file.")