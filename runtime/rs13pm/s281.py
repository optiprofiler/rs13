import bam

import math as _math
_INF = float('inf')
_NAN = float('nan')
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
    v[0] = -1. + x[0]
    v[1] = v[0] * v[0]
    v[0] = -1. + x[1]
    v[2] = v[0] * v[0]
    v[0] = 8. * v[2]
    v[1] += v[0]
    v[0] = -1. + x[2]
    v[2] = v[0] * v[0]
    v[0] = 27. * v[2]
    v[1] += v[0]
    v[0] = -1. + x[3]
    v[2] = v[0] * v[0]
    v[0] = 64. * v[2]
    v[1] += v[0]
    v[0] = -1. + x[4]
    v[2] = v[0] * v[0]
    v[0] = 125. * v[2]
    v[1] += v[0]
    v[0] = -1. + x[5]
    v[2] = v[0] * v[0]
    v[0] = 216. * v[2]
    v[1] += v[0]
    v[0] = -1. + x[6]
    v[2] = v[0] * v[0]
    v[0] = 343. * v[2]
    v[1] += v[0]
    v[0] = -1. + x[7]
    v[2] = v[0] * v[0]
    v[0] = 512. * v[2]
    v[1] += v[0]
    v[0] = -1. + x[8]
    v[2] = v[0] * v[0]
    v[0] = 729. * v[2]
    v[1] += v[0]
    v[0] = -1. + x[9]
    v[2] = v[0] * v[0]
    v[0] = 1000. * v[2]
    v[1] += v[0]
    v[0] = _cm_pow(v[1], 0.3333333333333333)
    f = v[0]
    return f


xmin = [-10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000]
xmax = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
x0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "s281.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
