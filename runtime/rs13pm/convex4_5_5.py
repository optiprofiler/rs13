import bam

N = 5
M = 4
A_mat = [
    [-0.1465, 0.8648, 3.159, -6.2397, 0.4204],
    [-0.5585, 0.8298, -2.0912, -6.8188, 0.6686],
    [0.6463, 0.3473, -2.8692, -3.8125, -0.445],
    [-0.4561, -0.5696, -3.8863, 4.0145, -0.8747]
]
b_vec = [4.1882, 5.9877, 3.8211, -1.2032]

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
    f = fval
    return f


xmin = [-10000, -10000, -10000, -10000, -10000]
xmax = [10000, 10000, 10000, 10000, 10000]
x0 = [0, 0, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "convex4_5_5.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
