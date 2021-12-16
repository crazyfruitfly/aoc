import pprint

pp = pprint.PrettyPrinter(indent = 2)   

known = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

def readup(fn):
    result = []
    with open(fn, 'r') as f:
        for i in f.readlines():
            s = i.strip().split()
            item = {}
            item['sn'] = int(s[1][:-1])
            for a in range(0, len(s[2:]), 2):
                num = s[a+3][:-1] if s[a+3][-1] == ',' else s[a+3]
                item[s[a+2][:-1]] = int(num)
            result.append(item)
    return result

def f_1(sues):
    print(len(sues))
    for key, value in known.items(): 
        tmps = []
        for sue in sues:
            if key in sue and sue[key] != value:
                continue
            else:
                tmps.append(sue)
        sues = tmps.copy()
    print(len(sues))
    pp.pprint(sues)


def f_2(sues):
    print(len(sues))
    for key, value in known.items(): 
        tmps = []
        for sue in sues:
            if key in ['cats', 'trees']:
                if key in sue and sue[key] <= value:
                    continue
                else:
                    tmps.append(sue)
            elif key in ['pomeranians', 'goldfish']:
                if key in sue and sue[key] >= value:
                    continue
                else:
                    tmps.append(sue)
            elif key in sue and sue[key] != value:
                continue
            else:
                tmps.append(sue)
        sues = tmps.copy()
    print(len(sues))
    pp.pprint(sues)

r = readup('16.in')
f_1(r)
f_2(r)