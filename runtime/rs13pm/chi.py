import bam
import math

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
    v[0] = x[0] * x[0]
    v[1] = 1.5707963267948966 * x[0]
    v[2] = math.cos(v[1])
    v[1] = 10. * v[2]
    v[0] += v[1]
    v[1] = 15.707963267948966 * x[0]
    v[2] = math.sin(v[1])
    v[1] = 8. * v[2]
    v[0] += v[1]
    v[1] = -0.5 + x[1]
    v[2] = v[1] * v[1]
    v[1] = v[2] / 2.
    v[2] = -v[1]
    v[1] = _cm_exp(v[2])
    v[2] = -0.4472135954999579 * v[1]
    v[0] += v[2]
    v[0] += 11.
    rv = v[0] - 12. * x[0]
    f = rv
    return f


xmin = [-30, -10]
xmax = [30, 10]
x0 = [0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "chi.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
