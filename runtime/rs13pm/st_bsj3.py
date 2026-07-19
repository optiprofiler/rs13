import bam

def objective(x):
    f = 0.0
    v = [0.0] * (3)
    rv = 0.0
    v[0] = x[0] * x[0]
    v[1] = -1.5 * v[0]
    v[0] = x[1] * x[1]
    v[2] = -v[0]
    v[1] += v[2]
    v[2] = x[2] * x[2]
    v[0] = -v[2]
    v[1] += v[0]
    v[0] = x[3] * x[3]
    v[2] = -2. * v[0]
    v[1] += v[2]
    v[2] = x[4] * x[4]
    v[0] = -v[2]
    v[1] += v[0]
    v[0] = x[5] * x[5]
    v[2] = -2.5 * v[0]
    v[1] += v[2]
    rv = v[1] + 10.5 * x[0]
    rv += -3.95 * x[1]
    rv += 3. * x[2]
    rv += 5. * x[3]
    rv += 1.5 * x[4]
    rv += -1.5 * x[5]
    f = rv
    return f


xmin = [0, 0, 0, 0, 0, 0]
xmax = [99, 99, 99, 99, 99, 99]
x0 = [49.5, 49.5, 49.5, 49.5, 49.5, 49.5]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "st_bsj3.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
