'''
Functions :
Functions are a collection or a block of statements with specific
name or identity.
The statement block is defined to acheve a specific task.
Using functions in programs can reduce the complexity and
size of the code.
In python , the python library provides several built-in functions
such as print() , input() , round() etc.
User can define custom functions and use it for their projects
or programs
Functions are defined in python using a keyword "def" followed
by the function name , parameter and the code.

Syntax:
def <function-name>(<parameters..>,...):
    statement
    statement
    ........
Example:
      A function to draw a horizontal line on the console window

'''

def horiz_line(): #function defnition
    print('-' * 100)

horiz_line() #function call
print("Welcome to Manorama Horizon..")
horiz_line() #function call multiple times
print("From Malayala Manorama group...")
horiz_line()
print("Learn Python online...")
horiz_line()


