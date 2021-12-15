import pprint

pp = pprint.PrettyPrinter(indent = 2)

def readup(fn):
    rds = []
    with open(fn, 'r') as f:
        for i in f.readlines():
            splitted = i.strip().split()
            rdd = {'reindeer': splitted[0], 'speed': int(splitted[3]), 'sd': int(splitted[6]), 'rd': int(splitted[-2]), "dist": 0, 'points': 0}
            rds.append(rdd)
    return rds


def sim(rds, time):
    for t in range(0, time):
        for i in rds:
            if t % (i['sd'] + i['rd']) < i['sd']:
                i['dist'] += i['speed']
        lp = max(rds, key=lambda x: x['dist'])['dist']
        for i in rds:
            if i['dist'] == lp:
                i['points'] += 1
        print(lp)
    pp.pprint(rds)


rds = readup('14.in')
sim(rds, 2503)