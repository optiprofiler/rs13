import bam

import math as _math
_INF = float('inf')
_NAN = float('nan')
def _cm_exp(a):
    try:
        return _math.exp(a)
    except OverflowError:
        return _INF

def objective(x):
    f = 0.0
    v = [0.0] * (4)
    v[0] = x[0] / 10.
    v[1] = -v[0]
    v[0] = _cm_exp(v[1])
    v[1] = x[1] / 10.
    v[2] = -v[1]
    v[1] = _cm_exp(v[2])
    v[2] = v[0] - v[1]
    v[0] = -0.5369579768645172 * x[2]
    v[1] = v[2] + v[0]
    v[2] = v[1] * v[1]
    v[1] = -0.2 * x[0]
    v[0] = _cm_exp(v[1])
    v[1] = -0.2 * x[1]
    v[3] = _cm_exp(v[1])
    v[1] = v[0] - v[3]
    v[0] = -0.6833954698413691 * x[2]
    v[3] = v[1] + v[0]
    v[1] = v[3] * v[3]
    v[2] += v[1]
    v[1] = -0.3 * x[0]
    v[3] = _cm_exp(v[1])
    v[1] = -0.3 * x[1]
    v[0] = _cm_exp(v[1])
    v[1] = v[3] - v[0]
    v[3] = -0.6910311523138539 * x[2]
    v[0] = v[1] + v[3]
    v[1] = v[0] * v[0]
    v[2] += v[1]
    v[1] = -0.4 * x[0]
    v[0] = _cm_exp(v[1])
    v[1] = -0.4 * x[1]
    v[3] = _cm_exp(v[1])
    v[1] = v[0] - v[3]
    v[0] = -0.6520044071469051 * x[2]
    v[3] = v[1] + v[0]
    v[1] = v[3] * v[3]
    v[2] += v[1]
    v[1] = -0.5 * x[0]
    v[3] = _cm_exp(v[1])
    v[1] = -0.5 * x[1]
    v[0] = _cm_exp(v[1])
    v[1] = v[3] - v[0]
    v[3] = -0.599792712713548 * x[2]
    v[0] = v[1] + v[3]
    v[1] = v[0] * v[0]
    v[2] += v[1]
    v[1] = -0.6 * x[0]
    v[0] = _cm_exp(v[1])
    v[1] = -0.6 * x[1]
    v[3] = _cm_exp(v[1])
    v[1] = v[0] - v[3]
    v[0] = -0.5463328839173601 * x[2]
    v[3] = v[1] + v[0]
    v[1] = v[3] * v[3]
    v[2] += v[1]
    v[1] = -0.7 * x[0]
    v[3] = _cm_exp(v[1])
    v[1] = -0.7 * x[1]
    v[0] = _cm_exp(v[1])
    v[1] = v[3] - v[0]
    v[3] = -0.49567342182585505 * x[2]
    v[0] = v[1] + v[3]
    v[1] = v[0] * v[0]
    v[2] += v[1]
    v[1] = -0.8 * x[0]
    v[0] = _cm_exp(v[1])
    v[1] = -0.8 * x[1]
    v[3] = _cm_exp(v[1])
    v[1] = v[0] - v[3]
    v[0] = -0.44899350148931905 * x[2]
    v[3] = v[1] + v[0]
    v[1] = v[3] * v[3]
    v[2] += v[1]
    v[1] = -0.9 * x[0]
    v[3] = _cm_exp(v[1])
    v[1] = -0.9 * x[1]
    v[0] = _cm_exp(v[1])
    v[1] = v[3] - v[0]
    v[3] = -0.4064462499365124 * x[2]
    v[0] = v[1] + v[3]
    v[1] = v[0] * v[0]
    v[2] += v[1]
    v[1] = -1. * x[0]
    v[0] = _cm_exp(v[1])
    v[1] = -1. * x[1]
    v[3] = _cm_exp(v[1])
    v[1] = v[0] - v[3]
    v[0] = -0.36783404124167984 * x[2]
    v[3] = v[1] + v[0]
    v[1] = v[3] * v[3]
    v[2] += v[1]
    f = v[2]
    return f


xmin = [-50, -50, -10000]
xmax = [50, 50, 10000]
x0 = [0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "s245.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
