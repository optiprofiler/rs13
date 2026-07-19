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
    i = 0.0
    x = [0.0] * (10 + 1)
    e1 = 0.0
    e2 = 0.0
    y1 = 0.0
    y2 = 0.0
    objvar = 0.0
    for i in range(1, (10) + 1):
        x[i] = xin[_post(_v, 'bam_idx', 1)]
    e1 = 1.0e-7 * (_cm_pow(x[1], 2)) + _cm_pow((x[2] + 2.0e0), 2) + _cm_pow(x[3], 2) + 4.0e0 * (_cm_pow(x[4], 2)) + _cm_pow(x[5], 2) + _cm_pow(x[6], 2) + _cm_pow(x[7], 2) + _cm_pow(x[8], 2) + _cm_pow(x[9], 2) + _cm_pow(x[10], 2)
    y1 = _cm_exp(e1)
    e2 = 1.0e-7 * (_cm_pow(x[1], 2)) + _cm_pow((x[2] - 2.0e0), 2) + _cm_pow(x[3], 2) + 4.0e0 * (_cm_pow(x[4], 2)) + _cm_pow(x[5], 2) + _cm_pow(x[6], 2) + _cm_pow(x[7], 2) + _cm_pow(x[8], 2) + _cm_pow(x[9], 2) + _cm_pow(x[10], 2)
    y2 = _cm_exp(e2)
    if y1 > y2:
        objvar = y1
    else:
        objvar = y2
    fout = objvar
    return fout


xmin = [-10000, -4, -4, -4, -4, -4, -4, -4, -4, -4]
xmax = [10000, 4, 4, 4, 4, 4, 4, 4, 4, 4]
x0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "problem2.22.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
