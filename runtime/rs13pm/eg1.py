import bam
import math

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
    v[0] = x[0] * x[0]
    v[1] = x[1] * x[2]
    v[2] = _cm_pow(v[1], 4.)
    v[0] += v[2]
    v[2] = x[0] * x[2]
    v[0] += v[2]
    v[2] = x[0] + x[2]
    v[1] = math.sin(v[2])
    v[2] = x[1] * v[1]
    v[0] += v[2]
    rv = v[0] + x[1]
    f = rv
    return f


xmin = [-10000, -1, 1]
xmax = [10000, 1, 2]
x0 = [0, 0, 1.5]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "eg1.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
