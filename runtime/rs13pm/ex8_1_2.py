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

def objective(x):
    f = 0.0
    v = [0.0] * (3)
    v[0] = -2.09439333333333 + x[0]
    v[1] = math.cos(v[0])
    v[0] = -4.21478541710781 * v[1]
    v[1] = 10.8095222429746 + v[0]
    v[0] = _cm_pow(v[1], 6.)
    v[1] = 588600. / v[0]
    v[0] = -2.09439333333333 + x[0]
    v[2] = math.cos(v[0])
    v[0] = -4.21478541710781 * v[2]
    v[2] = 10.8095222429746 + v[0]
    v[0] = _cm_pow(v[2], 3.)
    v[2] = 1079.1 / v[0]
    v[0] = -v[2]
    v[1] += v[0]
    v[0] = math.cos(x[0])
    v[2] = -4.21478541710781 * v[0]
    v[0] = 10.8095222429746 + v[2]
    v[2] = _cm_pow(v[0], 6.)
    v[0] = 600800. / v[2]
    v[1] += v[0]
    v[0] = math.cos(x[0])
    v[2] = -4.21478541710781 * v[0]
    v[0] = 10.8095222429746 + v[2]
    v[2] = _cm_pow(v[0], 3.)
    v[0] = 1071.5 / v[2]
    v[2] = -v[0]
    v[1] += v[2]
    v[2] = 2.09439333333333 + x[0]
    v[0] = math.cos(v[2])
    v[2] = -4.21478541710781 * v[0]
    v[0] = 10.8095222429746 + v[2]
    v[2] = _cm_pow(v[0], 6.)
    v[0] = 481300. / v[2]
    v[1] += v[0]
    v[0] = 2.09439333333333 + x[0]
    v[2] = math.cos(v[0])
    v[0] = -4.21478541710781 * v[2]
    v[2] = 10.8095222429746 + v[0]
    v[0] = _cm_pow(v[2], 3.)
    v[2] = 1064.6 / v[0]
    v[0] = -v[2]
    v[1] += v[0]
    f = v[1]
    return f


xmin = [0]
xmax = [6.28318]
x0 = [3.14159]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "ex8_1_2.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
