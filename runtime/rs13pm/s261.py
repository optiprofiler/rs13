import bam
import math

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
    v[0] = _cm_exp(x[0])
    v[1] = v[0] - x[1]
    v[0] = _cm_pow(v[1], 4.)
    v[1] = x[1] - x[2]
    v[2] = _cm_pow(v[1], 6.)
    v[1] = 100. * v[2]
    v[0] += v[1]
    v[1] = x[2] - x[3]
    v[2] = math.tan(v[1])
    v[1] = _cm_pow(v[2], 4.)
    v[0] += v[1]
    v[1] = _cm_pow(x[0], 8.)
    v[0] += v[1]
    v[1] = -1. + x[3]
    v[2] = v[1] * v[1]
    v[0] += v[2]
    f = v[0]
    return f


xmin = [-40, -10000, -10000, -10000]
xmax = [40, 10000, 10000, 10000]
x0 = [0, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "s261.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
