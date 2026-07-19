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
    v[0] = 10. * x[1]
    v[1] = x[0] + v[0]
    v[0] = v[1] * v[1]
    v[1] = x[2] - x[3]
    v[2] = v[1] * v[1]
    v[1] = 5. * v[2]
    v[0] += v[1]
    v[1] = -2. * x[2]
    v[2] = x[1] + v[1]
    v[1] = _cm_pow(v[2], 4.)
    v[0] += v[1]
    v[1] = x[0] - x[3]
    v[2] = _cm_pow(v[1], 4.)
    v[1] = 10. * v[2]
    v[0] += v[1]
    f = v[0]
    return f


xmin = [-4, -4, -4, -4]
xmax = [5, 5, 5, 5]
x0 = [0.5, 0.5, 0.5, 0.5]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "powell.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
