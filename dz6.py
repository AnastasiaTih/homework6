number = int(input('Введите целое число: '))
syst = int(input('Введите целевую систему счисления (2 или 8): '))
def f(number,syst):
    result = ''
    while number > 0:
        ost = number % syst
        result += str(ost)
        number //= syst
    return result[::-1]
print(f(number,syst))