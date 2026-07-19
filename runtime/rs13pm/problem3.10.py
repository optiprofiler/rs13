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
    y1 = 0.0
    y2 = 0.0
    y3 = 0.0
    objvar = 0.0
    ax2 = 0.0
    x1 = xin[_post(_v, 'bam_idx', 1)]
    x2 = xin[_post(_v, 'bam_idx', 1)]
    ax2 = math.fabs(x2)
    y1 = 5.0e0 * _cm_sqrt(9.0e0 * x1 * x1 + 16.0e0 * x2 * x2)
    y2 = 9.0e0 * x1 + 16.0e0 * ax2
    y3 = 9.0e0 * x1 + 16.0e0 * ax2 - _cm_pow(x1, 9)
    if x1 >= ax2:
        objvar = y1
    else:
        if x1 > 0.0e0 and x1 < ax2:
            objvar = y2
        else:
            objvar = y3
    fout = objvar
    return fout


xmin = [-10000, -10000]
xmax = [10000, 10000]
x0 = [0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "problem3.10.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
