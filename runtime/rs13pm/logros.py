import bam

import math as _math
_INF = float('inf')
_NAN = float('nan')
def _cm_log(a):
    if a < 0.0:
        return _NAN
    if a == 0.0:
        return -_INF
    return _math.log(a)

def objective(x):
    f = 0.0
    v = [0.0] * (3)
    v[0] = x[0] * x[0]
    v[1] = x[1] - v[0]
    v[0] = v[1] * v[1]
    v[1] = 10000. * v[0]
    v[1] += 1.
    v[0] = 1. - x[0]
    v[2] = v[0] * v[0]
    v[1] += v[2]
    v[2] = _cm_log(v[1])
    f = v[2]
    return f


xmin = [0, 0]
xmax = [10000, 10000]
x0 = [5000, 5000]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "logros.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
