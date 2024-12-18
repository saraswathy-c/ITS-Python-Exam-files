'''
Passing Parameters to functions :
Parameters are values passed to a function.  While calling the function
these parameter are used by the function for processing.
'''
def horiz_line(char,cnt): #function defnition with parameters
    print(char * cnt) #using parameters to print the line

horiz_line('=',50) #function call with custom parameters
print("Welcome to Manorama Horizon..")
horiz_line('*',80) #function call multiple times
print("From Malayala Manorama group...")
horiz_line('+',60)
print("Learn Python online...")
horiz_line('@',50)