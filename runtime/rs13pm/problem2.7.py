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

def _post(_v, _name, _delta):
    _old = _v.get(_name, 0)
    _v[_name] = _old + _delta
    return _old

def objective(xin):
    fout = 0.0
    _v = {}
    bam_idx = 0
    j = 0.0
    x1 = 0.0
    x2 = 0.0
    x3 = 0.0
    t = [0.0] * (21 + 1)
    a = [0.0] * (21 + 1)
    yj = 0.0
    objvar = 0.0
    val = 0.0
    x1 = xin[_post(_v, 'bam_idx', 1)]
    x2 = xin[_post(_v, 'bam_idx', 1)]
    x3 = xin[_post(_v, 'bam_idx', 1)]
    for j in range(1, (21) + 1):
        t[j] = 10.0e0 * (j - 1) / 20.0e0
    for j in range(1, (21) + 1):
        a[j] = (3.0e0 * _cm_exp(-t[j])) / 20.0e0 + (1.0e0 * _cm_exp(-5.0e0 * t[j])) / 52.0e0 - _cm_exp(-2.0e0 * t[j]) * (3.0e0 * math.sin(2.0e0 * t[j]) + 11.0e0 * math.cos(2.0e0 * t[j])) / 65.0e0
    if x2 == 0.e0:
        objvar = 1.0e300
    else:
        objvar = -1.0e300
        for j in range(1, (21) + 1):
            val = x3 * _cm_exp(-t[j] * x1) * math.sin(t[j] * x2) / x2 - a[j]
            yj = math.fabs(val)
            if yj > objvar:
                objvar = yj
    fout = objvar
    return fout


xmin = [-10, -10000, -10000]
xmax = [10, 10000, 10000]
x0 = [0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "problem2.7.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
