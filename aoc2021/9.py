import numpy as np
import pprint

pp = pprint.PrettyPrinter(indent=2)

def readup(fn):
    hm = []
    with open(fn) as f:
        for l in f.readlines():
            hm.append([int(c) for c in l.strip()])
    return np.array(hm)


def find_lowpoint(hm):
    lowpoints = []
    height = len(hm)
    for i in range(0, height):
        width = len(hm[i])
        for j in range(0, width):
            left = [i, j-1] if j-1 >= 0 else None
            right = [i, j+1] if j+1 < width else None
            top = [i-1, j] if i-1 >= 0 else None
            bottom = [i + 1, j] if i + 1 < height else None
            lowpoint = all([hm[i][j] < hm[x[0]][x[1]] for x in [left, right, top, bottom] if x])
            if lowpoint:
                lowpoints.append( ((i, j), hm[i][j]))
    return lowpoints

def check_neighbour(basins, coord):
    coords = [(coord[0]-1, coord[1]),(coord[0]+1, coord[1]),(coord[0], coord[1]-1),(coord[0], coord[1]+1)]
    if len(basins) == 0:
        basins.append([coord])
        return basins
    else:
        found = -1
        for i in range(0, len(basins)):
            if any([x in coords for x in basins[i]]):
                found = i
        if found > -1:
            basins[found].append(coord)
        else:
            basins.append([coord])
        return basins    

def calc_basin(basin, hm):
    to_append = []
    for x in basin:
        neighbours = [(x[0]-1, x[1]),(x[0]+1, x[1]),(x[0], x[1]-1),(x[0], x[1]+1)]
        neighbours = [c for c in neighbours if 0 <= c[0] < len(hm) and 0 <= c[1] < len(hm[0]) and c not in basin and hm[c[0]][c[1]] != 9]
        to_append.extend(neighbours)
    if len(to_append) > 0:
        basin.extend(list(set(to_append)))
        return calc_basin(basin, hm)
    else:
        return basin

def find_basins(lowpoints, hm):
    basins = []
    for lowpoint in lowpoints:
        basin = calc_basin([lowpoint[0]], hm)
        basins.append(basin)
    return basins

def f_2(basins):
    basins.sort(key=lambda x: len(x))
    b = basins[::-1]
    print(len(b[0]), len(b[1]), len(b[2]))
    print(len(b[0])*len(b[1])*len(b[2]))



def f_1(lowpoints):
    print(sum([x[-1] +1 for x in lowpoints]))



a = readup('9.in')
lowpoints = find_lowpoint(a)
f_1(lowpoints)
basins = find_basins(lowpoints, a)
f_2(basins)