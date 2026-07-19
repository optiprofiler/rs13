import bam
import math

N = 5
M = 4
A_mat = [
    [0.5669, -1.393, -2.2679, -3.9112, -0.2369],
    [0.5348, 0.8729, -2.0132, 9.6276, 0.531],
    [-0.2371, -1.9834, 1.6164, -9.9555, 0.5904],
    [0.342, -0.9451, 0.9736, -1.3099, -0.6263]
]
b_vec = [5.3361, -4.3938, 6.346, 1.3237]

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
                   options={"tracefname": "convex2_5_1.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
