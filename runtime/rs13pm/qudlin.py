import bam

def objective(x):
    f = 0.0
    v = [0.0] * (2)
    rv = 0.0
    v[0] = x[0] * x[1]
    v[1] = x[1] * x[2]
    v[0] += v[1]
    v[1] = x[2] * x[3]
    v[0] += v[1]
    v[1] = x[3] * x[4]
    v[0] += v[1]
    v[1] = x[4] * x[5]
    v[0] += v[1]
    v[1] = x[5] * x[6]
    v[0] += v[1]
    rv = v[0] - 10. * x[0]
    rv += -20. * x[1]
    rv += -30. * x[2]
    rv += -40. * x[3]
    rv += -50. * x[4]
    rv += -60. * x[5]
    rv += -70. * x[6]
    rv += -80. * x[7]
    rv += -90. * x[8]
    rv += -100. * x[9]
    rv += -110. * x[10]
    rv += -120. * x[11]
    f = rv
    return f


xmin = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
xmax = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
x0 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "qudlin.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
