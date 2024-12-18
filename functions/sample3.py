'''
Default values for parameters : -
Default values can be assigned to parameters during a function
defnition. If parameters are not passed to functions during runtime,
system will use the default parameter values ; otherwise the runtime
parameter values will overwrite the default value.
'''
def horiz_line(char='-',cnt=100): #function defnition with parameters
    print(char * cnt) #us

horiz_line() #function call with no parameters
print("Welcome to Manorama Horizon..")
horiz_line('*') #function call only so the second will be
#default value
print("From Malayala Manorama group...")
horiz_line(cnt=60) #only second parameter, first parameter
#will be default
print("Learn Python online...")
horiz_line('@',50) #both default parameters will
#be overwritten by the passed parameters
