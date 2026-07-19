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
    v[0] = x[0] * x[0]
    v[1] = 2. * v[0]
    v[0] = _cm_pow(x[0], 4.)
    v[2] = -1.05 * v[0]
    v[1] += v[2]
    v[2] = _cm_pow(x[0], 6.)
    v[0] = 0.166666666666667 * v[2]
    v[1] += v[0]
    v[0] = x[0] * x[1]
    v[2] = -v[0]
    v[1] += v[2]
    v[2] = x[1] * x[1]
    v[1] += v[2]
    f = v[1]
    return f


xmin = [-5, -10000]
xmax = [10000, 5]
x0 = [4997.5, -4997.5]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "ex4_1_5.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
