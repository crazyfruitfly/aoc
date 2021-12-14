import re

def readup(fn):
    sl = []
    with open(fn, 'r') as f:
        for l in f.readlines():
            sl.append(l.strip())
    return sl


def f_1(sl):
    s = sum([len(x) for x in sl])
    other = []
    for x in sl:
        y = x[1:-1].replace('\\"', '@')
        y = re.sub(r'\\x[0-9A-Fa-f][0-9A-Fa-f]', '@', y)
        y = y.replace('\\\\', '@')
        #print(x, len(x), y, len(y))
        other.append(y)
    so = sum([len(x) for x in other])
    print(s, so, s - so)


def f_2(sl):
    s = sum([len(x) for x in sl])
    other = []
    for x in sl:
        y = x.replace('"', '@"')
        y = y.replace('\\', '@@')
        other.append(y)
    so = sum([len(x) + 2 for x in other])
    print(so-s)
    

sl = readup("8.in")
f_1(sl)
f_2(sl)