import pprint
import numpy as np

pp = pprint.PrettyPrinter(indent = 2)

def readup(fn):
    with open(fn, 'r') as f:
        return [int(x.strip()) for x in f.readlines()[0].split(',')]

#nope
def sim(lfs, days = 256):
    #print('days: ', 80-days, lfs)
    print(days)
    if days == 0:
        return len(lfs)
    else:
        lfs = [x-1 for x in lfs]
        lfs.extend([8]*lfs.count(-1))
        return sim([x if x != -1 else 6 for x in lfs], days-1)


def sim2(lfs, days = 256):
    status = [0]*9
    for i in range(0,9):
        status[i] = lfs.count(i)

    for day in range(0, days):
        new_spawns = status[0]
        for i in range(1,9):
            status[i-1] = status[i]
        status[6] += new_spawns
        status[8] = new_spawns

    print(sum(status))

        

lfs = readup('test6.in')
sim2(lfs, 80)
sim2(lfs, 256)
print('-----------------------------------------')
lfs = readup('6.in')
sim2(lfs, 80)
sim2(lfs, 256)