import bam

def objective(x):
    f = 0.0
    v = [0.0] * (3)
    rv = 0.0
    v[0] = 9. * x[0]
    v[1] = v[0] * x[0]
    v[0] = 9. * x[1]
    v[2] = v[0] * x[1]
    v[1] += v[2]
    v[2] = 9. * x[2]
    v[0] = v[2] * x[2]
    v[1] += v[0]
    rv = v[1] - 15. * x[0]
    rv += -12. * x[1]
    rv += -9. * x[2]
    f = rv
    return f


xmin = [0, 0, 0]
xmax = [1, 1, 1]
x0 = [0.5, 0.5, 0.5]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "st_cqpjk2.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
