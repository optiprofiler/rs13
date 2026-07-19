import bam

def objective(x):
    f = 0.0
    v = [0.0] * (3)
    v[0] = -0.171747132 + x[0]
    if v[0] < 0.:
        v[1] = -v[0]
    else:
        v[1] = v[0]
    v[0] = -0.843266708 + x[0]
    if v[0] < 0.:
        v[2] = -v[0]
    else:
        v[2] = v[0]
    v[1] += v[2]
    v[2] = -0.550375356 + x[0]
    if v[2] < 0.:
        v[0] = -v[2]
    else:
        v[0] = v[2]
    v[1] += v[0]
    v[0] = -0.301137904 + x[0]
    if v[0] < 0.:
        v[2] = -v[0]
    else:
        v[2] = v[0]
    v[1] += v[2]
    v[2] = -0.292212117 + x[0]
    if v[2] < 0.:
        v[0] = -v[2]
    else:
        v[0] = v[2]
    v[1] += v[0]
    v[0] = -0.2240528679 + x[0]
    if v[0] < 0.:
        v[2] = -v[0]
    else:
        v[2] = v[0]
    v[1] += v[2]
    v[2] = -0.349830504 + x[0]
    if v[2] < 0.:
        v[0] = -v[2]
    else:
        v[0] = v[2]
    v[1] += v[0]
    v[0] = -0.856270347 + x[0]
    if v[0] < 0.:
        v[2] = -v[0]
    else:
        v[2] = v[0]
    v[1] += v[2]
    v[2] = -0.067113723 + x[0]
    if v[2] < 0.:
        v[0] = -v[2]
    else:
        v[0] = v[2]
    v[1] += v[0]
    v[0] = -0.500210669 + x[0]
    if v[0] < 0.:
        v[2] = -v[0]
    else:
        v[2] = v[0]
    v[1] += v[2]
    v[2] = -0.998117627 + x[0]
    if v[2] < 0.:
        v[0] = -v[2]
    else:
        v[0] = v[2]
    v[1] += v[0]
    v[0] = -0.578733378 + x[0]
    if v[0] < 0.:
        v[2] = -v[0]
    else:
        v[2] = v[0]
    v[1] += v[2]
    v[2] = -0.991133039 + x[0]
    if v[2] < 0.:
        v[0] = -v[2]
    else:
        v[0] = v[2]
    v[1] += v[0]
    v[0] = -0.762250467 + x[0]
    if v[0] < 0.:
        v[2] = -v[0]
    else:
        v[2] = v[0]
    v[1] += v[2]
    v[2] = -0.130692483 + x[0]
    if v[2] < 0.:
        v[0] = -v[2]
    else:
        v[0] = v[2]
    v[1] += v[0]
    v[0] = -0.639718759 + x[0]
    if v[0] < 0.:
        v[2] = -v[0]
    else:
        v[2] = v[0]
    v[1] += v[2]
    v[2] = -0.159517864 + x[0]
    if v[2] < 0.:
        v[0] = -v[2]
    else:
        v[0] = v[2]
    v[1] += v[0]
    v[0] = -0.250080533 + x[0]
    if v[0] < 0.:
        v[2] = -v[0]
    else:
        v[2] = v[0]
    v[1] += v[2]
    v[2] = -0.668928609 + x[0]
    if v[2] < 0.:
        v[0] = -v[2]
    else:
        v[0] = v[2]
    v[1] += v[0]
    f = v[1]
    return f


xmin = [-10000]
xmax = [10000]
x0 = [0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "median.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
