import itertools

def readup(fn):
    containers = []
    with open(fn, 'r') as f:
        for l in f.readlines():
            containers.append(int(l.strip()))
    return containers

def possibilities(c):
    s = 0
    for i in range(2,len(c)+1):
        for p in itertools.combinations(c, i):
            if sum(p) == 150:
                s += 1
        #print at all iterations so there will be the answer for part 2
        print(s)

def f_1(c):
    sc = set(c)
    possibilities(c)

c = readup('17.in')
f_1(c)