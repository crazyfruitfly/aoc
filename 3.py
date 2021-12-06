import pprint
import numpy as np

pp = pprint.PrettyPrinter(indent = 2)

m = {'up': -1, 'down': 1}

def readup(fn):
    with open(fn, 'r') as f:
        return np.array([[int(k) for k in i if k.strip()] for i in f.readlines()])

def f_1(m):
    g, e, s = '', '', len(m) / 2
    for r in m.transpose():
        g += '1' if sum(r) >= s else '0'
        e += '1' if s > sum(r) else '0'
    print(int(g, 2) * int(e, 2))

def f_2(m, c, scubber = False):
    if len(m) > 1:
        t = m.transpose()
        nm = []
        if not scubber:
            item = 1 if sum(t[c]) >= len(m) / 2 else 0
        else:
            item = 1 if sum(t[c]) < len(m) / 2 else 0
        indexes = np.where(t[c] == item)
        for i in indexes[0]:
            nm.append(m[i])
        nnpm = np.array(nm)

        return f_2(nnpm, c + 1, scubber)
    else:
        return int(''.join([str(x) for x in m[0]]), 2)

testm = readup('test3.in')
f_1(testm)
oxygen = f_2(testm, 0, scubber = False)
scubber = f_2(testm, 0, scubber = True)
print(oxygen)
print(scubber)
print(oxygen * scubber)
print('-----------------')
m = readup('3.in')
f_1(m)
oxygen = f_2(m, 0, scubber = False)
scubber = f_2(m, 0, scubber = True)
print(oxygen)
print(scubber)
print(oxygen * scubber)