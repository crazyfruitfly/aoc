import numpy as np

def readup(fn):
    items = []
    with open(fn, 'r') as f:
        for r in f.readlines():
            items.append([int(i) for i in r.strip()])
    return np.array(items)

def f_1(m):
    pmaxrisk = len(m) * len(m[0]) * 10
    risks = np.array([[pmaxrisk] *len(m)] * len(m[0]))
    print(risks.shape)
    risks[0][0] = 0
    risks[0][1] = m[0][1]
    risks[1][0] = m[1][0]
    while True:
        changed = False
        for i in range(len(m)):
            for j in range(len(m[i])):
                n = [x for x in [ (i + 1, j), (i - 1, j), (i, j + 1), (i, j-1)] if 0 <= x[0] < len(m) and 0 <= x[1] < len(m[0])]
                for k in n:
                    if risks[k[0]][k[1]] < pmaxrisk:
                        risk = m[i][j] + risks[k[0]][k[1]]
                        if risks[i][j] > risk:
                            changed = True
                            risks[i][j] = risk
        if not changed:
            break
    print(risks[-1][-1])

def add_one(m):
    nm = m + 1
    return np.where(nm == 10, 1, nm)

def generate_row(m):
    row = [m]
    for i in range(4):
        row.append(add_one(row[-1]))
    nm = row[0]
    for i in row[1:]:
        nm = np.concatenate((nm, i), axis=1)
    return nm


def generate_bigtile(m):
    row = [m]
    for i in range(4):
        row.append(add_one(row[-1]))
    
    nm = generate_row(row[0])
    for i in row[1:]:
        nm = np.concatenate((nm, generate_row(i)), axis=0)
    return nm


def f_2(m):
    print(m)
    nm = generate_bigtile(m)
    f_1(nm)


om = readup('test15.in')
f_1(om)
f_2(om)