import numpy as np

print(np.fv(0.02, 20*12, -100, -100))
print(np.pv(0.02, 20*12, -100, 586032.549))
print(np.npv(0.281,[-100, 823, 59, 55, 20]))
print(np.pmt(0.02/12, 20*12, 1000000))
print(np.ppmt(0.02/12, -100, 20*12, 1000000))
print(np.ipmt(0.02/12, 0.001, 20*12, 200000))
print(round(np.irr([-5, 10.5, 1, -8, 1]), 5))
print(np.mirr([-100, 823, 59, 55, 20], -100, -150))
print(np.nper(0.02, -1e7, 1e8))
print(np.rate(0.7, -1e8, 200000, 0))