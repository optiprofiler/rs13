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
def _cm_sqrt(a):
    if a < 0.0:
        return _NAN
    return _math.sqrt(a)

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
    t = 0.0
    r = 0.0
    y1 = 0.0
    y2 = 0.0
    objvar = 0.0
    x1 = xin[_post(_v, 'bam_idx', 1)]
    x2 = xin[_post(_v, 'bam_idx', 1)]
    t = x1 * x1 + x2 * x2
    r = _cm_sqrt(t)
    y1 = _cm_pow((x1 - r * math.cos(r)), 2) + 0.005e0 * t
    y2 = _cm_pow((x2 - r * math.sin(r)), 2) + 0.005e0 * t
    objvar = y1
    if y2 > objvar:
        objvar = y2
    fout = objvar
    return fout


xmin = [-10000, -10000]
xmax = [10000, 10000]
x0 = [0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "problem2.3.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
