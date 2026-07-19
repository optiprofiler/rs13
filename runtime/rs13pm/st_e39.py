import bam

def objective(x):
    f = 0.0
    v = [0.0] * (4)
    v[0] = -4. + x[0]
    v[1] = v[0] * v[0]
    v[1] += 0.1
    v[0] = -4. + x[1]
    v[2] = v[0] * v[0]
    v[1] += v[2]
    v[2] = -1. / v[1]
    v[1] = -1. + x[0]
    v[0] = v[1] * v[1]
    v[0] += 0.2
    v[1] = -1. + x[1]
    v[3] = v[1] * v[1]
    v[0] += v[3]
    v[3] = 1. / v[0]
    v[0] = -v[3]
    v[2] += v[0]
    v[0] = -8. + x[0]
    v[3] = v[0] * v[0]
    v[3] += 0.2
    v[0] = -8. + x[1]
    v[1] = v[0] * v[0]
    v[3] += v[1]
    v[1] = 1. / v[3]
    v[3] = -v[1]
    v[2] += v[3]
    f = v[2]
    return f


xmin = [-10000, -10000]
xmax = [10000, 10000]
x0 = [0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "st_e39.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
