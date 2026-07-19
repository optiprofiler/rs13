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
    ii = 0.0
    x = [0.0] * (5 + 1)
    A = [[0.0] * (5 + 1) for _ in range(10 + 1)]
    C = [[0.0] * (5 + 1) for _ in range(5 + 1)]
    b = [0.0] * (10 + 1)
    d = [0.0] * (5 + 1)
    e = [0.0] * (5 + 1)
    y = 0.0
    f = 0.0
    objvar = 0.0
    val = 0.0
    cubic_term = 0.0
    quad_term = 0.0
    linear_term = 0.0
    for i in range(1, (5) + 1):
        x[i] = xin[_post(_v, 'bam_idx', 1)]
    _init_A = [-16,0,-3.5,0,0,2,-1,-1,1,1,2,-2,0,-2,-9,0,-1,-2,2,1,0,0,2,0,-2,-4,-1,-3,3,1,1,4,0,-4,1,0,-1,-2,4,1,0,2,0,-1,-2.8,0,-1,-1,5,1]
    i = 0.0
    j = 0.0
    k = 0
    for i in range(1, (5) + 1):
        for j in range(1, (10) + 1):
            A[j][i] = _init_A[k]
            k = k + 1
    _init_C = [30,-20,-10,32,-10,-20,39,-6,-31,32,-10,-6,10,-6,-10,32,-31,-6,39,-20,-10,32,-10,-20,30]
    i = 0.0
    j = 0.0
    k = 0
    for j in range(1, (5) + 1):
        for i in range(1, (5) + 1):
            C[i][j] = _init_C[k]
            k = k + 1
    _init_b = [-40.0e0,-2.0e0,-0.25e0,-4.0e0,-4.0e0,-1.0e0,-40.0e0,-60.0e0,5.0e0,1.0e0]
    _k = 0.0
    for _k in range(0, 10):
        b[_k + 1] = _init_b[_k]
    _init_d = [4.0e0,8.0e0,10.0e0,6.0e0,2.0e0]
    _k = 0.0
    for _k in range(0, 5):
        d[_k + 1] = _init_d[_k]
    _init_e = [-15.0e0,-27.0e0,-36.0e0,-18.0e0,-12.0e0]
    _k = 0.0
    for _k in range(0, 5):
        e[_k + 1] = _init_e[_k]
    y = -1.0e300
    for j in range(1, (10) + 1):
        val = 0.0e0
        for i in range(1, (5) + 1):
            val = val + A[j][i] * x[i]
        val = b[j] - val
        if val > y:
            y = val
    f = y
    cubic_term = 0.0e0
    for i in range(1, (5) + 1):
        cubic_term = cubic_term + d[i] * _cm_pow(x[i], 3)
    quad_term = 0.0e0
    for i in range(1, (5) + 1):
        for ii in range(1, (5) + 1):
            quad_term = quad_term + C[i][ii] * x[i] * x[ii]
    linear_term = 0.0e0
    for i in range(1, (5) + 1):
        linear_term = linear_term + e[i] * x[i]
    objvar = cubic_term + quad_term + linear_term + 50.0e0 * f
    fout = objvar
    return fout


xmin = [0, 0, 0, 0, 0]
xmax = [10000, 10000, 10000, 10000, 10000]
x0 = [0, 0, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "problem3.13.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
