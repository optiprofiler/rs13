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
    i = 0.0
    x = [0.0] * (20 + 1)
    base = 0.0
    e = [0.0] * (18 + 1)
    objvar = 0.0
    for i in range(1, (20) + 1):
        x[i] = xin[_post(_v, 'bam_idx', 1)]
    base = _cm_pow(x[1], 2) + _cm_pow(x[2], 2) + x[1] * x[2] - 14.0e0 * x[1] - 16.0e0 * x[2] + _cm_pow((x[3] - 10.0e0), 2) + 4.0e0 * _cm_pow((x[4] - 5.0e0), 2) + _cm_pow((x[5] - 3.0e0), 2) + 2.0e0 * _cm_pow((x[6] - 1.0e0), 2) + 5.0e0 * (_cm_pow(x[7], 2)) + 7.0e0 * _cm_pow((x[8] - 11.0e0), 2) + 2.0e0 * _cm_pow((x[9] - 10.0e0), 2) + _cm_pow((x[10] - 7.0e0), 2) + _cm_pow((x[11] - 9.0e0), 2) + 10.0e0 * _cm_pow((x[12] - 1.0e0), 2) + 5.0e0 * _cm_pow((x[13] - 7.0e0), 2) + 4.0e0 * _cm_pow((x[14] - 14.0e0), 2) + 27.0e0 * _cm_pow((x[15] - 1.0e0), 2) + _cm_pow(x[16], 4) + _cm_pow((x[17] - 2.0e0), 2) + 13.0e0 * _cm_pow((x[18] - 2.0e0), 2) + _cm_pow((x[19] - 3.0e0), 2) + _cm_pow(x[20], 2) + 95.0e0
    e[1] = base
    e[2] = base + 10.0e0 * (3.0e0 * _cm_pow((x[1] - 2.0e0), 2) + 4.0e0 * _cm_pow((x[2] - 3.0e0), 2) + 2.0e0 * (_cm_pow(x[3], 2)) - 7.0e0 * x[4] - 120.0e0)
    e[3] = base + 10.0e0 * (5.0e0 * (_cm_pow(x[1], 2)) + 8.0e0 * x[2] + _cm_pow((x[3] - 6.0e0), 2) - 2.0e0 * x[4] - 40.0e0)
    e[4] = base + 10.0e0 * (0.5e0 * _cm_pow((x[1] - 8.0e0), 2) + 2.0e0 * _cm_pow((x[2] - 4.0e0), 2) + 3.0e0 * (_cm_pow(x[5], 2)) - x[6] - 30.0e0)
    e[5] = base + 10.0e0 * (_cm_pow(x[1], 2) + 2.0e0 * _cm_pow((x[2] - 2.0e0), 2) - 2.0e0 * x[1] * x[2] + 14.0e0 * x[5] - 6.0e0 * x[6])
    e[6] = base + 10.0e0 * (4.0e0 * x[1] + 5.0e0 * x[2] - 3.0e0 * x[7] + 9.0e0 * x[8] - 105.0e0)
    e[7] = base + 10.0e0 * (10.0e0 * x[1] - 8.0e0 * x[2] - 17.0e0 * x[7] + 2.0e0 * x[8])
    e[8] = base + 10.0e0 * (-3.0e0 * x[1] + 6.0e0 * x[2] + 12.0e0 * _cm_pow((x[9] - 8.0e0), 2) - 7.0e0 * x[10])
    e[9] = base + 10.0e0 * (-8.0e0 * x[1] + 2.0e0 * x[2] + 5.0e0 * x[9] - 2.0e0 * x[10] - 12.0e0)
    e[10] = base + 10.0e0 * (x[1] + x[2] + 4.0e0 * x[11] - 21.0e0 * x[12])
    e[11] = base + 10.0e0 * (_cm_pow(x[1], 2) + 15.0e0 * x[11] - 8.0e0 * x[12] - 28.0e0)
    e[12] = base + 10.0e0 * (4.0e0 * x[1] + 9.0e0 * x[2] + 5.0e0 * (_cm_pow(x[13], 2)) - 9.0e0 * x[14] - 87.0e0)
    e[13] = base + 10.0e0 * (3.0e0 * x[1] + 4.0e0 * x[2] + 3.0e0 * _cm_pow((x[13] - 6.0e0), 2) - 14.0e0 * x[14] - 10.0e0)
    e[14] = base + 10.0e0 * (14.0e0 * (_cm_pow(x[1], 2)) + 35.0e0 * x[15] - 79.0e0 * x[16] - 92.0e0)
    e[15] = base + 10.0e0 * (15.0e0 * (_cm_pow(x[2], 2)) + 11.0e0 * x[15] - 61.0e0 * x[16] - 54.0e0)
    e[16] = base + 10.0e0 * (5.0e0 * (_cm_pow(x[1], 2)) + 2.0e0 * x[2] + 9.0e0 * (_cm_pow(x[17], 4)) - x[18] - 68.0e0)
    e[17] = base + 10.0e0 * (_cm_pow(x[1], 2) - x[2] + 19.0e0 * x[19] - 20.0e0 * x[20] + 19.0e0)
    e[18] = base + 10.0e0 * (7.0e0 * (_cm_pow(x[1], 2)) + 5.0e0 * (_cm_pow(x[2], 2)) + (_cm_pow(x[19], 2)) - 30.0e0 * x[20])
    objvar = e[1]
    for i in range(2, (18) + 1):
        if e[i] > objvar:
            objvar = e[i]
    fout = objvar
    return fout


xmin = [-10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000]
xmax = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
x0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "problem2.21.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
