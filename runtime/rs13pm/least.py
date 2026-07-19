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
    v[0] = -5. * x[2]
    v[1] = _cm_exp(v[0])
    v[0] = v[1] * x[1]
    v[1] = 127. - v[0]
    v[0] = v[1] - x[0]
    v[1] = v[0] * v[0]
    v[0] = -3. * x[2]
    v[2] = _cm_exp(v[0])
    v[0] = v[2] * x[1]
    v[2] = 151. - v[0]
    v[0] = v[2] - x[0]
    v[2] = v[0] * v[0]
    v[1] += v[2]
    v[2] = -x[2]
    v[0] = _cm_exp(v[2])
    v[2] = v[0] * x[1]
    v[0] = 379. - v[2]
    v[2] = v[0] - x[0]
    v[0] = v[2] * v[2]
    v[1] += v[0]
    v[0] = 5. * x[2]
    v[2] = _cm_exp(v[0])
    v[0] = v[2] * x[1]
    v[2] = 421. - v[0]
    v[0] = v[2] - x[0]
    v[2] = v[0] * v[0]
    v[1] += v[2]
    v[2] = 3. * x[2]
    v[0] = _cm_exp(v[2])
    v[2] = v[0] * x[1]
    v[0] = 460. - v[2]
    v[2] = v[0] - x[0]
    v[0] = v[2] * v[2]
    v[1] += v[0]
    v[0] = _cm_exp(x[2])
    v[2] = v[0] * x[1]
    v[0] = 426. - v[2]
    v[2] = v[0] - x[0]
    v[0] = v[2] * v[2]
    v[1] += v[0]
    f = v[1]
    return f


xmin = [-10000, -10000, -5]
xmax = [10000, 10000, 5]
x0 = [0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "least.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
