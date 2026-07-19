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
    v = [0.0] * (4)
    v[0] = -x[0]
    v[1] = v[0] - x[1]
    v[0] = _cm_exp(v[1])
    v[1] = x[0] * x[0]
    v[2] = 2. * v[1]
    v[1] = x[1] * x[1]
    v[3] = 3. * v[1]
    v[1] = v[2] + v[3]
    v[2] = v[0] * v[1]
    f = v[2]
    return f


xmin = [-75, -75]
xmax = [75, 75]
x0 = [0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "himmelbg.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
