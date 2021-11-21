def printMax(a, b):
    if a > b:
        print(a, 'max')
    elif a == b:
        print(a, '=', b)
    else:
        print(b, 'max')


printMax(3, 4)  # Прямая передача значений

x = 5
y = 7

printMax(x, y)  # Передача переменных в качастве аргументов
