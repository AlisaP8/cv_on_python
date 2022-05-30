import random

a = int(input('Введиде начальную границу: '))
b = int(input('Введиде конечную границу: '))

# d = {c: random.randint(a, b+1) for c in range(a, b+1)}
d = {c: random.randint(a, b+1) for c in range(1, b+1)}
print(d)
