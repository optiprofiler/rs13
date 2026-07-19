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
    rv = 0.0
    v[0] = _cm_pow(x[0], 4.)
    v[1] = 1.41 * v[0]
    v[0] = _cm_pow(x[0], 3.)
    v[2] = -12.76 * v[0]
    v[1] += v[2]
    v[2] = x[0] * x[0]
    v[0] = 39.91 * v[2]
    v[1] += v[0]
    v[0] = -3.9 + x[1]
    v[2] = v[0] * v[0]
    v[1] += v[2]
    v[1] += 24.37
    rv = v[1] - 51.93 * x[0]
    f = rv
    return f


xmin = [-10000, -10000]
xmax = [10000, 10000]
x0 = [0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "s309.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
