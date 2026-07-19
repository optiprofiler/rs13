import bam

import math as _math
_INF = float('inf')
_NAN = float('nan')
def _cm_sqrt(a):
    if a < 0.0:
        return _NAN
    return _math.sqrt(a)

def objective(x):
    f = 0.0
    v = [0.0] * (3)
    v[0] = -1. + x[0]
    v[1] = v[0] * v[0]
    v[0] = _cm_sqrt(x[1])
    v[2] = x[0] - v[0]
    v[0] = v[2] * v[2]
    v[1] += v[0]
    v[0] = _cm_sqrt(x[2])
    v[2] = x[1] - v[0]
    v[0] = v[2] * v[2]
    v[1] += v[0]
    v[0] = _cm_sqrt(x[3])
    v[2] = x[2] - v[0]
    v[0] = v[2] * v[2]
    v[1] += v[0]
    f = v[1]
    return f


xmin = [0, 0, 0, 0]
xmax = [10000, 10000, 10000, 10000]
x0 = [5000, 5000, 5000, 5000]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "hatflda.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
