import bam
import math

def objective(x):
    f = 0.0
    v = [0.0] * (3)
    v[0] = x[0] * x[0]
    v[1] = 0.12918450914398066 * v[0]
    v[0] = x[1] - v[1]
    v[1] = 1.5915494309189535 * x[0]
    v[2] = v[0] + v[1]
    v[0] = -6. + v[2]
    v[2] = v[0] * v[0]
    v[0] = math.cos(x[0])
    v[1] = 9.602112642270262 * v[0]
    v[2] += v[1]
    v[2] += 10.
    f = v[2]
    return f


xmin = [-5, 0]
xmax = [10, 15]
x0 = [2.5, 7.5]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "branin.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
