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
    x = [0.0] * (6 + 1)
    t = 0.0
    auxy = 0.0
    model = 0.0
    objvar = 0.0
    for j in range(1, (6) + 1):
        x[j] = xin[_post(_v, 'bam_idx', 1)]
    objvar = 0.0e0
    for j in range(1, (51) + 1):
        t = 0.1e0 * (j - 1)
        auxy = 0.5e0 * _cm_exp(-t) - _cm_exp(-2.0e0 * t) + 0.5e0 * _cm_exp(-3.0e0 * t) + 1.5e0 * _cm_exp(-1.5e0 * t) * math.sin(7.0e0 * t) + _cm_exp(-2.5e0 * t) * math.sin(5.0e0 * t)
        model = x[1] * _cm_exp(-x[2] * t) * math.cos(x[3] * t + x[4]) + x[5] * _cm_exp(-x[6] * t)
        objvar = objvar + math.fabs(model - auxy)
    fout = objvar
    return fout


xmin = [-5000, -20, -5000, -5000, -5000, -20]
xmax = [10000, 30, 10000, 10000, 10000, 30]
x0 = [0, 0, 0, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "problem3.15.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
