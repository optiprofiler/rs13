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
    v = [0.0] * (4)
    v[0] = x[0] * x[0]
    v[1] = x[1] * x[1]
    v[0] += v[1]
    v[1] = x[2] * x[2]
    v[0] += v[1]
    v[1] = -1. + v[0]
    v[0] = v[1] * v[1]
    v[1] = x[0] * x[0]
    v[2] = x[1] * x[1]
    v[1] += v[2]
    v[2] = -2. + x[2]
    v[3] = v[2] * v[2]
    v[1] += v[3]
    v[3] = -1. + v[1]
    v[1] = v[3] * v[3]
    v[0] += v[1]
    v[1] = x[0] + x[1]
    v[1] += x[2]
    v[3] = -1. + v[1]
    v[1] = v[3] * v[3]
    v[0] += v[1]
    v[1] = x[0] + x[1]
    v[3] = v[1] - x[2]
    v[1] = 1. + v[3]
    v[3] = v[1] * v[1]
    v[0] += v[3]
    v[3] = x[1] * x[1]
    v[1] = 3. * v[3]
    v[3] = _cm_pow(x[0], 3.)
    v[1] += v[3]
    v[3] = 5. * x[2]
    v[2] = v[3] - x[0]
    v[3] = 1. + v[2]
    v[2] = v[3] * v[3]
    v[1] += v[2]
    v[2] = -36. + v[1]
    v[1] = v[2] * v[2]
    v[0] += v[1]
    f = v[0]
    return f


xmin = [-10000, -10000, -10000]
xmax = [10000, 10000, 10000]
x0 = [0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "engval2.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
