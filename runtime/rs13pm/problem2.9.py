import bam
import math

def _post(_v, _name, _delta):
    _old = _v.get(_name, 0)
    _v[_name] = _old + _delta
    return _old

def objective(xin):
    fout = 0.0
    _v = {}
    bam_idx = 0
    j = 0.0
    u = [0.0] * (11 + 1)
    a = [0.0] * (11 + 1)
    x1 = 0.0
    x2 = 0.0
    x3 = 0.0
    x4 = 0.0
    yj = 0.0
    objvar = 0.0
    num = 0.0
    den = 0.0
    _init_u = [4.0e0,2.0e0,1.0e0,0.5e0,0.25e0,0.167e0,0.125e0,0.1e0,0.0833e0,0.0714e0,0.0625e0]
    _k = 0.0
    for _k in range(0, 11):
        u[_k + 1] = _init_u[_k]
    _init_a = [0.1957e0,0.1947e0,0.1735e0,0.1600e0,0.0844e0,0.0627e0,0.0456e0,0.0342e0,0.0323e0,0.0235e0,0.0246e0]
    _k = 0.0
    for _k in range(0, 11):
        a[_k + 1] = _init_a[_k]
    x1 = xin[_post(_v, 'bam_idx', 1)]
    x2 = xin[_post(_v, 'bam_idx', 1)]
    x3 = xin[_post(_v, 'bam_idx', 1)]
    x4 = xin[_post(_v, 'bam_idx', 1)]
    objvar = -1.0e300
    for j in range(1, (11) + 1):
        num = x1 * (u[j] * u[j] + x2 * u[j])
        den = u[j] * u[j] + x3 * u[j] + x4
        if den == 0.e0:
            yj = 1.e300
        else:
            yj = math.fabs(num / den - a[j])
        if yj > objvar:
            objvar = yj
    fout = objvar
    return fout


xmin = [-10000, -10000, -10000, -10000]
xmax = [10000, 10000, 10000, 10000]
x0 = [0, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "problem2.9.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
