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
    v[0] = _cm_pow(x[0], 10.)
    v[1] = _cm_pow(x[1], 10.)
    v[0] += v[1]
    v[1] = _cm_pow(x[2], 10.)
    v[0] += v[1]
    v[1] = _cm_pow(x[3], 10.)
    v[0] += v[1]
    v[1] = _cm_pow(x[4], 10.)
    v[0] += v[1]
    f = v[0]
    return f


xmin = [-0.5, -0.5, -0.5, -0.5, -0.5]
xmax = [0.4, 0.4, 0.4, 0.4, 0.4]
x0 = [-0.05, -0.05, -0.05, -0.05, -0.05]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "schwefel.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
