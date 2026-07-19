import bam

N = 5
M = 4
A_mat = [
    [-0.7572, 0.3436, -0.0032, 1.4487, 0.3832],
    [-0.1709, -0.5408, 0.0632, 3.1048, -0.2622],
    [-0.7703, 0.9417, -1.2391, 0.7852, 0.4816],
    [-0.4144, 1.2947, 0.2032, -2.6475, 1.5505]
]
b_vec = [1.766, 2.0691, 2.6064, -0.4434]

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
                   options={"tracefname": "convex4_5_4.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
