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
    j = 0.0
    x1 = 0.0
    x2 = 0.0
    x3 = 0.0
    x4 = 0.0
    x5 = 0.0
    x6 = 0.0
    x7 = 0.0
    x8 = 0.0
    x9 = 0.0
    t = [0.0] * (41 + 1)
    auxy = 0.0
    auxcos = 0.0
    auxsin = 0.0
    pi = 3.14159265358979324e0
    A1 = 0.0
    A2 = 0.0
    A3 = 0.0
    A4 = 0.0
    expr = 0.0
    yj = 0.0
    objvar = 0.0
    _init_t = [0.00e0,0.01e0,0.02e0,0.03e0,0.04e0,0.05e0,0.07e0,0.1e0,0.13e0,0.16e0,0.19e0,0.22e0,0.25e0,0.28e0,0.31e0,0.34e0,0.37e0,0.4e0,0.43e0,0.46e0,0.5e0,0.54e0,0.57e0,0.6e0,0.63e0,0.66e0,0.69e0,0.72e0,0.75e0,0.78e0,0.81e0,0.84e0,0.87e0,0.9e0,0.93e0,0.95e0,0.96e0,0.97e0,0.98e0,0.99e0,1.0e0]
    _k = 0.0
    for _k in range(0, 41):
        t[_k + 1] = _init_t[_k]
    x1 = xin[_post(_v, 'bam_idx', 1)]
    x2 = xin[_post(_v, 'bam_idx', 1)]
    x3 = xin[_post(_v, 'bam_idx', 1)]
    x4 = xin[_post(_v, 'bam_idx', 1)]
    x5 = xin[_post(_v, 'bam_idx', 1)]
    x6 = xin[_post(_v, 'bam_idx', 1)]
    x7 = xin[_post(_v, 'bam_idx', 1)]
    x8 = xin[_post(_v, 'bam_idx', 1)]
    x9 = xin[_post(_v, 'bam_idx', 1)]
    objvar = -1.0e300
    for j in range(1, (41) + 1):
        auxy = math.fabs(1.0e0 - 2.0e0 * t[j])
        auxcos = math.cos(pi * t[j])
        auxsin = math.sin(pi * t[j])
        A1 = _cm_pow((x1 + (1.0e0 + x2) * auxcos), 2) + _cm_pow(((1.0e0 - x2) * auxsin), 2)
        A2 = _cm_pow((x3 + (1.0e0 + x4) * auxcos), 2) + _cm_pow(((1.0e0 - x4) * auxsin), 2)
        A3 = _cm_pow((x5 + (1.0e0 + x6) * auxcos), 2) + _cm_pow(((1.0e0 - x6) * auxsin), 2)
        A4 = _cm_pow((x7 + (1.0e0 + x8) * auxcos), 2) + _cm_pow(((1.0e0 - x8) * auxsin), 2)
        if A2 == 0.e0 or A4 == 0.e0:
            yj = 1.e300
        else:
            expr = x9 * _cm_sqrt(A1 / A2) * _cm_sqrt(A3 / A4)
            yj = math.fabs(expr - auxy)
        if yj > objvar:
            objvar = yj
    fout = objvar
    return fout


xmin = [-10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000]
xmax = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
x0 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "problem2.18.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
