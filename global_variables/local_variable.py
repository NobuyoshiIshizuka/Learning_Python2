"""
Local Variable in function x Global variable
"""
g = "awesome"  # This is global variable

def myfunc():
    g = "fantastic"  # This is local variable
    print("Python is " + g)

#  Show the result of the function
myfunc()

#  prints the global variable
print("Python is " + g)