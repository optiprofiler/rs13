import bam

def objective(x):
    f = 0.0
    v = [0.0] * (1)
    rv = 0.0
    v[0] = x[0] * x[0]
    rv = v[0] + x[0]
    f = rv
    return f


xmin = [0]
xmax = [0.5]
x0 = [0.25]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "bqp1var.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
