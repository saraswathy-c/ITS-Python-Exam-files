'''
Functions with return values : Functions can return a value
to the calling function , the value can be of any data type
supported by python.A keyword "return" followed by the
return value  or varible must be defined within the
function body.
Example: Program to find the factorial of a number
using a function
'''
def factorial(n): #function defnition
    fact=1
    for i in range(1,n+1):
        fact=fact*i #finding the factorial
    return fact #returns the value back
#main program
n=int(input("Number:"))
print("Factorial of {} is {}".format(n,factorial(n)))
