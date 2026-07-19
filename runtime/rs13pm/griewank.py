import bam
import math

def objective(x):
    f = 0.0
    v = [0.0] * (4)
    v[0] = x[0] * x[0]
    v[1] = 0.005 * v[0]
    v[0] = x[1] * x[1]
    v[2] = 0.005 * v[0]
    v[1] += v[2]
    v[2] = math.cos(x[0])
    v[0] = x[1] / 1.4142135623730951
    v[3] = math.cos(v[0])
    v[0] = v[2] * v[3]
    v[2] = -v[0]
    v[1] += v[2]
    v[1] += 1.
    f = v[1]
    return f


xmin = [-100, -100]
xmax = [100, 100]
x0 = [0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "griewank.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
