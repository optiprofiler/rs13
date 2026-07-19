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
    j = 0.0
    x = [0.0] * (11 + 1)
    y = 0.0
    objvar = 0.0
    arg = 0.0
    for j in range(1, (11) + 1):
        x[j] = xin[_post(_v, 'bam_idx', 1)]
    objvar = -1.e300
    for i in range(1, (10) + 1):
        y = 0.0e0
        for j in range(0, (10) + 1):
            arg = (i - 1 + 2 * j)
            y = y + _cm_exp(_cm_pow((x[j + 1] - math.sin(arg)), 2)) / (i + j)
        if y > objvar:
            objvar = y
    fout = objvar
    return fout


xmin = [-10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10]
xmax = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
x0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "problem2.23.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
