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
    x = [0.0] * (10 + 1)
    i = 0.0
    j = 0.0
    y1 = 0.0
    y2 = 0.0
    y3 = 0.0
    y4 = 0.0
    objvar = 0.0
    t1 = 0.0
    t2 = 0.0
    t = 0.0
    for i in range(1, (10) + 1):
        x[i] = xin[_post(_v, 'bam_idx', 1)]
    t1 = 0.0e0
    t2 = 0.0e0
    for i in range(1, (10) + 1):
        t = x[i] - 1.0e0
        t1 = t1 + t * t
        t2 = t2 + (x[i] * x[i] - 0.25e0)
    y1 = t1 + 1.0e-3 * t2
    y2 = x[1] * x[1] + _cm_pow((x[2] - x[1] * x[1] - 1), 2)
    for i in range(2, (30) + 1):
        t1 = 0.0e0
        t2 = x[1]
        for j in range(2, (10) + 1):
            t1 = t1 + x[j] * (j - 1) * _cm_pow(((i - 1) / 29), (j - 2))
            t2 = t2 + x[j] * _cm_pow(((i - 1) / 29), (j - 1))
        t2 = _cm_pow(t2, 2)
        y2 = y2 + _cm_pow((t1 - t2 - 1), 2)
    y3 = 0.0e0
    for i in range(2, (10) + 1):
        y3 = y3 + 100.0e0 * _cm_pow((x[i] - x[i - 1] * x[i - 1]), 2) + _cm_pow((1.0e0 - x[i]), 2)
    objvar = y1
    if y2 > objvar:
        objvar = y2
    if y3 > objvar:
        objvar = y3
    fout = objvar
    return fout


xmin = [-5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000, -5000]
xmax = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
x0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "problem3.17.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
