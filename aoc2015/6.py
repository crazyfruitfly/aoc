import numpy as np

def turnon(m, fromxy, toxy):
    for i in range(fromxy[0], toxy[0] + 1):
        for j in range(fromxy[1], toxy[1] + 1):
            m[i][j] = True
    return m

def turnoff(m, fromxy, toxy):
    for i in range(fromxy[0], toxy[0] + 1):
        for j in range(fromxy[1], toxy[1] + 1):
            m[i][j] = False
    return m


def toggle(m, fromxy, toxy):
    for i in range(fromxy[0], toxy[0] + 1):
        for j in range(fromxy[1], toxy[1] + 1):
            m[i][j] = not m[i][j]
    return m


def turnon2(m, fromxy, toxy):
    for i in range(fromxy[0], toxy[0] + 1):
        for j in range(fromxy[1], toxy[1] + 1):
            m[i][j] = m[i][j] + 1
    return m

def turnoff2(m, fromxy, toxy):
    for i in range(fromxy[0], toxy[0] + 1):
        for j in range(fromxy[1], toxy[1] + 1):
            m[i][j] = 0 if m[i][j] == 0 else m[i][j] - 1
    return m


def toggle2(m, fromxy, toxy):
    for i in range(fromxy[0], toxy[0] + 1):
        for j in range(fromxy[1], toxy[1] + 1):
            m[i][j] = m[i][j] + 2
    return m


def readup(fn):
    commands = []
    with open(fn, 'r') as f:
        for line in f.readlines():
            line = line.strip().split()
            cmd = ''
            fromconrer = None
            tocorner = None
            if line[0] == 'turn':
                cmd = line[1]
                fromcorner = (int(line[2].split(',')[0]), int(line[2].split(',')[1]))
                tocorner = (int(line[-1].split(',')[0]), int(line[-1].split(',')[1]))
            else:
                cmd = line[0]
                fromcorner = (int(line[1].split(',')[0]), int(line[1].split(',')[1]))
                tocorner = (int(line[-1].split(',')[0]), int(line[-1].split(',')[1]))
            commands.append( (cmd, fromcorner, tocorner) )
    return commands


def sim(commands):
    m = np.zeros( (1000,1000), dtype=bool)
    for item in commands:
        m = functions[item[0]](m, item[1], item[2])
    print(np.count_nonzero(m))

def sim2(commands):
    m = np.zeros( (1000,1000))
    for item in commands:
        m = functions2[item[0]](m, item[1], item[2])
    print(np.sum(m))

functions = {'on': turnon, 'off': turnoff, 'toggle': toggle}
functions2 = {'on': turnon2, 'off': turnoff2, 'toggle': toggle2}
commands = readup('6.in')
sim(commands)
sim2(commands)