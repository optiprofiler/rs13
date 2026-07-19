import bam
import math

N = 5
TWON = 10
a_mat = [
    [37.8429, 82.6675, -84.3649, 54.9821, -48.0259, -37.8429, -82.6675, 84.3649, -54.9821, 48.0259],
    [49.6303, -69.5244, -11.4643, 63.4606, 60.0137, -49.6303, 69.5244, 11.4643, -63.4606, -60.0137],
    [-9.8917, 65.1634, -78.6694, 73.7389, -13.7172, 9.8917, -65.1634, 78.6694, -73.7389, 13.7172],
    [-83.2357, 7.6685, 92.3796, -83.1128, 82.1295, 83.2357, -7.6685, -92.3796, 83.1128, -82.1295],
    [-54.2046, 99.2269, -99.0732, -20.0435, -63.6306, 54.2046, -99.2269, 99.0732, 20.0435, 63.6306]
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
                   options={"tracefname": "convex1_5_3.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
