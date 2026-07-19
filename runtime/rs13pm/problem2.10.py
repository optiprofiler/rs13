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
def _cm_pow(a, b):
    try:
        return _math.pow(a, b)
    except OverflowError:
        return _INF
    except ValueError:
        return _NAN

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
    t = 0.0
    term1 = 0.0
    term2 = 0.0
    yj = 0.0
    objvar = 0.0
    x1 = xin[_post(_v, 'bam_idx', 1)]
    x2 = xin[_post(_v, 'bam_idx', 1)]
    x3 = xin[_post(_v, 'bam_idx', 1)]
    x4 = xin[_post(_v, 'bam_idx', 1)]
    objvar = -1.0e300
    for j in range(1, (20) + 1):
        t = 0.2e0 * (j)
        term1 = _cm_pow((x1 + x2 * t - _cm_exp(t)), 2)
        term2 = _cm_pow((x3 + x4 * math.sin(t) - math.cos(t)), 2)
        yj = math.fabs(term1 + term2)
        if yj > objvar:
            objvar = yj
    fout = objvar
    return fout


xmin = [-10000, -10000, -10000, -10000]
xmax = [10000, 10000, 10000, 10000]
x0 = [0, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "problem2.10.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
