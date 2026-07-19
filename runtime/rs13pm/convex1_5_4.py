import bam
import math

N = 5
TWON = 10
a_mat = [
    [-51.6617, 91.2269, 64.2388, 46.3445, 48.9386, 51.6617, -91.2269, -64.2388, -46.3445, -48.9386],
    [-19.2176, 15.0417, -96.9193, 29.5492, -62.209, 19.2176, -15.0417, 96.9193, -29.5492, 62.209],
    [-80.7091, -88.0441, -91.3952, -9.8153, 37.3551, 80.7091, 88.0441, 91.3952, 9.8153, -37.3551],
    [-73.6053, -53.044, -66.202, 9.4018, -63.2978, 73.6053, 53.044, 66.202, -9.4018, 63.2978],
    [88.4101, -29.3683, 29.8231, -40.7358, -26.3031, -88.4101, 29.3683, -29.8231, 40.7358, 26.3031]
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
                   options={"tracefname": "convex1_5_4.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
