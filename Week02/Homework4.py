import random
from math import sqrt

a = []
for i in range(20):
    a.append(random.randint(1, 10))
print(a)
b = []
for i in range(1, 11):
    b.append(0)
for i in range(0, 15):
    b[a[i] - 1] += 1
for i in range(0, 10):
    print("{}: {}".format(i + 1, b[i]))
_max = 0
for x in a:
    _max = max(_max, x)
print("Max: {}".format(_max))
_min = 11
for x in a:
    _min = min(_min, x)
print("Min: {}".format(_min))
_sum = 0
for x in a:
    _sum += x
mean = _sum / len(a)
print("Mean: {}".format(mean))
variance = 0
for x in a:
    variance += x ** 2
variance /= len(a)
print("Variance: {}".format(variance))
standard_deviation = sqrt(variance)
print("Standard Deviation: {0:.2f}".format(standard_deviation))
vis = []
for i in range(10):
    vis.append(0)
print(set(a))
