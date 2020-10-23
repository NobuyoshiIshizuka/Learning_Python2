"""
FUNCTION RANGE()

If you need to iterate over number strings, the built-in range () function is the answer.
It generates arithmetic progressions:
"""
for i in range(5):
    print(i, end=',')

print()
print('************')

#Iterando de 1 até 5
for j in range(1,5+1):
    print(j, end=',')

print()
print('************')

#Iterando de 100 até 1 decrementenado 2 números
for n in range(100,1,-2):
    print(n, end=',',)

print('\n')


#Para iterar sobre os índices de uma sequência, combine range() e len() da seguinte forma:
a = ['Mary', 'Had', 'a', 'little', 'lamb']

for i in range(len(a)):
    print(i, a[i])