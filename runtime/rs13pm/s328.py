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
    v = [0.0] * (5)
    v[0] = x[0] * x[0]
    v[1] = 0.1 * v[0]
    v[0] = x[1] * x[1]
    v[2] = 1. + v[0]
    v[0] = x[0] * x[0]
    v[3] = v[2] / v[0]
    v[2] = 0.1 * v[3]
    v[1] += v[2]
    v[2] = x[0] * x[0]
    v[3] = x[1] * x[1]
    v[0] = v[2] * v[3]
    v[2] = 100. + v[0]
    v[0] = _cm_pow(x[0], 4.)
    v[3] = _cm_pow(x[1], 4.)
    v[4] = v[0] * v[3]
    v[0] = v[2] / v[4]
    v[2] = 0.1 * v[0]
    v[1] += v[2]
    v[1] += 1.2000000000000002
    f = v[1]
    return f


xmin = [1, 1]
xmax = [3, 3]
x0 = [2, 2]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "s328.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
