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
    x3 = 0.0
    y1 = 0.0
    y2 = 0.0
    y3 = 0.0
    y4 = 0.0
    y5 = 0.0
    y6 = 0.0
    objvar = 0.0
    x1 = xin[_post(_v, 'bam_idx', 1)]
    x2 = xin[_post(_v, 'bam_idx', 1)]
    x3 = xin[_post(_v, 'bam_idx', 1)]
    y1 = x1 * x1 + x2 * x2 + x3 * x3 - 1.0e0
    y2 = x1 * x1 + x2 * x2 + _cm_pow((x3 - 2.0e0), 2)
    y3 = x1 + x2 + x3 - 1.0e0
    y4 = x1 + x2 - x3 + 1.0e0
    y5 = 2.0e0 * (_cm_pow(x1, 3)) + 6.0e0 * (_cm_pow(x2, 2)) + 2.0e0 * _cm_pow((5.0e0 * x3 - x1 + 1.0e0), 2)
    y6 = x1 * x1 - 9.0e0 * x3
    objvar = y1
    if y2 > objvar:
        objvar = y2
    if y3 > objvar:
        objvar = y3
    if y4 > objvar:
        objvar = y4
    if y5 > objvar:
        objvar = y5
    if y6 > objvar:
        objvar = y6
    fout = objvar
    return fout


xmin = [-10000, -10000, -10000]
xmax = [10000, 10000, 10000]
x0 = [0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "problem2.4.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
