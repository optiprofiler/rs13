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
    ni = 6
    nj = 11
    x = [0.0] * (ni + 1)
    y = [0.0] * (nj + 1)
    t = [0.0] * (nj + 1)
    a = [0.0] * (nj + 1)
    obj = 0.0
    term = 0.0
    i = 0.0
    j = 0.0
    _init_t = [0.0e0,0.1e0,0.2e0,0.3e0,0.4e0,0.5e0,0.6e0,0.7e0,0.8e0,0.9e0,1.0e0]
    _k = 0.0
    for _k in range(0, 11):
        t[_k + 1] = _init_t[_k]
    for i in range(1, (ni) + 1):
        x[i] = xin[_post(_v, 'bam_idx', 1)]
    # a(j) generated from the Luksan-Vlcek formula (report V-798,
    # problem 2.17; identical generator to problem 2.16):
    #   a(t) = 0.5*exp(-t) - exp(-2t) + 0.5*exp(-3t)
    #          + 1.5*exp(-1.5t)*sin(7t) + exp(-2.5t)*sin(5t)
    for j in range(1, (nj) + 1):
        a[j] = (0.5 * math.exp(-t[j]) - math.exp(-2.0 * t[j])
                + 0.5 * math.exp(-3.0 * t[j])
                + 1.5 * math.exp(-1.5 * t[j]) * math.sin(7.0 * t[j])
                + math.exp(-2.5 * t[j]) * math.sin(5.0 * t[j]))
        term = x[1] * _cm_exp(-x[2] * t[j]) * math.cos(x[3] * t[j] + x[4]) + x[5] * _cm_exp(-x[6] * t[j]) - a[j]
        y[j] = math.fabs(term)
    obj = y[1]
    for j in range(2, (nj) + 1):
        if y[j] > obj:
            obj = y[j]
    fout = obj
    return fout


xmin = [-1000, -1000, -1000, -1000, -1000, -1000]
xmax = [1000, 1000, 1000, 1000, 1000, 1000]
x0 = [0, 0, 0, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "problem2.17.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
