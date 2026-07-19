import bam
import math

N = 5
M = 4
A_mat = [
    [0.4998, 1.166, -2.1219, 3.5246, 0.0657],
    [1.1149, -0.0559, 0.0932, 1.7253, -0.2985],
    [-1.6665, -0.2713, 0.118, -1.4512, 0.878],
    [1.7084, -0.2251, 3.4803, 3.7248, 0.7519]
]
b_vec = [4.6944, 2.3443, -1.3168, 2.9515]

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
                   options={"tracefname": "convex2_5_4.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
