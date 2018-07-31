import numpy as np

m, n, k = map(int, input().split())
a = np.random.randint(-100, 100, (m, n, k))

x_max = np.amax(a, axis=0)
y_max = np.amax(a, axis=1)
z_max = np.amax(a, axis=2)

x_min = np.amin(a, axis=0)
y_min = np.amin(a, axis=1)
z_min = np.amin(a, axis=2)

x_sum = np.sum(a, axis=0)
y_sum = np.sum(a, axis=1)
z_sum = np.sum(a, axis=2)
