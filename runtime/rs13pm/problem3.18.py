import bam

import math as _math
_INF = float('inf')
_NAN = float('nan')
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
    i = 0.0
    x = [0.0] * (12 + 1)
    p = [0.0] * (6 + 1)
    pbar = [0.0] * (6 + 1)
    a = [[0.0] * (2 + 1) for _ in range(6 + 1)]
    abar21 = 5.5e0
    abar22 = -1.0e0
    objvar = 0.0
    dx1 = 0.0
    dx2 = 0.0
    _init_p = [2e0,1e0,1e0,5e0,1e0,1e0]
    _k = 0.0
    for _k in range(0, 6):
        p[_k + 1] = _init_p[_k]
    _init_pbar = [1e0,1e0,2e0,3e0,2e0,0e0]
    _k = 0.0
    for _k in range(0, 6):
        pbar[_k + 1] = _init_pbar[_k]
    _init_A = [0.0,2.0,3.0,4.0,5.0,6.0,2.0,3.0,-1.0,-0.5,2.0,2.0]
    i = 0.0
    j = 0.0
    k = 0
    for j in range(1, (2) + 1):
        for i in range(1, (6) + 1):
            a[i][j] = _init_A[k]
            k = k + 1
    for i in range(1, (12) + 1):
        x[i] = xin[_post(_v, 'bam_idx', 1)]
    objvar = 0.0e0
    objvar = objvar + _cm_sqrt(x[1] * x[1] + x[7] * x[7])
    dx1 = abar21 - x[6]
    dx2 = abar22 - x[12]
    objvar = objvar + _cm_sqrt(dx1 * dx1 + dx2 * dx2)
    for i in range(1, (6) + 1):
        dx1 = a[i][1] - x[i]
        dx2 = a[i][2] - x[i + 6]
        objvar = objvar + p[i] * _cm_sqrt(dx1 * dx1 + dx2 * dx2)
    for i in range(1, (5) + 1):
        dx1 = x[i] - x[i + 1]
        dx2 = x[i + 6] - x[i + 7]
        objvar = objvar + pbar[i] * _cm_sqrt(dx1 * dx1 + dx2 * dx2)
    fout = objvar
    return fout


xmin = [-10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000]
xmax = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
x0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "problem3.18.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
