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
    for j in range(1, (21) + 1):
        t = -1.0e0 + (j - 1) / 10.0e0
        num = x1 + x2 * t
        den = 1.0e0 + x3 * t + x4 * (t * t) + x5 * (t * t * t)
        if den == 0.e0:
            yj = 1.e300
        else:
            yj = math.fabs(num / den - _cm_exp(t))
        if yj > objvar:
            objvar = yj
    fout = objvar
    return fout


xmin = [-10000, -10000, -10000, -10000, -10000]
xmax = [10000, 10000, 10000, 10000, 10000]
x0 = [0, 0, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "problem2.14.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
