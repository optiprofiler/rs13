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
    j = 0.0
    x = [0.0] * (5 + 1)
    A = [[0.0] * (5 + 1) for _ in range(10 + 1)]
    b = [0.0] * (10 + 1)
    val = 0.0
    objvar = 0.0
    _init_A = [0,2,1,1,3,0,1,1,0,1,0,1,2,4,2,2,1,0,0,1,0,1,1,1,1,1,1,1,2,2,0,1,1,2,0,0,1,2,1,0,0,3,2,2,1,1,1,1,0,0]
    i = 0.0
    j = 0.0
    k = 0
    for i in range(1, (5) + 1):
        for j in range(1, (10) + 1):
            A[j][i] = _init_A[k]
            k = k + 1
    _init_b = [1.0e0,5.0e0,10.0e0,2.0e0,4.0e0,3.0e0,1.7e0,2.5e0,6.0e0,3.5e0]
    _k = 0.0
    for _k in range(0, 10):
        b[_k + 1] = _init_b[_k]
    for i in range(1, (5) + 1):
        x[i] = xin[_post(_v, 'bam_idx', 1)]
    objvar = -1.0e300
    for j in range(1, (10) + 1):
        val = 0.0e0
        for i in range(1, (5) + 1):
            val = val + _cm_pow((x[i] - A[j][i]), 2)
        val = b[j] * val
        if val > objvar:
            objvar = val
    fout = objvar
    return fout


xmin = [-10000, -10000, -10000, -10000, -10000]
xmax = [10000, 10000, 10000, 10000, 10000]
x0 = [0, 0, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "problem3.12.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
