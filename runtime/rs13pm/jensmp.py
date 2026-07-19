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
    v[0] = _cm_exp(x[0])
    v[1] = _cm_exp(x[1])
    v[2] = v[0] + v[1]
    v[0] = 4. - v[2]
    v[2] = v[0] * v[0]
    v[0] = 2. * x[0]
    v[1] = _cm_exp(v[0])
    v[0] = 2. * x[1]
    v[3] = _cm_exp(v[0])
    v[0] = v[1] + v[3]
    v[1] = 6. - v[0]
    v[0] = v[1] * v[1]
    v[2] += v[0]
    v[0] = 3. * x[0]
    v[1] = _cm_exp(v[0])
    v[0] = 3. * x[1]
    v[3] = _cm_exp(v[0])
    v[0] = v[1] + v[3]
    v[1] = 8. - v[0]
    v[0] = v[1] * v[1]
    v[2] += v[0]
    v[0] = 4. * x[0]
    v[1] = _cm_exp(v[0])
    v[0] = 4. * x[1]
    v[3] = _cm_exp(v[0])
    v[0] = v[1] + v[3]
    v[1] = 10. - v[0]
    v[0] = v[1] * v[1]
    v[2] += v[0]
    v[0] = 5. * x[0]
    v[1] = _cm_exp(v[0])
    v[0] = 5. * x[1]
    v[3] = _cm_exp(v[0])
    v[0] = v[1] + v[3]
    v[1] = 12. - v[0]
    v[0] = v[1] * v[1]
    v[2] += v[0]
    v[0] = 6. * x[0]
    v[1] = _cm_exp(v[0])
    v[0] = 6. * x[1]
    v[3] = _cm_exp(v[0])
    v[0] = v[1] + v[3]
    v[1] = 14. - v[0]
    v[0] = v[1] * v[1]
    v[2] += v[0]
    v[0] = 7. * x[0]
    v[1] = _cm_exp(v[0])
    v[0] = 7. * x[1]
    v[3] = _cm_exp(v[0])
    v[0] = v[1] + v[3]
    v[1] = 16. - v[0]
    v[0] = v[1] * v[1]
    v[2] += v[0]
    v[0] = 8. * x[0]
    v[1] = _cm_exp(v[0])
    v[0] = 8. * x[1]
    v[3] = _cm_exp(v[0])
    v[0] = v[1] + v[3]
    v[1] = 18. - v[0]
    v[0] = v[1] * v[1]
    v[2] += v[0]
    v[0] = 9. * x[0]
    v[1] = _cm_exp(v[0])
    v[0] = 9. * x[1]
    v[3] = _cm_exp(v[0])
    v[0] = v[1] + v[3]
    v[1] = 20. - v[0]
    v[0] = v[1] * v[1]
    v[2] += v[0]
    v[0] = 10. * x[0]
    v[1] = _cm_exp(v[0])
    v[0] = 10. * x[1]
    v[3] = _cm_exp(v[0])
    v[0] = v[1] + v[3]
    v[1] = 22. - v[0]
    v[0] = v[1] * v[1]
    v[2] += v[0]
    f = v[2]
    return f


xmin = [-15, -15]
xmax = [15, 15]
x0 = [0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "jensmp.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
