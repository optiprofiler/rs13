import bam
import math

def objective(x):
    f = 0.0
    v = [0.0] * (4)
    v[0] = 2. * x[0]
    v[1] = 1. + v[0]
    v[0] = math.cos(v[1])
    v[1] = 3. * x[0]
    v[2] = 2. + v[1]
    v[1] = math.cos(v[2])
    v[2] = 2. * v[1]
    v[0] += v[2]
    v[2] = 4. * x[0]
    v[1] = 3. + v[2]
    v[2] = math.cos(v[1])
    v[1] = 3. * v[2]
    v[0] += v[1]
    v[1] = 5. * x[0]
    v[2] = 4. + v[1]
    v[1] = math.cos(v[2])
    v[2] = 4. * v[1]
    v[0] += v[2]
    v[2] = 6. * x[0]
    v[1] = 5. + v[2]
    v[2] = math.cos(v[1])
    v[1] = 5. * v[2]
    v[0] += v[1]
    v[1] = 2. * x[1]
    v[2] = 1. + v[1]
    v[1] = math.cos(v[2])
    v[2] = 3. * x[1]
    v[3] = 2. + v[2]
    v[2] = math.cos(v[3])
    v[3] = 2. * v[2]
    v[1] += v[3]
    v[3] = 4. * x[1]
    v[2] = 3. + v[3]
    v[3] = math.cos(v[2])
    v[2] = 3. * v[3]
    v[1] += v[2]
    v[2] = 5. * x[1]
    v[3] = 4. + v[2]
    v[2] = math.cos(v[3])
    v[3] = 4. * v[2]
    v[1] += v[3]
    v[3] = 6. * x[1]
    v[2] = 5. + v[3]
    v[3] = math.cos(v[2])
    v[2] = 5. * v[3]
    v[1] += v[2]
    v[2] = v[0] * v[1]
    v[0] = -v[2]
    f = v[0]
    return f


xmin = [-10, -10]
xmax = [10, 10]
x0 = [0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "levy3.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
