import bam
import math

N = 5
TWON = 10
a_mat = [
    [-54.8156, 84.6759, -12.226, -47.5577, -40.6648, 54.8156, -84.6759, 12.226, 47.5577, 40.6648],
    [-65.8584, -13.9585, -77.7762, 20.5686, -36.2443, 65.8584, 13.9585, 77.7762, -20.5686, 36.2443],
    [-54.4671, -63.0367, -48.3871, 42.2432, -15.1666, 54.4671, 63.0367, 48.3871, -42.2432, 15.1666],
    [-12.8603, 80.9762, -18.256, -55.6507, 1.5717, 12.8603, -80.9762, 18.256, 55.6507, -1.5717],
    [-37.7795, 95.9497, 18.9792, -76.5165, -82.8968, 37.7795, -95.9497, -18.9792, 76.5165, 82.8968]
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
                   options={"tracefname": "convex1_5_5.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
