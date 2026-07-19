import bam

import math as _math
_INF = float('inf')
_NAN = float('nan')
def _cm_exp(a):
    try:
        return _math.exp(a)
    except OverflowError:
        return _INF
def _cm_pow(a, b):
    try:
        return _math.pow(a, b)
    except OverflowError:
        return _INF
    except ValueError:
        return _NAN

def objective(x):
    f = 0.0
    v = [0.0] * (4)
    rv = 0.0
    v[0] = x[0] * x[0]
    v[1] = -0.1269366345 * v[0]
    v[0] = _cm_pow(x[0], 3.)
    v[2] = 0.0020567665 * v[0]
    v[1] += v[2]
    v[2] = _cm_pow(x[0], 4.)
    v[0] = -1.0345e-05 * v[2]
    v[1] += v[0]
    v[0] = 0.0302344793 * x[0]
    v[2] = x[0] * x[0]
    v[3] = -0.0012813448 * v[2]
    v[0] += v[3]
    v[3] = _cm_pow(x[0], 3.)
    v[2] = 3.52599e-05 * v[3]
    v[0] += v[2]
    v[2] = _cm_pow(x[0], 4.)
    v[3] = -2.266e-07 * v[2]
    v[0] += v[3]
    v[3] = x[1] * v[0]
    v[0] = -v[3]
    v[1] += v[0]
    v[0] = x[1] * x[1]
    v[3] = -0.2564581253 * v[0]
    v[1] += v[3]
    v[3] = _cm_pow(x[1], 3.)
    v[0] = 0.003460403 * v[3]
    v[1] += v[0]
    v[0] = _cm_pow(x[1], 4.)
    v[3] = -1.35139e-05 * v[0]
    v[1] += v[3]
    v[3] = 1. + x[1]
    v[0] = -28.1064434908 / v[3]
    v[3] = -v[0]
    v[1] += v[3]
    v[3] = 0.0003405462 * x[0]
    v[0] = x[0] * x[0]
    v[2] = -5.2375e-06 * v[0]
    v[3] += v[2]
    v[2] = _cm_pow(x[0], 3.)
    v[0] = -6.3e-09 * v[2]
    v[3] += v[0]
    v[0] = x[1] * x[1]
    v[2] = v[3] * v[0]
    v[3] = -v[2]
    v[1] += v[3]
    v[3] = _cm_pow(x[0], 3.)
    v[2] = 7.e-10 * v[3]
    v[3] = -1.6638e-06 * x[0]
    v[0] = v[2] + v[3]
    v[2] = _cm_pow(x[1], 3.)
    v[3] = v[0] * v[2]
    v[0] = -v[3]
    v[1] += v[0]
    v[0] = 0.0005 * x[0]
    v[3] = v[0] * x[1]
    v[0] = _cm_exp(v[3])
    v[3] = 2.8673112392 * v[0]
    v[1] += v[3]
    v[1] += -75.1963666677
    rv = v[1] + 3.8112755343 * x[0]
    rv += 6.8306567613 * x[1]
    f = rv
    return f


xmin = [0, 0]
xmax = [95, 75]
x0 = [47.5, 37.5]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "himmelp1.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
