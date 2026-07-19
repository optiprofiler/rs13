import bam
import math

N = 5
TWON = 10
a_mat = [
    [-76.2005, -55.2376, 78.1807, -48.4983, 85.8527, 76.2005, 55.2376, -78.1807, 48.4983, -85.8527],
    [-0.3272, 50.2534, 91.8583, 68.1435, -30.0032, 0.3272, -50.2534, -91.8583, -68.1435, 30.0032],
    [91.9488, -48.981, 9.4431, -49.1436, -60.6809, -91.9488, 48.981, -9.4431, 49.1436, 60.6809],
    [-31.9229, 1.1914, -72.2751, 62.857, -49.7832, 31.9229, -1.1914, 72.2751, -62.857, 49.7832],
    [17.0536, 39.8153, -70.1412, -51.295, 23.2089, -17.0536, -39.8153, 70.1412, 51.295, -23.2089]
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
                   options={"tracefname": "convex1_5_2.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
