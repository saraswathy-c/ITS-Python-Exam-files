# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 23:10:31 2024

@author: saras
"""

'''
Program to read the name and marks of 3 subjects of the student data
stored in the student.dat file
calculate the total marks , result and remarks and print a consolidated
report.
result - if the student scroes less than 35 in any of the subjects
or less than 120 as total , then "Failed" , otherwise "Passed"
Remarks:
if the student is "Failed" , then no remarks, if student
is passed,
if total is equal or above 240 then "Outstanding"
if total less than 240 and equal or above 180 then "Excellent"
if total less than 180 and equal or above 150 then "Good"
if total less than 150 then "Average"
'''
fp =open("student.dat","r")
stud_list = fp.readlines()
fp.close()

print("Details read....")
for i in stud_list:
    print(i.strip())
print("\nStudents marks report\n")    
print("{:10},{:<10},{:<10},{:<10},{:<10},{:20},{:20}".format("Name","Math","Science","English","Total marks", "Result","Remarks" ))
print("*"*100)
    
for data in stud_list:
    name,m1,m2,m3 = data.split(",")
    m1 = int(m1)
    m2 =int(m2)
    m3 = int(m3)
    total = m1+m2+m3
    if total>=120 or m1>=35 or m2>=35 or m3>=35:
        result="Passed"
    else:
        result="Failed"
    if result =="Passed":
        if total>=240:
            remarks = "Outstanding"
        elif total>=180:
            remarks = "Excellent"
        elif total >=150:
            remarks = "Good"
        else:
            remarks = "Average"
    else:
        remarks = ""
    print("{:10},{:<10},{:<10},{:<10},{:<10},{:20},{:20}".format(name,m1,m2,m3,total,result,remarks ))
    

