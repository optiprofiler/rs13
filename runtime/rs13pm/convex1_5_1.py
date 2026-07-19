import bam
import math

N = 5
TWON = 10
a_mat = [
    [62.9447, -80.4919, -68.4774, -71.6227, 31.1481, -62.9447, 80.4919, 68.4774, 71.6227, -31.1481],
    [81.1584, -44.3004, 94.1186, -15.6477, -92.8577, -81.1584, 44.3004, -94.1186, 15.6477, 92.8577],
    [-74.6026, 9.3763, 91.4334, 83.1471, 69.8259, 74.6026, -9.3763, -91.4334, -83.1471, -69.8259],
    [82.6752, 91.5014, -2.9249, 58.4415, 86.7986, -82.6752, -91.5014, 2.9249, -58.4415, -86.7986],
    [26.4718, 92.9777, 60.0561, 91.8985, 35.747, -26.4718, -92.9777, -60.0561, -91.8985, -35.747]
]

def objective(x):
    f = 0.0
    i = 0.0
    j = 0.0
    fval = 0.0
    ftemp = 0.0
    for i in range(0, TWON):
        ftemp = 0.0
        for j in range(0, N):
            ftemp += a_mat[j][i] * x[j]
        if math.fabs(ftemp) > fval:
            fval = math.fabs(ftemp)
    f = fval
    return f


xmin = [-5000, -5000, -5000, -5000, -5000]
xmax = [10000, 10000, 10000, 10000, 10000]
x0 = [0, 0, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "convex1_5_1.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
