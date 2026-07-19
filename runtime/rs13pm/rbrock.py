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
    v[0] = v[1] + v[2]
    f = v[0]
    return f


xmin = [-10, -10]
xmax = [5, 10]
x0 = [-2.5, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "rbrock.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
