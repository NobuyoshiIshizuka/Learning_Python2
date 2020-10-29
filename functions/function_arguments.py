def my_function(fname):
    print(fname + " Silva" )

my_function("José")
my_function("Tobias")
my_function("Linus")

print("****************************************************")

"""
Number of Arguments
By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments,
you have to call the function with 2 arguments, not more, and not less.
"""
#This function expects 2 arguments, and gets 2 arguments:
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Roberto", "Santoro")