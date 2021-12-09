import numpy as np

def readup(fn):
    with open(fn, 'r') as f:
        return f.read().strip()


def f_1(dirs):
    houses = [(0,0)]
    for i in dirs:
        if i == '<' : houses.append( (houses[-1][0] -1, houses[-1][1] ) )
        elif i == '>' : houses.append( (houses[-1][0] +1, houses[-1][1] ) )
        elif i == '^' : houses.append( (houses[-1][0], houses[-1][1] + 1) )
        elif i == 'v' : houses.append( (houses[-1][0], houses[-1][1] - 1) )
    print(len(set(houses)))


def f_2(dirs):
    santa_houses = [(0,0)]
    robostanta_houses = [(0,0)]
    counter = 1
    for i in dirs:
        if counter % 2 == 1:
            houses = santa_houses
        else:
            houses = robostanta_houses
        if i == '<' : houses.append( (houses[-1][0] -1, houses[-1][1] ) )
        elif i == '>' : houses.append( (houses[-1][0] +1, houses[-1][1] ) )
        elif i == '^' : houses.append( (houses[-1][0], houses[-1][1] + 1) )
        elif i == 'v' : houses.append( (houses[-1][0], houses[-1][1] - 1) )
        counter += 1
    
    print(len(set(set(santa_houses).union(set(robostanta_houses)))))

dirs = readup('3.in')
f_1(dirs)
f_2(dirs)