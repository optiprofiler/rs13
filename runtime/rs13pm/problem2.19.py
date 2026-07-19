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
    x5 = 0.0
    x6 = 0.0
    x7 = 0.0
    base = 0.0
    expr1 = 0.0
    expr2 = 0.0
    expr3 = 0.0
    expr4 = 0.0
    objvar = 0.0
    x1 = xin[_post(_v, 'bam_idx', 1)]
    x2 = xin[_post(_v, 'bam_idx', 1)]
    x3 = xin[_post(_v, 'bam_idx', 1)]
    x4 = xin[_post(_v, 'bam_idx', 1)]
    x5 = xin[_post(_v, 'bam_idx', 1)]
    x6 = xin[_post(_v, 'bam_idx', 1)]
    x7 = xin[_post(_v, 'bam_idx', 1)]
    base = _cm_pow((x1 - 10.0e0), 2) + 5.0e0 * _cm_pow((x2 - 12.0e0), 2) + (_cm_pow(x3, 4)) + 3.0e0 * _cm_pow((x4 - 11.0e0), 2) + 10.0e0 * (_cm_pow(x5, 6)) + 7.0e0 * (_cm_pow(x6, 2)) + (_cm_pow(x7, 4)) - 4.0e0 * x6 * x7 - 10.0e0 * x6 - 8.0e0 * x7
    expr1 = base
    expr2 = base + 10.0e0 * (2.0e0 * (_cm_pow(x1, 2)) + 3.0e0 * (_cm_pow(x2, 4)) + x3 + 4.0e0 * (_cm_pow(x4, 2)) + 5.0e0 * x5 - 127.0e0)
    expr3 = base + 10.0e0 * (7.0e0 * x1 + 3.0e0 * x2 + 10.0e0 * (_cm_pow(x3, 2)) + x4 - x5 - 282.0e0)
    expr4 = base + 10.0e0 * (23.0e0 * x1 + (_cm_pow(x2, 2)) + 6.0e0 * (_cm_pow(x6, 2)) - 8.0e0 * x7 - 196.0e0)
    objvar = expr1
    if expr2 > objvar:
        objvar = expr2
    if expr3 > objvar:
        objvar = expr3
    if expr4 > objvar:
        objvar = expr4
    fout = objvar
    return fout


xmin = [-10000, -10000, -10000, -10000, -10000, -10000, -10000]
xmax = [10000, 10000, 10000, 10000, 10000, 10000, 10000]
x0 = [0, 0, 0, 0, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "problem2.19.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
