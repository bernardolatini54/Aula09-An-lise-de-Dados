def dobro(x):
    r = x * 2
    return r


def triplo(y):
    r = y * 3
    return r


def quadrado(q):
    r = q **2
    return r



num = float(input('Informe um número: '))
resultado = dobro(num)
print(resultado)



num2 = float(input('informe um número: '))
resultado2 = triplo(num2)
print(resultado2)



num3 = float(input('Informe um número: '))
resultado3 = quadrado(num3)
print(resultado3)