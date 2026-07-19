import bam
import math

def objective(x):
    f = 0.0
    v = [0.0] * (5)
    rv = 0.0
    v[0] = x[0] * x[0]
    v[1] = x[1] * x[1]
    v[0] += v[1]
    v[1] = 2. + x[2]
    v[2] = v[1] * v[1]
    v[0] += v[2]
    v[2] = math.sin(x[2])
    v[1] = v[2] * v[2]
    v[0] += v[1]
    v[1] = x[0] * x[0]
    v[2] = x[1] * x[1]
    v[3] = v[1] * v[2]
    v[0] += v[3]
    v[3] = math.sin(x[2])
    v[1] = v[3] * v[3]
    v[0] += v[1]
    v[1] = x[1] * x[1]
    v[3] = v[1] * v[1]
    v[0] += v[3]
    v[3] = x[2] * x[2]
    v[1] = 2. + x[0]
    v[2] = v[1] * v[1]
    v[1] = v[3] + v[2]
    v[3] = v[1] * v[1]
    v[0] += v[3]
    v[3] = -3.173178189568194 + x[0]
    v[1] = x[1] * x[1]
    v[2] = x[2] * x[2]
    v[4] = v[1] * v[2]
    v[3] += v[4]
    v[4] = v[3] * v[3]
    v[0] += v[4]
    v[0] += -0.3163656937942707
    rv = v[0] + x[2]
    f = rv
    return f


xmin = [-10000, 1, -10000]
xmax = [10000, 10000, 1]
x0 = [0, 5000.5, -4999.5]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "allinit.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
