from itertools import islice, count

import numpy as np

a = np.random.uniform(-10, 10, [10, 8])
inp = float(input())
b = abs(a - inp)
# print the smallest value
idx = np.unravel_index(np.argmin(b), a.shape)
print("{0:.2f}".format(a[idx]))

# print the 3 smallest value
flat = a.flatten()
flat_b = abs(flat - inp)
for i in islice(count(1), 3):
    idx = np.argmin(flat_b)
    print("{0:.2f}".format(flat[idx]))
    flat = np.delete(flat, idx)
    flat_b = np.delete(flat_b, idx)
