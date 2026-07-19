import bam

import math as _math
_INF = float('inf')
_NAN = float('nan')
def _cm_exp(a):
    try:
        return _math.exp(a)
    except OverflowError:
        return _INF

def objective(x):
    f = 0.0
    v = [0.0] * (3)
    rv = 0.0
    v[0] = 0.01 * x[0]
    v[1] = -0.03 + v[0]
    v[0] = v[1] * v[1]
    v[1] = x[0] - x[1]
    v[2] = 20. * v[1]
    v[1] = _cm_exp(v[2])
    v[2] = v[0] + v[1]
    rv = v[2] - x[0]
    rv += x[1]
    f = rv
    return f


xmin = [-5, -5]
xmax = [5, 5]
x0 = [0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "cliff.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
