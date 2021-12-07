import pprint
import numpy as np

pp = pprint.PrettyPrinter(indent = 2)

def readup(fn):
    with open(fn, 'r') as f:
        return np.array(sorted([int(x.strip()) for x in f.readlines()[0].split(',')]))


def align(crabs):
    to = np.median(crabs)
    fuel = sum(abs(x - to) for x in crabs)
    print(fuel)

#nope
def align2(crabs):
    result = {}
    for x in range(crabs[0], crabs[-1]+1):
        result[x] = sum([sum(range(1,abs(c - x) + 1 )) for c in crabs])
    minkey = min(result, key=result.get)
    print(minkey, result[minkey])


def align3(crabs):
    result = {}
    avg = np.average(crabs)
    possibilities = [int(avg), int(avg + 1)]
    for x in possibilities:
        result[x] = sum([sum(range(1,abs(c - x) + 1 )) for c in crabs])
    minkey = min(result, key=result.get)
    print(minkey, result[minkey])

crabs = readup('test7.in')
align(crabs)
align3(crabs)
#print('-----------------------------')
crabs = readup('7.in')
align(crabs)
align3(crabs)
