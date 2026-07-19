import bam
import math

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
    i = 0.0
    j = 0.0
    x = [0.0] * (20 + 1)
    yj = [0.0] * (29 + 1)
    y1 = 0.0
    y2 = 0.0
    objvar = 0.0
    t = 0.0
    s1 = 0.0
    s2 = 0.0
    for i in range(1, (20) + 1):
        x[i] = xin[_post(_v, 'bam_idx', 1)]
    for j in range(3, (31) + 1):
        t = (j - 2) / 29.0e0
        s1 = 0.0e0
        for i in range(1, (20) + 1):
            if i == 1:
                s1 = s1 + 0.0e0
            else:
                s1 = s1 + (i - 1) * x[i] * _cm_pow(t, (i - 2))
        s2 = 0.0e0
        for i in range(1, (20) + 1):
            s2 = s2 + x[i] * _cm_pow(t, (i - 1))
        yj[j - 2] = math.fabs(s1 - s2 * s2 - 1.0e0)
    y1 = math.fabs(x[1])
    y2 = math.fabs(x[2] - x[1] * x[1] - 1.0e0)
    objvar = y1
    if y2 > objvar:
        objvar = y2
    for j in range(1, (29) + 1):
        if yj[j] > objvar:
            objvar = yj[j]
    fout = objvar
    return fout


xmin = [-10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000]
xmax = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
x0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "problem2.24.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
