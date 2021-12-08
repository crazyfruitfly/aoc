import requests, pprint

pp = pprint.PrettyPrinter(indent = 2)

m = {'up': -1, 'down': 1}

def readup(fn):
    with open(fn, 'r') as f:
        l = [(i.split()[0], int(i.split()[1].strip())) for i in f.readlines()]
        return l

def f_1(l):
    hpos = 0
    vpos = 0
    for i in l:
        hpos += 0 if i[0] in m else i[1]
        vpos += 0 if i[0] not in m else m[i[0]] * i[1]
    print(hpos, vpos)
    print(hpos*vpos)

def f_2(l):
    hpos = 0
    vpos = 0
    aim = 0
    for i in l:
        hpos, vpos = (hpos, vpos) if i[0] in m else (hpos + i[1], vpos + (aim * i[1]))
        aim += 0 if i[0] not in m else m[i[0]] * i[1]
    print(hpos*vpos)

testl = readup('test2.in')
f_1(testl)
f_2(testl)
l = readup('2.in')
f_1(l)
f_2(l)