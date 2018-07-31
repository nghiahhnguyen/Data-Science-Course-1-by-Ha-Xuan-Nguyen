import numpy as np

a = np.array([range(4), range(10, 14)])
b = np.array([2, -1, 1, 0])

print(a * b)
b1 = b * 100
print(b1)
b2 = b * 100.
print(b2)
print(b1 == b2)

arr = np.array(range(10))
print(arr < 3)
print(np.less(arr, 3))
condition = np.logical_or(arr < 3, arr > 8)
new_arr = np.where(condition, arr * 5, arr * -5)
print(new_arr)


def calcMag(c, d, _min=0.1):
    mag = (c ** 2 + d ** 2) ** 0.5
    output = np.where(mag > _min, mag, _min)
    return output


u = np.array([[4, 5, 0.01], [2, 3, 4]])
v = np.array([[2, 2, 0.03], [1, 1, 1]])

print(calcMag(u, v))
