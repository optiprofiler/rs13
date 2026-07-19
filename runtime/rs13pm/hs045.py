import bam

def objective(x):
    f = 0.0
    v = [0.0] * (2)
    v[0] = x[0] * x[1]
    v[1] = v[0] * x[2]
    v[0] = v[1] * x[3]
    v[1] = v[0] * x[4]
    v[0] = -0.008333333333333333 * v[1]
    v[1] = v[0] + 2.
    f = v[1]
    return f


xmin = [0, 0, 0, 0, 0]
xmax = [1, 2, 3, 4, 5]
x0 = [0.5, 1, 1.5, 2, 2.5]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "hs045.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
