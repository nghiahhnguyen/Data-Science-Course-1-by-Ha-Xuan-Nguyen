import random as rd


def func(x):
    return x ** 2 / (4 * x)


a = []
for i in range(100):
    x = rd.randint(1, 10)
    a.append(func(x))

print(a)
