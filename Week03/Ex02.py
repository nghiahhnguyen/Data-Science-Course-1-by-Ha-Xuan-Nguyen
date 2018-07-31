import numpy as np

N = int(input())
a = np.random.randint(0, 10, (N, N, N))
x_max = np.amax(a, axis=0)
y_max = np.amax(a, axis=1)
z_max = np.amax(a, axis=2)
x_min = np.amin(a, axis=0)
y_min = np.amin(a, axis=1)
z_min = np.amin(a, axis=2)
x_sum = a.sum(axis=0)
y_sum = a.sum(axis=1)
z_sum = a.sum(axis=2)
