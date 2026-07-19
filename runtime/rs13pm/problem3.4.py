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

def _post(_v, _name, _delta):
    _old = _v.get(_name, 0)
    _v[_name] = _old + _delta
    return _old

def objective(xin):
    fout = 0.0
    _v = {}
    bam_idx = 0
    x1 = 0.0
    x2 = 0.0
    y1 = 0.0
    y2 = 0.0
    y3 = 0.0
    objvar = 0.0
    x1 = xin[_post(_v, 'bam_idx', 1)]
    x2 = xin[_post(_v, 'bam_idx', 1)]
    y1 = _cm_pow(x1, 4) + x2 * x2
    y2 = _cm_pow((2.0e0 - x1), 2) + _cm_pow((2.0e0 - x2), 2)
    y3 = 2.0e0 * _cm_exp(-x1 + x2)
    objvar = y1
    if y2 > objvar:
        objvar = y2
    if y3 > objvar:
        objvar = y3
    fout = objvar
    return fout


xmin = [-50, -50]
xmax = [50, 50]
x0 = [0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "problem3.4.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
