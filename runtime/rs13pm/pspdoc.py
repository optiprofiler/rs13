import bam

import math as _math
_INF = float('inf')
_NAN = float('nan')
def _cm_sqrt(a):
    if a < 0.0:
        return _NAN
    return _math.sqrt(a)

def objective(x):
    f = 0.0
    v = [0.0] * (4)
    v[0] = x[0] * x[0]
    v[0] += 1.
    v[1] = x[1] - x[2]
    v[2] = v[1] * v[1]
    v[0] += v[2]
    v[2] = _cm_sqrt(v[0])
    v[0] = x[1] * x[1]
    v[0] += 1.
    v[1] = x[2] - x[3]
    v[3] = v[1] * v[1]
    v[0] += v[3]
    v[3] = _cm_sqrt(v[0])
    v[0] = v[2] + v[3]
    f = v[0]
    return f


xmin = [-10000, -10000, -10000, -10000]
xmax = [-1, 10000, 10000, 10000]
x0 = [-5000.5, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "pspdoc.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
