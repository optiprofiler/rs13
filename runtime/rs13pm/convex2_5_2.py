import bam
import math

N = 5
M = 4
A_mat = [
    [-0.0859, 0.1808, 1.1179, -34.675, -0.7402],
    [-0.4768, 1.5166, -0.5267, 2.3941, 0.1376],
    [1.0633, -0.7785, 0.2988, 21.7019, -0.0612],
    [0.274, 0.935, -1.8687, 33.7391, -0.9762]
]
b_vec = [-9.5049, 0.6176, 7.0707, 10.3214]

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
                   options={"tracefname": "convex2_5_2.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
