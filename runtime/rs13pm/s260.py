import bam

def objective(x):
    f = 0.0
    v = [0.0] * (3)
    v[0] = x[0] * x[0]
    v[1] = x[1] - v[0]
    v[0] = v[1] * v[1]
    v[1] = 100. * v[0]
    v[0] = 1. - x[0]
    v[2] = v[0] * v[0]
    v[1] += v[2]
    v[2] = x[2] * x[2]
    v[0] = x[3] - v[2]
    v[2] = v[0] * v[0]
    v[0] = 90. * v[2]
    v[1] += v[0]
    v[0] = 1. - x[2]
    v[2] = v[0] * v[0]
    v[1] += v[2]
    v[2] = -2. + x[1]
    v[2] += x[3]
    v[0] = v[2] * v[2]
    v[2] = 9.9 * v[0]
    v[1] += v[2]
    v[2] = -1. + x[1]
    v[0] = v[2] * v[2]
    v[2] = 0.2 * v[0]
    v[1] += v[2]
    v[2] = -1. + x[3]
    v[0] = v[2] * v[2]
    v[2] = 0.2 * v[0]
    v[1] += v[2]
    f = v[1]
    return f


xmin = [-10000, -10000, -10000, -10000]
xmax = [10000, 10000, 10000, 10000]
x0 = [0, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "s260.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
