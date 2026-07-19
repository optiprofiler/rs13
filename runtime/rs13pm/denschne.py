import bam

import math as _math
_INF = float('inf')
_NAN = float('nan')
def _cm_exp(a):
    try:
        return _math.exp(a)
    except OverflowError:
        return _INF

def objective(x):
    f = 0.0
    v = [0.0] * (3)
    v[0] = x[0] * x[0]
    v[1] = x[1] * x[1]
    v[2] = x[1] + v[1]
    v[1] = v[2] * v[2]
    v[0] += v[1]
    v[1] = _cm_exp(x[2])
    v[2] = -1. + v[1]
    v[1] = v[2] * v[2]
    v[0] += v[1]
    f = v[0]
    return f


xmin = [-10000, -10000, -150]
xmax = [10000, 10000, 150]
x0 = [0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "denschne.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
