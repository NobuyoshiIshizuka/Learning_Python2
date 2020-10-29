"""
The following example shows how to use a default parameter value.

If we call the function without argument, it uses the default value:
"""

def my_funcion(country = "Normay"):
    print("I am from " + country)

my_funcion("Sweden")
my_funcion()
my_funcion("Brazil")