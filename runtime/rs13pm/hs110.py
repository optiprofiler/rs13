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
def _cm_log(a):
    if a < 0.0:
        return _NAN
    if a == 0.0:
        return -_INF
    return _math.log(a)

def objective(x):
    f = 0.0
    v = [0.0] * (3)
    v[0] = -2. + x[0]
    v[1] = _cm_log(v[0])
    v[0] = v[1] * v[1]
    v[1] = 10. - x[0]
    v[2] = _cm_log(v[1])
    v[1] = v[2] * v[2]
    v[0] += v[1]
    v[1] = -2. + x[1]
    v[2] = _cm_log(v[1])
    v[1] = v[2] * v[2]
    v[0] += v[1]
    v[1] = 10. - x[1]
    v[2] = _cm_log(v[1])
    v[1] = v[2] * v[2]
    v[0] += v[1]
    v[1] = -2. + x[2]
    v[2] = _cm_log(v[1])
    v[1] = v[2] * v[2]
    v[0] += v[1]
    v[1] = 10. - x[2]
    v[2] = _cm_log(v[1])
    v[1] = v[2] * v[2]
    v[0] += v[1]
    v[1] = -2. + x[3]
    v[2] = _cm_log(v[1])
    v[1] = v[2] * v[2]
    v[0] += v[1]
    v[1] = 10. - x[3]
    v[2] = _cm_log(v[1])
    v[1] = v[2] * v[2]
    v[0] += v[1]
    v[1] = -2. + x[4]
    v[2] = _cm_log(v[1])
    v[1] = v[2] * v[2]
    v[0] += v[1]
    v[1] = 10. - x[4]
    v[2] = _cm_log(v[1])
    v[1] = v[2] * v[2]
    v[0] += v[1]
    v[1] = -2. + x[5]
    v[2] = _cm_log(v[1])
    v[1] = v[2] * v[2]
    v[0] += v[1]
    v[1] = 10. - x[5]
    v[2] = _cm_log(v[1])
    v[1] = v[2] * v[2]
    v[0] += v[1]
    v[1] = -2. + x[6]
    v[2] = _cm_log(v[1])
    v[1] = v[2] * v[2]
    v[0] += v[1]
    v[1] = 10. - x[6]
    v[2] = _cm_log(v[1])
    v[1] = v[2] * v[2]
    v[0] += v[1]
    v[1] = -2. + x[7]
    v[2] = _cm_log(v[1])
    v[1] = v[2] * v[2]
    v[0] += v[1]
    v[1] = 10. - x[7]
    v[2] = _cm_log(v[1])
    v[1] = v[2] * v[2]
    v[0] += v[1]
    v[1] = -2. + x[8]
    v[2] = _cm_log(v[1])
    v[1] = v[2] * v[2]
    v[0] += v[1]
    v[1] = 10. - x[8]
    v[2] = _cm_log(v[1])
    v[1] = v[2] * v[2]
    v[0] += v[1]
    v[1] = -2. + x[9]
    v[2] = _cm_log(v[1])
    v[1] = v[2] * v[2]
    v[0] += v[1]
    v[1] = 10. - x[9]
    v[2] = _cm_log(v[1])
    v[1] = v[2] * v[2]
    v[0] += v[1]
    v[1] = x[0] * x[1]
    v[2] = v[1] * x[2]
    v[1] = v[2] * x[3]
    v[2] = v[1] * x[4]
    v[1] = v[2] * x[5]
    v[2] = v[1] * x[6]
    v[1] = v[2] * x[7]
    v[2] = v[1] * x[8]
    v[1] = v[2] * x[9]
    v[2] = _cm_pow(v[1], 0.2)
    v[1] = -v[2]
    v[0] += v[1]
    f = v[0]
    return f


xmin = [2.001, 2.001, 2.001, 2.001, 2.001, 2.001, 2.001, 2.001, 2.001, 2.001]
xmax = [9.999, 9.999, 9.999, 9.999, 9.999, 9.999, 9.999, 9.999, 9.999, 9.999]
x0 = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "hs110.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
