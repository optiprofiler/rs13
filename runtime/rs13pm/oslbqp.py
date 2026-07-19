import bam

def objective(x):
    f = 0.0
    v = [0.0] * (3)
    rv = 0.0
    v[0] = x[0] * x[0]
    v[1] = 0.5 * v[0]
    v[0] = x[1] * x[1]
    v[2] = 0.5 * v[0]
    v[1] += v[2]
    v[2] = x[2] * x[2]
    v[0] = 0.5 * v[2]
    v[1] += v[0]
    v[0] = x[3] * x[3]
    v[2] = 0.5 * v[0]
    v[1] += v[2]
    v[2] = x[4] * x[4]
    v[0] = 0.5 * v[2]
    v[1] += v[0]
    v[0] = x[5] * x[5]
    v[2] = 0.5 * v[0]
    v[1] += v[2]
    v[2] = x[6] * x[6]
    v[0] = 0.5 * v[2]
    v[1] += v[0]
    v[0] = x[7] * x[7]
    v[2] = 0.5 * v[0]
    v[1] += v[2]
    rv = v[1] + x[0]
    rv += 2. * x[4]
    rv += -x[7]
    f = rv
    return f


xmin = [2.5, 0, 0, 0, 0.5, 0, 0, 0]
xmax = [10000, 4.1, 10000, 10000, 4, 10000, 10000, 4.3]
x0 = [5001.25, 2.05, 5000, 5000, 2.25, 5000, 5000, 2.15]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "oslbqp.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
