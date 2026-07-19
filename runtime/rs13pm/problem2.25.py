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
    auxy = [0.0] * (65 + 1)
    t = 0.0
    model = 0.0
    yj = 0.0
    objvar = 0.0
    _init_auxy = [1.366e0,1.191e0,1.112e0,1.013e0,0.991e0,0.885e0,0.831e0,0.847e0,0.786e0,0.725e0,0.746e0,0.679e0,0.608e0,0.655e0,0.616e0,0.606e0,0.602e0,0.626e0,0.651e0,0.724e0,0.649e0,0.649e0,0.694e0,0.644e0,0.624e0,0.661e0,0.612e0,0.558e0,0.533e0,0.495e0,0.500e0,0.423e0,0.395e0,0.375e0,0.372e0,0.391e0,0.396e0,0.405e0,0.428e0,0.429e0,0.523e0,0.562e0,0.607e0,0.653e0,0.672e0,0.708e0,0.633e0,0.668e0,0.645e0,0.632e0,0.591e0,0.559e0,0.597e0,0.625e0,0.739e0,0.710e0,0.729e0,0.720e0,0.636e0,0.581e0,0.428e0,0.292e0,0.162e0,0.098e0,0.054e0]
    _k = 0.0
    for _k in range(0, 65):
        auxy[_k + 1] = _init_auxy[_k]
    for i in range(1, (11) + 1):
        x[i] = xin[_post(_v, 'bam_idx', 1)]
    objvar = -1.0e300
    for j in range(1, (65) + 1):
        t = 0.1e0 * (j - 1)
        model = x[1] * _cm_exp(-x[5] * t) + x[2] * _cm_exp(-x[6] * _cm_pow((t - x[9]), 2)) + x[3] * _cm_exp(-x[7] * _cm_pow((t - x[10]), 2)) + x[4] * _cm_exp(-x[8] * _cm_pow((t - x[11]), 2))
        yj = math.fabs(auxy[j] - model)
        if yj > objvar:
            objvar = yj
    fout = objvar
    return fout


xmin = [-10000, -10000, -10000, -10000, -25, -2, -2, -2, -2, -2, -2]
xmax = [10000, 10000, 10000, 10000, 25, 10, 10, 10, 10, 10, 10]
x0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "problem2.25.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
