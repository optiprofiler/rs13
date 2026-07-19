import bam
import math

import math as _math
_INF = float('inf')
_NAN = float('nan')
def _cm_pow(a, b):
    try:
        return _math.pow(a, b)
    except OverflowError:
        return _INF
    except ValueError:
        return _NAN

def _post(_v, _name, _delta):
    _old = _v.get(_name, 0)
    _v[_name] = _old + _delta
    return _old

def objective(xin):
    fout = 0.0
    _v = {}
    bam_idx = 0
    nx = 15
    nk = 5
    x = [0.0] * (nx + 1)
    z = [0.0] * (nk + 1)
    w = [0.0] * (nx + 1)
    Y = [0.0] * (95 + 1)
    objvar = 0.0
    tmp = 0.0
    i = 0.0
    k = 0.0
    _init_Y = [-16e0,0e0,-3.5e0,0e0,0e0,2e0,-1e0,-1e0,1e0,1e0,2e0,-2e0,0e0,-2e0,-9e0,0e0,-1e0,-2e0,2e0,1e0,0e0,0e0,2e0,0e0,-2e0,-4e0,-1e0,-3e0,3e0,1e0,1e0,4e0,0e0,-4e0,1e0,0e0,-1e0,-2e0,4e0,1e0,0e0,2e0,0e0,-1e0,-2.8e0,0e0,-1e0,-1e0,5e0,1e0,-40e0,-2e0,-0.25e0,-4e0,-4e0,-1e0,-40e0,-60e0,5e0,1e0,30e0,-20e0,-10e0,32e0,-10e0,-20e0,39e0,-6e0,-31e0,32e0,-10e0,-6e0,10e0,-6e0,-10e0,32e0,-31e0,-6e0,39e0,-20e0,-10e0,32e0,-10e0,-20e0,30e0,4e0,8e0,10e0,6e0,2e0,-15e0,-27e0,-36e0,-18e0,-12e0]
    _k = 0.0
    for _k in range(0, 95):
        Y[_k + 1] = _init_Y[_k]
    for i in range(1, (nx) + 1):
        x[i] = xin[_post(_v, 'bam_idx', 1)]
    z[1] = max(-3e0 * Y[86] * _cm_pow(x[1], 2) - Y[91] - 2e0 * (Y[61] * x[1] + Y[62] * x[2] + Y[63] * x[3] + Y[64] * x[4] + Y[65] * x[5]) + Y[1] * x[6] + Y[2] * x[7] + Y[3] * x[8] + Y[4] * x[9] + Y[5] * x[10] + Y[6] * x[11] + Y[7] * x[12] + Y[8] * x[13] + Y[9] * x[14] + Y[10] * x[15], 0e0)
    z[2] = max(-3e0 * Y[87] * _cm_pow(x[2], 2) - Y[92] - 2e0 * (Y[66] * x[1] + Y[67] * x[2] + Y[68] * x[3] + Y[69] * x[4] + Y[70] * x[5]) + Y[11] * x[6] + Y[12] * x[7] + Y[13] * x[8] + Y[14] * x[9] + Y[15] * x[10] + Y[16] * x[11] + Y[17] * x[12] + Y[18] * x[13] + Y[19] * x[14] + Y[20] * x[15], 0e0)
    z[3] = max(-3e0 * Y[88] * _cm_pow(x[3], 2) - Y[93] - 2e0 * (Y[71] * x[1] + Y[72] * x[2] + Y[73] * x[3] + Y[74] * x[4] + Y[75] * x[5]) + Y[21] * x[6] + Y[22] * x[7] + Y[23] * x[8] + Y[24] * x[9] + Y[25] * x[10] + Y[26] * x[11] + Y[27] * x[12] + Y[28] * x[13] + Y[29] * x[14] + Y[30] * x[15], 0e0)
    z[4] = max(-3e0 * Y[89] * _cm_pow(x[4], 2) - Y[94] - 2e0 * (Y[76] * x[1] + Y[77] * x[2] + Y[78] * x[3] + Y[79] * x[4] + Y[80] * x[5]) + Y[31] * x[6] + Y[32] * x[7] + Y[33] * x[8] + Y[34] * x[9] + Y[35] * x[10] + Y[36] * x[11] + Y[37] * x[12] + Y[38] * x[13] + Y[39] * x[14] + Y[40] * x[15], 0e0)
    z[5] = max(-3e0 * Y[90] * _cm_pow(x[5], 2) - Y[95] - 2e0 * (Y[81] * x[1] + Y[82] * x[2] + Y[83] * x[3] + Y[84] * x[4] + Y[85] * x[5]) + Y[41] * x[6] + Y[42] * x[7] + Y[43] * x[8] + Y[44] * x[9] + Y[45] * x[10] + Y[46] * x[11] + Y[47] * x[12] + Y[48] * x[13] + Y[49] * x[14] + Y[50] * x[15], 0e0)
    for i in range(1, (nx) + 1):
        w[i] = min(x[i], 0e0)
    objvar = math.fabs(2e0 * (Y[86] * _cm_pow(x[1], 3) + Y[87] * _cm_pow(x[2], 3) + Y[88] * _cm_pow(x[3], 3) + Y[89] * _cm_pow(x[4], 3) + Y[90] * _cm_pow(x[5], 3)))
    objvar = objvar + x[1] * (Y[61] * x[1] + Y[62] * x[2] + Y[63] * x[3] + Y[64] * x[4] + Y[65] * x[5]) + x[2] * (Y[66] * x[1] + Y[67] * x[2] + Y[68] * x[3] + Y[69] * x[4] + Y[70] * x[5]) + x[3] * (Y[71] * x[1] + Y[72] * x[2] + Y[73] * x[3] + Y[74] * x[4] + Y[75] * x[5]) + x[4] * (Y[76] * x[1] + Y[77] * x[2] + Y[78] * x[3] + Y[79] * x[4] + Y[80] * x[5]) + x[5] * (Y[81] * x[1] + Y[82] * x[2] + Y[83] * x[3] + Y[84] * x[4] + Y[85] * x[5])
    for i in range(6, (15) + 1):
        objvar = objvar - Y[45 + i] * x[i]
    for k in range(1, (nk) + 1):
        objvar = objvar + 100e0 * z[k]
    for i in range(1, (nx) + 1):
        objvar = objvar - 100e0 * w[i]
    fout = objvar
    return fout


xmin = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
xmax = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
x0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "problem3.25.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
