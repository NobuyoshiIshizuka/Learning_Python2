"""
Global variable in function
"""

def myfunc():
    global g  #  This is a global variable within the function
    g = "fantastic"
    print("show variable global in function: " + g)

myfunc()  #  Calling the function

print("showing the global variable outside the scope of the function: " + g)