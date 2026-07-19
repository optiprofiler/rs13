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
    x8 = 0.0
    x9 = 0.0
    x10 = 0.0
    base = 0.0
    e1 = 0.0
    e2 = 0.0
    e3 = 0.0
    e4 = 0.0
    e5 = 0.0
    e6 = 0.0
    e7 = 0.0
    e8 = 0.0
    e9 = 0.0
    objvar = 0.0
    x1 = xin[_post(_v, 'bam_idx', 1)]
    x2 = xin[_post(_v, 'bam_idx', 1)]
    x3 = xin[_post(_v, 'bam_idx', 1)]
    x4 = xin[_post(_v, 'bam_idx', 1)]
    x5 = xin[_post(_v, 'bam_idx', 1)]
    x6 = xin[_post(_v, 'bam_idx', 1)]
    x7 = xin[_post(_v, 'bam_idx', 1)]
    x8 = xin[_post(_v, 'bam_idx', 1)]
    x9 = xin[_post(_v, 'bam_idx', 1)]
    x10 = xin[_post(_v, 'bam_idx', 1)]
    base = x1 * x1 + x2 * x2 + x1 * x2 - 14.0e0 * x1 - 16.0e0 * x2 + _cm_pow((x3 - 10.0e0), 2) + 4.0e0 * _cm_pow((x4 - 5.0e0), 2) + _cm_pow((x5 - 3.0e0), 2) + 2.0e0 * _cm_pow((x6 - 1.0e0), 2) + 5.0e0 * (_cm_pow(x7, 2)) + 7.0e0 * _cm_pow((x8 - 11.0e0), 2) + 2.0e0 * _cm_pow((x9 - 10.0e0), 2) + _cm_pow((x10 - 7.0e0), 2) + 45.0e0
    e1 = base
    e2 = base + 10.0e0 * (3.0e0 * _cm_pow((x1 - 2.0e0), 2) + 4.0e0 * _cm_pow((x2 - 3.0e0), 2) + 2.0e0 * (_cm_pow(x3, 2)) - 7.0e0 * x4 - 120.0e0)
    e3 = base + 10.0e0 * (5.0e0 * (_cm_pow(x1, 2)) + 8.0e0 * x2 + _cm_pow((x3 - 6.0e0), 2) - 2.0e0 * x4 - 40.0e0)
    e4 = base + 10.0e0 * (0.5e0 * _cm_pow((x1 - 8.0e0), 2) + 2.0e0 * _cm_pow((x2 - 4.0e0), 2) + 3.0e0 * (_cm_pow(x5, 2)) - x6 - 30.0e0)
    e5 = base + 10.0e0 * ((_cm_pow(x1, 2)) + 2.0e0 * _cm_pow((x2 - 2.0e0), 2) - 2.0e0 * x1 * x2 + 14.0e0 * x5 - 6.0e0 * x6)
    e6 = base + 10.0e0 * (4.0e0 * x1 + 5.0e0 * x2 - 3.0e0 * x7 + 9.0e0 * x8 - 105.0e0)
    e7 = base + 10.0e0 * (10.0e0 * x1 - 8.0e0 * x2 - 17.0e0 * x7 + 2.0e0 * x8)
    e8 = base + 10.0e0 * (-3.0e0 * x1 + 6.0e0 * x2 + 12.0e0 * _cm_pow((x9 - 8.0e0), 2) - 7.0e0 * x10)
    e9 = base + 10.0e0 * (-8.0e0 * x1 + 2.0e0 * x2 + 5.0e0 * x9 - 2.0e0 * x10 - 12.0e0)
    objvar = e1
    if e2 > objvar:
        objvar = e2
    if e3 > objvar:
        objvar = e3
    if e4 > objvar:
        objvar = e4
    if e5 > objvar:
        objvar = e5
    if e6 > objvar:
        objvar = e6
    if e7 > objvar:
        objvar = e7
    if e8 > objvar:
        objvar = e8
    if e9 > objvar:
        objvar = e9
    fout = objvar
    return fout


xmin = [-10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000]
xmax = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
x0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "problem2.20.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
