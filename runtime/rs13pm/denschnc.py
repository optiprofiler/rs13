import bam

import math as _math
_INF = float('inf')
_NAN = float('nan')
def _cm_exp(a):
    try:
        return _math.exp(a)
    except OverflowError:
        return _INF
def _cm_pow(a, b):
    try:
        return _math.pow(a, b)
    except OverflowError:
        return _INF
    except ValueError:
        return _NAN

def objective(x):
    f = 0.0
    v = [0.0] * (3)
    v[0] = x[0] * x[0]
    v[0] += -2.
    v[1] = x[1] * x[1]
    v[0] += v[1]
    v[1] = v[0] * v[0]
    v[0] = -1. + x[0]
    v[2] = _cm_exp(v[0])
    v[2] += -2.
    v[0] = _cm_pow(x[1], 3.)
    v[2] += v[0]
    v[0] = v[2] * v[2]
    v[2] = v[1] + v[0]
    f = v[2]
    return f


xmin = [-150, -10000]
xmax = [150, 10000]
x0 = [0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "denschnc.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
