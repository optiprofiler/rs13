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
    v[0] = _cm_pow(x[0], 6.)
    v[1] = _cm_pow(x[0], 4.)
    v[2] = -15. * v[1]
    v[0] += v[2]
    v[2] = x[0] * x[0]
    v[1] = 27. * v[2]
    v[0] += v[1]
    v[0] += 250.
    f = v[0]
    return f


xmin = [-5]
xmax = [5]
x0 = [0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "ex4_1_6.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
