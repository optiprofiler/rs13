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

def objective(x):
    f = 0.0
    x1 = x[0]
    x2 = x[1]
    f = 4. * x1 * x1 - 2.1 * _cm_pow(x1, 4.) + 0.3333333333333333 * _cm_pow(x1, 6.) + x1 * x2 - 4. * x2 * x2 + 4. * _cm_pow(x2, 4.)
    return f


xmin = [-3, -1.5]
xmax = [3, 1.5]
x0 = [0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "camel6.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
