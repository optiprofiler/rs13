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
    v[0] = 4. * x[1]
    v[1] = -v[0]
    v[0] = _cm_exp(v[1])
    v[1] = x[0] * v[0]
    v[0] = 72.1 - v[1]
    v[1] = v[0] - x[2]
    v[0] = v[1] / 72.1
    v[1] = v[0] * v[0]
    v[0] = 5.75 * x[1]
    v[2] = -v[0]
    v[0] = _cm_exp(v[2])
    v[2] = x[0] * v[0]
    v[0] = 65.6 - v[2]
    v[2] = v[0] - x[2]
    v[0] = v[2] / 65.6
    v[2] = v[0] * v[0]
    v[1] += v[2]
    v[2] = 7.5 * x[1]
    v[0] = -v[2]
    v[2] = _cm_exp(v[0])
    v[0] = x[0] * v[2]
    v[2] = 55.9 - v[0]
    v[0] = v[2] - x[2]
    v[2] = v[0] / 55.9
    v[0] = v[2] * v[2]
    v[1] += v[0]
    v[0] = 24. * x[1]
    v[2] = -v[0]
    v[0] = _cm_exp(v[2])
    v[2] = x[0] * v[0]
    v[0] = 17.1 - v[2]
    v[2] = v[0] - x[2]
    v[0] = v[2] / 17.1
    v[2] = v[0] * v[0]
    v[1] += v[2]
    v[2] = 32. * x[1]
    v[0] = -v[2]
    v[2] = _cm_exp(v[0])
    v[0] = x[0] * v[2]
    v[2] = 9.8 - v[0]
    v[0] = v[2] - x[2]
    v[2] = v[0] / 9.8
    v[0] = v[2] * v[2]
    v[1] += v[0]
    v[0] = 48. * x[1]
    v[2] = -v[0]
    v[0] = _cm_exp(v[2])
    v[2] = x[0] * v[0]
    v[0] = 4.5 - v[2]
    v[2] = v[0] - x[2]
    v[0] = v[2] / 4.5
    v[2] = v[0] * v[0]
    v[1] += v[2]
    v[2] = 72. * x[1]
    v[0] = -v[2]
    v[2] = _cm_exp(v[0])
    v[0] = x[0] * v[2]
    v[2] = 1.3 - v[0]
    v[0] = v[2] - x[2]
    v[2] = v[0] / 1.3
    v[0] = v[2] * v[2]
    v[1] += v[0]
    v[0] = 96. * x[1]
    v[2] = -v[0]
    v[0] = _cm_exp(v[2])
    v[2] = x[0] * v[0]
    v[0] = 0.6 - v[2]
    v[2] = v[0] - x[2]
    v[0] = v[2] / 0.6
    v[2] = v[0] * v[0]
    v[1] += v[2]
    f = v[1]
    return f


xmin = [-10000, -1.5, -10000]
xmax = [10000, 1.5, 10000]
x0 = [0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "s333.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
