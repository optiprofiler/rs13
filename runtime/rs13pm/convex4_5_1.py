import bam

N = 5
M = 4
A_mat = [
    [-0.4876, -2.2297, 2.6109, 3.5728, 0.0254],
    [0.7657, -1.0439, -0.9953, -0.9634, 0.2699],
    [0.9813, 1.9977, 2.5475, 2.4311, -0.6591],
    [0.0094, -1.5107, -0.8282, 0.7574, 0.4198]
]
b_vec = [3.1864, 0.2809, 1.1892, 1.6148]

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
                   options={"tracefname": "convex4_5_1.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
