x = lambda a : a + 10
print(x(5))

#Lambda functions can take any number of arguments:

j = lambda a, b : a * b
print("This second function: ", j(5, 6))

n = lambda a, b, c : a +  b + c
print("Three arguments: ", n(5, 3, 2))

#Use that function definition to make a function that always doubles the number you send in:
def minha_funcao(n):
    return lambda a : a * n

mydoubler = minha_funcao(2)

print("Result minha_funcao: ", mydoubler(11))