import bam
import math

import math as _math
_INF = float('inf')
_NAN = float('nan')
def _cm_sqrt(a):
    if a < 0.0:
        return _NAN
    return _math.sqrt(a)

def objective(x):
    f = 0.0
    v = [0.0] * (3)
    v[0] = 7. * x[0]
    v[1] = math.sin(v[0])
    v[0] = v[1] * v[1]
    v[1] = 7. * x[1]
    v[2] = math.cos(v[1])
    v[1] = v[2] * v[2]
    v[2] = v[0] * v[1]
    v[0] = 30. * v[2]
    v[2] = x[0] - x[1]
    v[1] = v[2] * v[2]
    v[2] = 0.01 + v[1]
    v[1] = _cm_sqrt(v[2])
    v[2] = 100. * v[1]
    v[0] += v[2]
    v[2] = x[0] * x[0]
    v[1] = 0.01 + v[2]
    v[2] = _cm_sqrt(v[1])
    v[1] = 100. * v[2]
    v[0] += v[1]
    f = v[0]
    return f


xmin = [-10000, -10000]
xmax = [10000, 10000]
x0 = [0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "hairy.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
