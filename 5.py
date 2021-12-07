import pprint
import numpy as np

pp = pprint.PrettyPrinter(indent = 2)

def generate_linecoords2(start, end):
    coords = []
    sx, sy = start[0], start[1]
    diffx = -1 if sx > end[0] else 1 if sx < end[0] else 0
    diffy = -1 if sy > end[1] else 1 if sy < end[1] else 0
    while not (sx == end[0] and sy == end[1]):
        coords.append( [sx, sy] )
        sx += diffx
        sy += diffy
    coords.append(end)
    return coords

def generate_linecoords( start, end ):
    coords = []
    if start[1] == end[1]:
        s, e = max(start[0], end[0]), min(start[0], end[0])
        while s >= e:
            coords.append( [e, start[1]] )
            e += 1
    elif start[0] == end[0]:
        s, e = max(start[1], end[1]), min(start[1], end[1])
        while s >= e:   
            coords.append( [start[0], e] )
            e += 1
    else:
        sx, sy = start[0], start[1]
        diffx = -1 if sx > end[0] else 1 if sx < end[0] else 0
        diffy = -1 if sx > end[1] else 1 if sy < end[1] else 0
        while sx != end[0] and sy != end[1]:
            coords.append( [sx, sy] )
            sx += diffx
            sy += diffy
        coords.append(end)
    return coords

def readup(fn):
    lines = []
    with open(fn, 'r') as f:
        for x in f.readlines():
            row = x.split()
            lines.append( ([int(x) for x in row[0].split(',')], [int(x) for x in row[-1].split(',')]) )
    maxx = max([max(x[0][0], x[1][0]) for x in lines])
    maxy = max([max(x[0][1], x[1][1]) for x in lines])
    field = np.zeros((maxy + 1, maxx + 1))
    for line in lines:
        #comment for #2
        #if line[0][0] != line[1][0] and line[0][1] != line[1][1]:
        #    continue
    
        coords = generate_linecoords2(line[0], line[1])
        for item in coords:
            field[item[1]][item[0]] = field[item[1]][item[0]] + 1
    return field

def count(field):
    pp.pprint(field)
    print(np.count_nonzero(field > 1))
    

field = readup('test5.in')
count(field)
print('-------------------------------')
field = readup('5.in')
count(field)