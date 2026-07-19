import bam
import math

def objective(x):
    f = 0.0
    v = [0.0] * (3)
    rv = 0.0
    v[0] = -x[1]
    v[1] = math.sin(x[0])
    v[2] = v[0] + v[1]
    v[0] = v[2] * v[2]
    v[2] = 100. * v[0]
    rv = v[2] + x[0]
    f = rv
    return f


xmin = [0, -10000]
xmax = [10000, 10000]
x0 = [5000, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "mdhole.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
