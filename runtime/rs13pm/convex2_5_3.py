import bam
import math

N = 5
M = 4
A_mat = [
    [-0.3515, 0.2158, 0.4016, -11.4152, -0.5201],
    [-0.5276, 0.135, -0.4904, -7.0016, -0.1655],
    [-0.5416, -0.9611, 0.0436, -10.1405, -0.9007],
    [0.5496, 0.9556, -0.3231, -8.5094, 0.8054]
]
b_vec = [10.1222, 6.3357, 8.4508, 6.7387]

def objective(x):
    f = 0.0
    i = 0.0
    j = 0.0
    fval = 0.0
    ftemp = 0.0
    for i in range(0, M):
        ftemp = 0.0
        for j in range(0, N):
            ftemp += A_mat[i][j] * x[j]
        ftemp -= b_vec[i]
        fval += ftemp * ftemp
    fval *= 0.5
    for i in range(0, N):
        fval += math.fabs(x[i])
    f = fval
    return f


xmin = [-10000, -10000, -10000, -10000, -10000]
xmax = [10000, 10000, 10000, 10000, 10000]
x0 = [0, 0, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "convex2_5_3.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
