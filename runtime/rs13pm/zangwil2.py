import bam

def objective(x):
    f = 0.0
    v = [0.0] * (3)
    rv = 0.0
    v[0] = x[0] * x[0]
    v[1] = 1.0666666666666667 * v[0]
    v[0] = x[1] * x[1]
    v[2] = 1.0666666666666667 * v[0]
    v[1] += v[2]
    v[2] = 8. * x[0]
    v[0] = v[2] * x[1]
    v[2] = -0.06666666666666667 * v[0]
    v[1] += v[2]
    v[1] += 66.06666666666666
    rv = v[1] - 3.7333333333333334 * x[0]
    rv += -17.066666666666666 * x[1]
    f = rv
    return f


xmin = [-10000, -10000]
xmax = [10000, 10000]
x0 = [0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "zangwil2.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
