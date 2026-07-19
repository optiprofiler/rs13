import bam

def objective(x):
    f = 0.0
    v = [0.0] * (3)
    v[0] = -1. + x[0]
    v[1] = v[0] * v[0]
    v[0] = x[1] - x[2]
    v[2] = v[0] * v[0]
    v[1] += v[2]
    v[2] = x[2] - x[3]
    v[0] = v[2] * v[2]
    v[1] += v[0]
    v[0] = x[3] - x[4]
    v[2] = v[0] * v[0]
    v[1] += v[2]
    v[2] = x[4] - x[5]
    v[0] = v[2] * v[2]
    v[1] += v[0]
    v[0] = x[5] - x[6]
    v[2] = v[0] * v[0]
    v[1] += v[2]
    v[2] = x[6] - x[7]
    v[0] = v[2] * v[2]
    v[1] += v[0]
    v[0] = x[7] - x[8]
    v[2] = v[0] * v[0]
    v[1] += v[2]
    v[2] = x[8] - x[9]
    v[0] = v[2] * v[2]
    v[1] += v[0]
    v[0] = -1. + x[9]
    v[2] = v[0] * v[0]
    v[1] += v[2]
    f = v[1]
    return f


xmin = [-10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000]
xmax = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
x0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "dixon3dq.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
