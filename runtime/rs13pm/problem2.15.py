import bam
import math

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
def _cm_sqrt(a):
    if a < 0.0:
        return _NAN
    return _math.sqrt(a)

def _post(_v, _name, _delta):
    _old = _v.get(_name, 0)
    _v[_name] = _old + _delta
    return _old

def objective(xin):
    fout = 0.0
    _v = {}
    bam_idx = 0
    j = 0.0
    x1 = 0.0
    x2 = 0.0
    x3 = 0.0
    x4 = 0.0
    x5 = 0.0
    t = 0.0
    a = 0.0
    num = 0.0
    den = 0.0
    yj = 0.0
    objvar = 0.0
    x1 = xin[_post(_v, 'bam_idx', 1)]
    x2 = xin[_post(_v, 'bam_idx', 1)]
    x3 = xin[_post(_v, 'bam_idx', 1)]
    x4 = xin[_post(_v, 'bam_idx', 1)]
    x5 = xin[_post(_v, 'bam_idx', 1)]
    objvar = -1.0e300
    for j in range(1, (30) + 1):
        t = -1.0e0 + 2.0e0 * (j - 1) / 29.0e0
        a = _cm_sqrt(_cm_pow((8.0e0 * t - 1.0e0), 2) + 1.0e0) * math.atan(8.0e0 * t) / (8.0e0 * t)
        num = x1 + x2 * t + x3 * (t * t)
        den = 1.0e0 + x4 * t + x5 * (t * t)
        if den == 0.e0:
            yj = 1.e300
        else:
            yj = math.fabs(num / den - a)
        if yj > objvar:
            objvar = yj
    fout = objvar
    return fout


xmin = [-10000, -10000, -10000, -10000, -10000]
xmax = [10000, 10000, 10000, 10000, 10000]
x0 = [0, 0, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "problem2.15.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
