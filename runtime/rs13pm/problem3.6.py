import bam

def _post(_v, _name, _delta):
    _old = _v.get(_name, 0)
    _v[_name] = _old + _delta
    return _old

def objective(xin):
    fout = 0.0
    _v = {}
    bam_idx = 0
    x1 = 0.0
    x2 = 0.0
    y1 = 0.0
    y2 = 0.0
    y3 = 0.0
    objvar = 0.0
    x1 = xin[_post(_v, 'bam_idx', 1)]
    x2 = xin[_post(_v, 'bam_idx', 1)]
    y1 = x1 * x1 + x2 * x2
    y2 = x1 * x1 + x2 * x2 + 10.0e0 * (-4.0e0 * x1 - x2 + 4.0e0)
    y3 = x1 * x1 + x2 * x2 + 10.0e0 * (-x1 - 2.0e0 * x2 + 6.0e0)
    objvar = y1
    if y2 > objvar:
        objvar = y2
    if y3 > objvar:
        objvar = y3
    fout = objvar
    return fout


xmin = [-10000, -10000]
xmax = [10000, 10000]
x0 = [0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "problem3.6.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
