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
    u = [0.0] * (15 + 1)
    v = [0.0] * (15 + 1)
    w = [0.0] * (15 + 1)
    a = [0.0] * (15 + 1)
    x1 = 0.0
    x2 = 0.0
    x3 = 0.0
    yj = 0.0
    z = 0.0
    objvar = 0.0
    denom = 0.0
    _init_a = [0.14e0,0.18e0,0.22e0,0.25e0,0.29e0,0.32e0,0.35e0,0.39e0,0.37e0,0.58e0,0.73e0,0.96e0,1.34e0,2.10e0,4.39e0]
    _k = 0.0
    for _k in range(0, 15):
        a[_k + 1] = _init_a[_k]
    x1 = xin[_post(_v, 'bam_idx', 1)]
    x2 = xin[_post(_v, 'bam_idx', 1)]
    x3 = xin[_post(_v, 'bam_idx', 1)]
    for j in range(1, (15) + 1):
        u[j] = (j)
        v[j] = 16.0e0 - (j)
        if u[j] < v[j]:
            w[j] = u[j]
        else:
            w[j] = v[j]
    z = -1.0e300
    for j in range(1, (15) + 1):
        denom = v[j] * x2 + w[j] * x3
        if denom == 0.e0:
            yj = 1.0e300
        else:
            yj = x1 + u[j] / denom - a[j]
            yj = math.fabs(yj)
        if yj > z:
            z = yj
    objvar = z
    fout = objvar
    return fout


xmin = [-10000, -10000, -10000]
xmax = [10000, 10000, 10000]
x0 = [0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "problem2.8.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
