import numpy as np

def readup(fn):
    with open(fn, 'r') as f:
        d = [list(map(int, l.strip().split('x'))) for l in f.readlines()]
    return d


def f_1(boxes):
    s = 0
    for box in boxes:
        sides = [box[0] * box[1], box[1] * box[2], box[0] * box[2]]
        s += 2* sum(sides) + min(sides)
    print(s)

def f_2(boxes):
    s = 0
    for box in boxes:
        s += 2 * sum(sorted(box)[:-1]) + np.prod(box)
    print(s)

boxes = readup('2.in')
f_1(boxes)
f_2(boxes)