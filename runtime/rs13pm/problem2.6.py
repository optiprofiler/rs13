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
    x4 = 0.0
    t1 = 0.0
    t2 = 0.0
    base = 0.0
    expr1 = 0.0
    expr2 = 0.0
    expr3 = 0.0
    expr4 = 0.0
    y = 0.0
    objvar = 0.0
    x1 = xin[_post(_v, 'bam_idx', 1)]
    x2 = xin[_post(_v, 'bam_idx', 1)]
    x3 = xin[_post(_v, 'bam_idx', 1)]
    x4 = xin[_post(_v, 'bam_idx', 1)]
    t1 = _cm_pow((x4 + 1.0e0), 4)
    t2 = _cm_pow((x1 - t1), 4)
    base = _cm_pow((x1 - t1), 2) + _cm_pow((x2 - t2), 2) + 2.0e0 * (_cm_pow(x3, 2)) + x4 * x4 - 5.0e0 * (x1 - t1) - 5.0e0 * (x2 - t2) - 21.0e0 * x3 + 7.0e0 * x4
    expr1 = base
    expr2 = base + 10.0e0 * (_cm_pow((x1 - t1), 2) + _cm_pow((x2 - t2), 2) + x3 * x3 + x4 * x4 + x1 - t1 - (x2 - t2) + x3 - x4 - 8.0e0)
    expr3 = base + 10.0e0 * (_cm_pow((x1 - t1), 2) + 2.0e0 * (_cm_pow((x2 - t2), 2)) + x3 * x3 + 2.0e0 * (_cm_pow(x4, 2)) - (x1 - t1) - x4 - 10.0e0)
    expr4 = base + 10.0e0 * (_cm_pow((x1 - t1), 2) + _cm_pow((x2 - t2), 2) + x3 * x3 + 2.0e0 * (x1 - t1) - (x2 - t2) - x4 - 5.0e0)
    y = expr1
    if expr2 > y:
        y = expr2
    if expr3 > y:
        y = expr3
    if expr4 > y:
        y = expr4
    objvar = y
    fout = objvar
    return fout


xmin = [-1000, -1000, -1000, -1000]
xmax = [1000, 1000, 1000, 1000]
x0 = [0, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "problem2.6.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
