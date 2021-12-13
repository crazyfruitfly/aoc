import numpy as np
import matplotlib.pyplot as plt


def readup(fn):
    folds = []
    coords = []
    with open(fn, 'r') as f:
        for l in f.readlines():
            if l.startswith('fold'):
                fold = l.strip().split()[-1].split('=')
                folds.append( (fold[0], int(fold[1])) )
            elif l.strip():
                coord = l.strip().split(',')
                coords.append( (int(coord[0]), int(coord[1])) )
    return folds, coords

def init_matrix(coords):
    width = max([x[0] + 1 for x in coords])
    height = max([x[1] + 1  for x in coords])
    m = np.zeros( (height, width) )
    for coord in coords:
        m[coord[1]][coord[0]] = 1
    return m

def fold_up(m, line):
    for x in range(line + 1, len(m)):
        for y in range(len(m[x])):
            if m[x][y] > 0:
                newx = line-(x-line)
                m[newx][y] += m[x][y]
    return m[:line]

def fold_left(m, line):
    for x in range(len(m)):
        for y in range(line+1, len(m[x])):
            if m[x][y] > 0:
                newy = line-(y-line)
                m[x][newy] += m[x][y]
    return m[:,:line]

def calc(m):
    print(np.count_nonzero(m))

def printm(m):
    for row in m:
        print(''.join(['.' if x == 0 else '#' for x in row]))

fs = {'x': fold_left, 'y': fold_up}
#fs = {'x': fold_left, 'y': fold_up}


folds, coords = readup('13.in')
m = init_matrix(coords)
for f in folds:
    m = fs[f[0]](m, f[1])
    #break
printm(m)
calc(m)
