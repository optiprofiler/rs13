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
    v = [0.0] * (2)
    rv = 0.0
    v[0] = 1. + x[0]
    v[1] = _cm_pow(v[0], 3.)
    v[0] = 0.3333333333333333 * v[1]
    rv = v[0] + x[1]
    f = rv
    return f


xmin = [1, 0]
xmax = [10000, 10000]
x0 = [5000.5, 5000]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "hs004.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
