#было
size = int(input('Введите размерность массива: '))
massiv = []
for i in range(size):
     massiv.append(float(int(input('Введите число: '))))
     i += 1
print(massiv)
b = massiv.index(max(massiv))
for i in range(b+1, size):
    massiv[i]=0
print(massiv)

#стало
def f(size):
    massiv = []
    for i in range(size):
        massiv.append(float(int(input('Введите число: '))))
        i += 1
    return massiv
size = int(input('Введите размерность массива: '))
massiv = f(size)
print(massiv)
b = massiv.index(max(massiv))
for i in range(b+1, size):
    massiv[i]=0
print(massiv)