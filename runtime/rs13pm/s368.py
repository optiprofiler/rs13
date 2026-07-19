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
    v = [0.0] * (4)
    v[0] = _cm_pow(x[0], 3.)
    v[1] = _cm_pow(x[1], 3.)
    v[0] += v[1]
    v[1] = _cm_pow(x[2], 3.)
    v[0] += v[1]
    v[1] = _cm_pow(x[3], 3.)
    v[0] += v[1]
    v[1] = _cm_pow(x[4], 3.)
    v[0] += v[1]
    v[1] = _cm_pow(x[5], 3.)
    v[0] += v[1]
    v[1] = _cm_pow(x[6], 3.)
    v[0] += v[1]
    v[1] = _cm_pow(x[7], 3.)
    v[0] += v[1]
    v[1] = v[0] * v[0]
    v[0] = x[0] * x[0]
    v[2] = x[1] * x[1]
    v[0] += v[2]
    v[2] = x[2] * x[2]
    v[0] += v[2]
    v[2] = x[3] * x[3]
    v[0] += v[2]
    v[2] = x[4] * x[4]
    v[0] += v[2]
    v[2] = x[5] * x[5]
    v[0] += v[2]
    v[2] = x[6] * x[6]
    v[0] += v[2]
    v[2] = x[7] * x[7]
    v[0] += v[2]
    v[2] = _cm_pow(x[0], 4.)
    v[3] = _cm_pow(x[1], 4.)
    v[2] += v[3]
    v[3] = _cm_pow(x[2], 4.)
    v[2] += v[3]
    v[3] = _cm_pow(x[3], 4.)
    v[2] += v[3]
    v[3] = _cm_pow(x[4], 4.)
    v[2] += v[3]
    v[3] = _cm_pow(x[5], 4.)
    v[2] += v[3]
    v[3] = _cm_pow(x[6], 4.)
    v[2] += v[3]
    v[3] = _cm_pow(x[7], 4.)
    v[2] += v[3]
    v[3] = v[0] * v[2]
    v[0] = v[1] - v[3]
    f = v[0]
    return f


xmin = [0, 0, 0, 0, 0, 0, 0, 0]
xmax = [1, 1, 1, 1, 1, 1, 1, 1]
x0 = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "s368.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
