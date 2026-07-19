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
    v[0] = 0.2 * x[2]
    v[1] = _cm_exp(v[0])
    v[0] = 0.2 * x[1]
    v[2] = _cm_exp(v[0])
    v[0] = x[0] * v[2]
    v[2] = v[1] - v[0]
    v[1] = 1.751 + v[2]
    v[2] = v[1] * v[1]
    v[1] = 0.3 * x[2]
    v[0] = _cm_exp(v[1])
    v[1] = 0.3 * x[1]
    v[3] = _cm_exp(v[1])
    v[1] = x[0] * v[3]
    v[3] = v[0] - v[1]
    v[0] = 1.561 + v[3]
    v[3] = v[0] * v[0]
    v[2] += v[3]
    v[3] = 0.4 * x[2]
    v[0] = _cm_exp(v[3])
    v[3] = 0.4 * x[1]
    v[1] = _cm_exp(v[3])
    v[3] = x[0] * v[1]
    v[1] = v[0] - v[3]
    v[0] = 1.391 + v[1]
    v[1] = v[0] * v[0]
    v[2] += v[1]
    v[1] = 0.5 * x[2]
    v[0] = _cm_exp(v[1])
    v[1] = 0.5 * x[1]
    v[3] = _cm_exp(v[1])
    v[1] = x[0] * v[3]
    v[3] = v[0] - v[1]
    v[0] = 1.239 + v[3]
    v[3] = v[0] * v[0]
    v[2] += v[3]
    v[3] = 0.6 * x[2]
    v[0] = _cm_exp(v[3])
    v[3] = 0.6 * x[1]
    v[1] = _cm_exp(v[3])
    v[3] = x[0] * v[1]
    v[1] = v[0] - v[3]
    v[0] = 1.103 + v[1]
    v[1] = v[0] * v[0]
    v[2] += v[1]
    v[1] = 0.7 * x[2]
    v[0] = _cm_exp(v[1])
    v[1] = 0.7 * x[1]
    v[3] = _cm_exp(v[1])
    v[1] = x[0] * v[3]
    v[3] = v[0] - v[1]
    v[0] = 0.981 + v[3]
    v[3] = v[0] * v[0]
    v[2] += v[3]
    v[3] = 0.75 * x[2]
    v[0] = _cm_exp(v[3])
    v[3] = 0.75 * x[1]
    v[1] = _cm_exp(v[3])
    v[3] = x[0] * v[1]
    v[1] = v[0] - v[3]
    v[0] = 0.925 + v[1]
    v[1] = v[0] * v[0]
    v[2] += v[1]
    v[1] = 0.8 * x[2]
    v[0] = _cm_exp(v[1])
    v[1] = 0.8 * x[1]
    v[3] = _cm_exp(v[1])
    v[1] = x[0] * v[3]
    v[3] = v[0] - v[1]
    v[0] = 0.8721 + v[3]
    v[3] = v[0] * v[0]
    v[2] += v[3]
    v[3] = 0.85 * x[2]
    v[0] = _cm_exp(v[3])
    v[3] = 0.85 * x[1]
    v[1] = _cm_exp(v[3])
    v[3] = x[0] * v[1]
    v[1] = v[0] - v[3]
    v[0] = 0.8221 + v[1]
    v[1] = v[0] * v[0]
    v[2] += v[1]
    v[1] = 0.9 * x[2]
    v[0] = _cm_exp(v[1])
    v[1] = 0.9 * x[1]
    v[3] = _cm_exp(v[1])
    v[1] = x[0] * v[3]
    v[3] = v[0] - v[1]
    v[0] = 0.7748 + v[3]
    v[3] = v[0] * v[0]
    v[2] += v[3]
    f = v[2]
    return f


xmin = [-10000, -150, -150]
xmax = [10000, 150, 150]
x0 = [0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "hatfldd.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
