import bam

def objective(x):
    f = 0.0
    v = [0.0] * (2)
    rv = 0.0
    v[0] = x[1] - x[0]
    v[1] = v[0] * v[0]
    v[0] = 1.e-05 * v[1]
    rv = v[0] + x[1]
    f = rv
    return f


xmin = [-10000, 0]
xmax = [10000, 10000]
x0 = [0, 5000]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "hs003.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
