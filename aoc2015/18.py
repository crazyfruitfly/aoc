import numpy as np

def readup(fn):
    m = [[0]*102]
    with open(fn, 'r') as f:
        for l in f.readlines():
            m.append([0] + [1 if x == '#' else 0 for x in l.strip()] + [0])
    m.append([0]*102)
    return np.array(m)

def printm(m):
    for i in range(1, len(m)-1):
        for j in range(1, len(m[i]) -1):
            a = '.' if m[i][j] == 0 else '#'
            print(a, end='')
        print()

def sim(m, steps):
    for _ in range(steps):
        nm = np.zeros((len(m), len(m[0])))
        
        for i in range(1, len(m)-1):
            for j in range(1, len(m[i]) -1):
                neighs = [(i-1, j-1), (i-1, j), (i-1, j+1),
                          (i, j-1), (i, j+1),
                          (i+1, j-1), (i+1, j), (i+1, j+1)]
                s = sum([m[x[0]][x[1]] for x in neighs])
                if m[i][j] == 1:
                    nm[i][j] = 1 if s in [2,3] else 0
                else:
                    nm[i][j] = 1 if s == 3 else 0
        m = nm
    printm(m)
    return m

def sim2(m, steps):
    for _ in range(steps):
        m[1,1],m[1,100],m[1][100],m[100][100] = 1,1,1,1
        nm = np.zeros((len(m), len(m[0])))
        
        for i in range(1, len(m)-1):
            for j in range(1, len(m[i]) -1):
                neighs = [(i-1, j-1), (i-1, j), (i-1, j+1),
                          (i, j-1), (i, j+1),
                          (i+1, j-1), (i+1, j), (i+1, j+1)]
                s = sum([m[x[0]][x[1]] for x in neighs])
                if (i,j) in [(1,1),(1, 100), (100,1), (100,100)]:
                    nm[i][j] = 1
                elif m[i][j] == 1:
                    nm[i][j] = 1 if s in [2,3] else 0
                else:
                    nm[i][j] = 1 if s == 3 else 0
        m = nm
    m[1,1],m[1,100],m[1][100],m[100][100] = 1,1,1,1
    printm(m)
    return m

lights = readup('18.in')
m = sim2(lights, 100)
print(np.sum(m))