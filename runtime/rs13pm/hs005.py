import bam
import math

def objective(x):
    f = 0.0
    v = [0.0] * (3)
    rv = 0.0
    v[0] = x[0] + x[1]
    v[1] = math.sin(v[0])
    v[0] = x[0] - x[1]
    v[2] = v[0] * v[0]
    v[1] += v[2]
    v[1] += 1.
    rv = v[1] - 1.5 * x[0]
    rv += 2.5 * x[1]
    f = rv
    return f


xmin = [-1.5, -3]
xmax = [4, 3]
x0 = [1.25, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "hs005.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
