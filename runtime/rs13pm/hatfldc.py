import bam

def objective(x):
    f = 0.0
    v = [0.0] * (3)
    v[0] = -1. + x[0]
    v[1] = v[0] * v[0]
    v[0] = x[1] * x[1]
    v[2] = x[2] - v[0]
    v[0] = v[2] * v[2]
    v[1] += v[0]
    v[0] = x[2] * x[2]
    v[2] = x[3] - v[0]
    v[0] = v[2] * v[2]
    v[1] += v[0]
    v[0] = -1. + x[3]
    v[2] = v[0] * v[0]
    v[1] += v[2]
    f = v[1]
    return f


xmin = [0, 0, 0, -10000]
xmax = [10, 10, 10, 10000]
x0 = [5, 5, 5, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "hatfldc.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
