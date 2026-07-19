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
    x6 = 0.0
    t = 0.0
    a = 0.0
    yj = 0.0
    objvar = 0.0
    term1 = 0.0
    term2 = 0.0
    x1 = xin[_post(_v, 'bam_idx', 1)]
    x2 = xin[_post(_v, 'bam_idx', 1)]
    x3 = xin[_post(_v, 'bam_idx', 1)]
    x4 = xin[_post(_v, 'bam_idx', 1)]
    x5 = xin[_post(_v, 'bam_idx', 1)]
    x6 = xin[_post(_v, 'bam_idx', 1)]
    objvar = -1.0e300
    for j in range(1, (51) + 1):
        t = 0.1e0 * (j - 1)
        a = 0.5e0 * _cm_exp(-t) - _cm_exp(-2.0e0 * t) + 0.5e0 * _cm_exp(-3.0e0 * t) + 1.5e0 * _cm_exp(-1.5e0 * t) * math.sin(7.0e0 * t) + _cm_exp(-2.5e0 * t) * math.sin(5.0e0 * t)
        term1 = x1 * _cm_exp(-x2 * t) * math.cos(x3 * t + x4)
        term2 = x5 * _cm_exp(-x6 * t)
        yj = math.fabs(term1 + term2 - a)
        if yj > objvar:
            objvar = yj
    fout = objvar
    return fout


xmin = [-10000, -25, -10000, -10000, -10000, -25]
xmax = [10000, 25, 10000, 10000, 10000, 25]
x0 = [0, 0, 0, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "problem2.16.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
