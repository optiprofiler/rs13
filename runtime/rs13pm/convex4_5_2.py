import bam

N = 5
M = 4
A_mat = [
    [-1.2363, -0.0681, 1.1726, 3.1623, 0.0863],
    [-0.1108, 1.3512, 1.7164, 0.9851, -0.0843],
    [0.7784, -1.2521, 0.1707, 2.6314, 0.6434],
    [-1.1901, 0.1128, 2.008, -1.6134, -0.5331]
]
b_vec = [4.2427, 1.3269, 3.611, 1.4336]

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
                   options={"tracefname": "convex4_5_2.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
