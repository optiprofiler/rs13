import bam

def objective(x):
    f = 0.0
    v = [0.0] * (3)
    v[0] = x[0] * x[0]
    v[1] = 2. * x[1]
    v[2] = x[1] * v[1]
    v[0] += v[2]
    v[2] = 3. * x[2]
    v[1] = x[2] * v[2]
    v[0] += v[1]
    v[1] = 4. * x[3]
    v[2] = x[3] * v[1]
    v[0] += v[2]
    v[2] = 5. * x[4]
    v[1] = x[4] * v[2]
    v[0] += v[1]
    v[1] = 6. * x[5]
    v[2] = x[5] * v[1]
    v[0] += v[2]
    v[2] = 7. * x[6]
    v[1] = x[6] * v[2]
    v[0] += v[1]
    v[1] = 8. * x[7]
    v[2] = x[7] * v[1]
    v[0] += v[2]
    v[2] = 9. * x[8]
    v[1] = x[8] * v[2]
    v[0] += v[1]
    v[1] = 10. * x[9]
    v[2] = x[9] * v[1]
    v[0] += v[2]
    f = v[0]
    return f


xmin = [-10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000]
xmax = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
x0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "s291.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
