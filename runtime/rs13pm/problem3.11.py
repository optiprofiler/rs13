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
    x = [0.0] * (4 + 1)
    y1 = 0.0
    y2 = 0.0
    y3 = 0.0
    y4 = 0.0
    c1 = 0.0
    c2 = 0.0
    c3 = 0.0
    c4 = 0.0
    objvar = 0.0
    i = 0.0
    for i in range(1, (4) + 1):
        x[i] = xin[_post(_v, 'bam_idx', 1)]
    y1 = _cm_pow(x[1], 2) + _cm_pow(x[2], 2) + 2.0e0 * _cm_pow(x[3], 2) + _cm_pow(x[4], 2) - 5.0e0 * x[1] - 5.0e0 * x[2] - 21.0e0 * x[3] + 7.0e0 * x[4]
    y2 = _cm_pow(x[1], 2) + _cm_pow(x[2], 2) + _cm_pow(x[3], 2) + _cm_pow(x[4], 2) + x[1] - x[2] + x[3] - x[4] - 8.0e0
    y3 = _cm_pow(x[1], 2) + 2.0e0 * _cm_pow(x[2], 2) + _cm_pow(x[3], 2) + 2.0e0 * _cm_pow(x[4], 2) - x[1] - x[4] - 10.0e0
    y4 = _cm_pow(x[1], 2) + _cm_pow(x[2], 2) + _cm_pow(x[3], 2) + 2.0e0 * x[1] - x[2] - x[4] - 5.0e0
    c1 = y1
    c2 = y1 + 10.0e0 * y2
    c3 = y1 + 10.0e0 * y3
    c4 = y1 + 10.0e0 * y4
    objvar = c1
    if c2 > objvar:
        objvar = c2
    if c3 > objvar:
        objvar = c3
    if c4 > objvar:
        objvar = c4
    fout = objvar
    return fout


xmin = [-10000, -10000, -10000, -10000]
xmax = [10000, 10000, 10000, 10000]
x0 = [0, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "problem3.11.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
