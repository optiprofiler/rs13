import bam
import math

N = 5
M = 4
A_mat = [
    [-0.8387, 1.2932, -0.269, -3.0748, -0.8761],
    [1.0629, -0.064, 3.0268, -0.1272, -1.1116],
    [-1.6624, 0.4409, 0.3059, 1.4212, 4.0919],
    [1.5143, -1.4751, 0.1381, 2.0521, -3.8762]
]
b_vec = [1.479, 2.3823, 1.1265, -1.0119]

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
                   options={"tracefname": "convex2_5_5.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
