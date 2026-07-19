import bam

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
def _cm_log(a):
    if a < 0.0:
        return _NAN
    if a == 0.0:
        return -_INF
    return _math.log(a)

def objective(x):
    f = 0.0
    _labels = {
        'L1': 25,
        'L3': 51,
        'L5': 75,
        'L7': 102,
        'L9': 118,
        'L11': 129,
        'L13': 139,
        'L15': 148,
        'L16': 151,
        'L14': 152,
        'L12': 153,
        'L10': 154,
        'L8': 155,
        'L6': 156,
        'L4': 157,
        'L2': 158,
    }
    _pc = 0
    _n_instr = 160
    while _pc < _n_instr:
        if _pc == 0:
            v = [0.0] * (10)
            _pc += 1
            continue
        if _pc == 1:
            v[0] = -10. + x[0]
            _pc += 1
            continue
        if _pc == 2:
            v[1] = _cm_pow(v[0], 3.)
            _pc += 1
            continue
        if _pc == 3:
            v[0] = -20. + x[1]
            _pc += 1
            continue
        if _pc == 4:
            v[2] = _cm_pow(v[0], 3.)
            _pc += 1
            continue
        if _pc == 5:
            v[1] += v[2]
            _pc += 1
            continue
        if _pc == 6:
            v[2] = -5. + x[0]
            _pc += 1
            continue
        if _pc == 7:
            v[0] = v[2] * v[2]
            _pc += 1
            continue
        if _pc == 8:
            v[2] = -v[0]
            _pc += 1
            continue
        if _pc == 9:
            v[0] = -5. + x[1]
            _pc += 1
            continue
        if _pc == 10:
            v[3] = v[0] * v[0]
            _pc += 1
            continue
        if _pc == 11:
            v[0] = v[2] - v[3]
            _pc += 1
            continue
        if _pc == 12:
            v[2] = 201. + v[0]
            _pc += 1
            continue
        if _pc == 13:
            if v[2] > 0.:
                _pc = _labels['L1']
            else:
                _pc += 1
            continue
        if _pc == 14:
            v[2] = -5. + x[0]
            _pc += 1
            continue
        if _pc == 15:
            v[0] = v[2] * v[2]
            _pc += 1
            continue
        if _pc == 16:
            v[2] = -v[0]
            _pc += 1
            continue
        if _pc == 17:
            v[0] = -5. + x[1]
            _pc += 1
            continue
        if _pc == 18:
            v[3] = v[0] * v[0]
            _pc += 1
            continue
        if _pc == 19:
            v[0] = v[2] - v[3]
            _pc += 1
            continue
        if _pc == 20:
            v[2] = 200. + v[0]
            _pc += 1
            continue
        if _pc == 21:
            v[0] = v[2] * v[2]
            _pc += 1
            continue
        if _pc == 22:
            v[2] = 1.e+10 * v[0]
            _pc += 1
            continue
        if _pc == 23:
            v[3] = v[2]
            _pc += 1
            continue
        if _pc == 24:
            _pc = _labels['L2']
            continue
        if _pc == 25:
            v[2] = -5. + x[0]
            _pc += 1
            continue
        if _pc == 26:
            v[0] = v[2] * v[2]
            _pc += 1
            continue
        if _pc == 27:
            v[2] = -v[0]
            _pc += 1
            continue
        if _pc == 28:
            v[0] = -5. + x[1]
            _pc += 1
            continue
        if _pc == 29:
            v[3] = v[0] * v[0]
            _pc += 1
            continue
        if _pc == 30:
            v[0] = v[2] - v[3]
            _pc += 1
            continue
        if _pc == 31:
            v[2] = 201. + v[0]
            _pc += 1
            continue
        if _pc == 32:
            v[0] = _cm_log(v[2])
            _pc += 1
            continue
        if _pc == 33:
            v[2] = -v[0]
            _pc += 1
            continue
        if _pc == 34:
            v[0] = -5. + x[0]
            _pc += 1
            continue
        if _pc == 35:
            v[3] = v[0] * v[0]
            _pc += 1
            continue
        if _pc == 36:
            v[0] = -5. + x[1]
            _pc += 1
            continue
        if _pc == 37:
            v[4] = v[0] * v[0]
            _pc += 1
            continue
        if _pc == 38:
            v[0] = v[3] + v[4]
            _pc += 1
            continue
        if _pc == 39:
            v[3] = -99. + v[0]
            _pc += 1
            continue
        if _pc == 40:
            if v[3] > 0.:
                _pc = _labels['L3']
            else:
                _pc += 1
            continue
        if _pc == 41:
            v[3] = -5. + x[0]
            _pc += 1
            continue
        if _pc == 42:
            v[0] = v[3] * v[3]
            _pc += 1
            continue
        if _pc == 43:
            v[3] = -5. + x[1]
            _pc += 1
            continue
        if _pc == 44:
            v[4] = v[3] * v[3]
            _pc += 1
            continue
        if _pc == 45:
            v[3] = v[0] + v[4]
            _pc += 1
            continue
        if _pc == 46:
            v[0] = -100. + v[3]
            _pc += 1
            continue
        if _pc == 47:
            v[3] = v[0] * v[0]
            _pc += 1
            continue
        if _pc == 48:
            v[0] = 1.e+10 * v[3]
            _pc += 1
            continue
        if _pc == 49:
            v[5] = v[0]
            _pc += 1
            continue
        if _pc == 50:
            _pc = _labels['L4']
            continue
        if _pc == 51:
            v[0] = -5. + x[0]
            _pc += 1
            continue
        if _pc == 52:
            v[3] = v[0] * v[0]
            _pc += 1
            continue
        if _pc == 53:
            v[0] = -5. + x[1]
            _pc += 1
            continue
        if _pc == 54:
            v[4] = v[0] * v[0]
            _pc += 1
            continue
        if _pc == 55:
            v[0] = v[3] + v[4]
            _pc += 1
            continue
        if _pc == 56:
            v[3] = -99. + v[0]
            _pc += 1
            continue
        if _pc == 57:
            v[0] = _cm_log(v[3])
            _pc += 1
            continue
        if _pc == 58:
            v[3] = -v[0]
            _pc += 1
            continue
        if _pc == 59:
            v[0] = -5. + x[1]
            _pc += 1
            continue
        if _pc == 60:
            v[4] = v[0] * v[0]
            _pc += 1
            continue
        if _pc == 61:
            v[4] += 1.
            _pc += 1
            continue
        if _pc == 62:
            v[0] = -6. + x[0]
            _pc += 1
            continue
        if _pc == 63:
            v[5] = v[0] * v[0]
            _pc += 1
            continue
        if _pc == 64:
            v[4] += v[5]
            _pc += 1
            continue
        if _pc == 65:
            if v[4] > 0.:
                _pc = _labels['L5']
            else:
                _pc += 1
            continue
        if _pc == 66:
            v[4] = -5. + x[1]
            _pc += 1
            continue
        if _pc == 67:
            v[5] = v[4] * v[4]
            _pc += 1
            continue
        if _pc == 68:
            v[4] = -6. + x[0]
            _pc += 1
            continue
        if _pc == 69:
            v[0] = v[4] * v[4]
            _pc += 1
            continue
        if _pc == 70:
            v[4] = v[5] + v[0]
            _pc += 1
            continue
        if _pc == 71:
            v[5] = v[4] * v[4]
            _pc += 1
            continue
        if _pc == 72:
            v[4] = 1.e+10 * v[5]
            _pc += 1
            continue
        if _pc == 73:
            v[0] = v[4]
            _pc += 1
            continue
        if _pc == 74:
            _pc = _labels['L6']
            continue
        if _pc == 75:
            v[4] = -5. + x[1]
            _pc += 1
            continue
        if _pc == 76:
            v[5] = v[4] * v[4]
            _pc += 1
            continue
        if _pc == 77:
            v[5] += 1.
            _pc += 1
            continue
        if _pc == 78:
            v[4] = -6. + x[0]
            _pc += 1
            continue
        if _pc == 79:
            v[0] = v[4] * v[4]
            _pc += 1
            continue
        if _pc == 80:
            v[5] += v[0]
            _pc += 1
            continue
        if _pc == 81:
            v[0] = _cm_log(v[5])
            _pc += 1
            continue
        if _pc == 82:
            v[5] = -v[0]
            _pc += 1
            continue
        if _pc == 83:
            v[0] = -5. + x[1]
            _pc += 1
            continue
        if _pc == 84:
            v[4] = v[0] * v[0]
            _pc += 1
            continue
        if _pc == 85:
            v[0] = -v[4]
            _pc += 1
            continue
        if _pc == 86:
            v[4] = -6. + x[0]
            _pc += 1
            continue
        if _pc == 87:
            v[6] = v[4] * v[4]
            _pc += 1
            continue
        if _pc == 88:
            v[4] = v[0] - v[6]
            _pc += 1
            continue
        if _pc == 89:
            v[0] = 83.81 + v[4]
            _pc += 1
            continue
        if _pc == 90:
            if v[0] > 0.:
                _pc = _labels['L7']
            else:
                _pc += 1
            continue
        if _pc == 91:
            v[0] = -5. + x[1]
            _pc += 1
            continue
        if _pc == 92:
            v[4] = v[0] * v[0]
            _pc += 1
            continue
        if _pc == 93:
            v[0] = -v[4]
            _pc += 1
            continue
        if _pc == 94:
            v[4] = -6. + x[0]
            _pc += 1
            continue
        if _pc == 95:
            v[6] = v[4] * v[4]
            _pc += 1
            continue
        if _pc == 96:
            v[4] = v[0] - v[6]
            _pc += 1
            continue
        if _pc == 97:
            v[0] = 82.81 + v[4]
            _pc += 1
            continue
        if _pc == 98:
            v[4] = v[0] * v[0]
            _pc += 1
            continue
        if _pc == 99:
            v[0] = 1.e+10 * v[4]
            _pc += 1
            continue
        if _pc == 100:
            v[4] = v[0]
            _pc += 1
            continue
        if _pc == 101:
            _pc = _labels['L8']
            continue
        if _pc == 102:
            v[0] = -5. + x[1]
            _pc += 1
            continue
        if _pc == 103:
            v[4] = v[0] * v[0]
            _pc += 1
            continue
        if _pc == 104:
            v[0] = -v[4]
            _pc += 1
            continue
        if _pc == 105:
            v[4] = -6. + x[0]
            _pc += 1
            continue
        if _pc == 106:
            v[6] = v[4] * v[4]
            _pc += 1
            continue
        if _pc == 107:
            v[4] = v[0] - v[6]
            _pc += 1
            continue
        if _pc == 108:
            v[0] = 83.81 + v[4]
            _pc += 1
            continue
        if _pc == 109:
            v[4] = _cm_log(v[0])
            _pc += 1
            continue
        if _pc == 110:
            v[0] = -v[4]
            _pc += 1
            continue
        if _pc == 111:
            v[4] = -x[0]
            _pc += 1
            continue
        if _pc == 112:
            v[6] = 101. + v[4]
            _pc += 1
            continue
        if _pc == 113:
            if v[6] > 0.:
                _pc = _labels['L9']
            else:
                _pc += 1
            continue
        if _pc == 114:
            v[6] = 100. - x[0]
            _pc += 1
            continue
        if _pc == 115:
            v[4] = v[6] * v[6]
            _pc += 1
            continue
        if _pc == 116:
            v[6] = 1.e+10 * v[4]
            _pc += 1
            continue
        if _pc == 117:
            _pc = _labels['L10']
            continue
        if _pc == 118:
            v[6] = -x[0]
            _pc += 1
            continue
        if _pc == 119:
            v[4] = 101. + v[6]
            _pc += 1
            continue
        if _pc == 120:
            v[6] = _cm_log(v[4])
            _pc += 1
            continue
        if _pc == 121:
            v[4] = -v[6]
            _pc += 1
            continue
        if _pc == 122:
            v[6] = -12. + x[0]
            _pc += 1
            continue
        if _pc == 123:
            if v[6] > 0.:
                _pc = _labels['L11']
            else:
                _pc += 1
            continue
        if _pc == 124:
            v[6] = -13. + x[0]
            _pc += 1
            continue
        if _pc == 125:
            v[7] = v[6] * v[6]
            _pc += 1
            continue
        if _pc == 126:
            v[6] = 1.e+10 * v[7]
            _pc += 1
            continue
        if _pc == 127:
            v[7] = v[6]
            _pc += 1
            continue
        if _pc == 128:
            _pc = _labels['L12']
            continue
        if _pc == 129:
            v[6] = -12. + x[0]
            _pc += 1
            continue
        if _pc == 130:
            v[7] = _cm_log(v[6])
            _pc += 1
            continue
        if _pc == 131:
            v[6] = -v[7]
            _pc += 1
            continue
        if _pc == 132:
            v[7] = -x[1]
            _pc += 1
            continue
        if _pc == 133:
            v[8] = 101. + v[7]
            _pc += 1
            continue
        if _pc == 134:
            if v[8] > 0.:
                _pc = _labels['L13']
            else:
                _pc += 1
            continue
        if _pc == 135:
            v[8] = 100. - x[1]
            _pc += 1
            continue
        if _pc == 136:
            v[7] = v[8] * v[8]
            _pc += 1
            continue
        if _pc == 137:
            v[8] = 1.e+10 * v[7]
            _pc += 1
            continue
        if _pc == 138:
            _pc = _labels['L14']
            continue
        if _pc == 139:
            v[8] = -x[1]
            _pc += 1
            continue
        if _pc == 140:
            v[7] = 101. + v[8]
            _pc += 1
            continue
        if _pc == 141:
            v[8] = _cm_log(v[7])
            _pc += 1
            continue
        if _pc == 142:
            v[7] = -v[8]
            _pc += 1
            continue
        if _pc == 143:
            v[8] = 1. + x[1]
            _pc += 1
            continue
        if _pc == 144:
            if v[8] > 0.:
                _pc = _labels['L15']
            else:
                _pc += 1
            continue
        if _pc == 145:
            v[8] = x[1] * x[1]
            _pc += 1
            continue
        if _pc == 146:
            v[9] = 1.e+10 * v[8]
            _pc += 1
            continue
        if _pc == 147:
            _pc = _labels['L16']
            continue
        if _pc == 148:
            v[9] = 1. + x[1]
            _pc += 1
            continue
        if _pc == 149:
            v[8] = _cm_log(v[9])
            _pc += 1
            continue
        if _pc == 150:
            v[9] = -v[8]
            _pc += 1
            continue
        if _pc == 151:
            v[8] = v[7] + v[9]
            _pc += 1
            continue
        if _pc == 152:
            v[7] = v[6] + v[8]
            _pc += 1
            continue
        if _pc == 153:
            v[6] = v[4] + v[7]
            _pc += 1
            continue
        if _pc == 154:
            v[4] = v[0] + v[6]
            _pc += 1
            continue
        if _pc == 155:
            v[0] = v[5] + v[4]
            _pc += 1
            continue
        if _pc == 156:
            v[5] = v[3] + v[0]
            _pc += 1
            continue
        if _pc == 157:
            v[3] = v[2] + v[5]
            _pc += 1
            continue
        if _pc == 158:
            v[1] += v[3]
            _pc += 1
            continue
        if _pc == 159:
            f = v[1]
            _pc += 1
            continue
    return f


xmin = [-10000, -10000]
xmax = [10000, 10000]
x0 = [0, 0]

res = bam.minimize(objective, x0=x0,
                   bounds=list(zip(xmin, xmax)),
                   options={"tracefname": "djtl.trc"})

print("Status = %d" % res.status)
print("Best f = %.15e" % res.fun)
print("Best x = " + "".join("%.15e " % xi for xi in res.x))
