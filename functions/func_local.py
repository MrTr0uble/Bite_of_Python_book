x = 50


def func(x):
    print('x =', x)
    x = 2
    print('замена локального x на', x)


func(x)
print('x по прежнему', x)
