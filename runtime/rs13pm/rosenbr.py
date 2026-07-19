import bam

def objective(x):
    f = 0.0
    v = [0.0] * (7)
    v[0] = x[0] * x[0]
    v[5] = -10. * v[0]
    v[5] = v[5] + 10. * x[1]
    v[6] = 1. - x[0]
    v[2] = v[5] * v[5]
    v[3] = v[6] * v[6]
    v[4] = v[2] + v[3]
    f = v[4]
    return f


xmin = [-10000, -10000]
xmax = [10000, 10000]
x0 = [0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "rosenbr.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
