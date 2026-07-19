import bam

N = 5
M = 4
A_mat = [
    [-0.8347, -0.805, -0.2696, -1.3795, 0.6384],
    [-0.7528, -0.4496, 0.8867, 0.8217, -0.981],
    [0.3503, -1.5268, -0.6727, 0.4686, 1.4145],
    [-0.161, 0.6239, -0.3824, -4.5906, -0.6068]
]
b_vec = [2.0954, 0.9168, 1.9135, 0.7937]

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
                   options={"tracefname": "convex4_5_3.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
