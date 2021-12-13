import numpy as np

def readup(fn):
    octopuses = []
    with open(fn, 'r') as f:
        for l in f.readlines():
            octopuses.append([int(x) for x in l.strip()])
    return np.array(octopuses)

def increase_by_one(octopuses):
    return octopuses + 1

def flash(octopuses, flashed = []):
    flashes = 0
    for i in range(0, len(octopuses[0])):
        for j in range(0, len(octopuses)):
            neighbours = [ (i+1, j+1), (i+1, j), (i+1, j-1), (i, j+1), (i, j-1), (i-1, j+1), (i-1, j), (i-1, j-1) ]
            neighbours = [x for x in neighbours if 0 <= x[0] < 10 and 0 <= x[1] < 10]
            if octopuses[i][j] > 9 and (i, j) not in flashed:
                flashes += 1
                flashed.append((i,j))
                for coord in neighbours:
                    octopuses[coord[0]][coord[1]] += 1
    if flashes > 0:
        return flash(octopuses, flashed)
    else:
        return octopuses, flashed


def reset_flashed(octopuses, flashed):
    for coord in flashed:
        octopuses[coord[0]][coord[1]] = 0
    return octopuses


def sim(octopuses, steps=100):
    all_flashes = []
    for i in range(0, steps):
        octopuses = increase_by_one(octopuses)
        octopuses, tmp_flashed = flash(octopuses, [])
        octopuses = reset_flashed(octopuses, tmp_flashed)
        all_flashes.append(tmp_flashed)
    print(sum([len(x) for x in all_flashes]))

def sim2(octopuses):
    i = 1
    while True:
        octopuses = increase_by_one(octopuses)
        octopuses, tmp_flashed = flash(octopuses, [])
        octopuses = reset_flashed(octopuses, tmp_flashed)
        if np.all((octopuses == 0)):
            print(i)
            break
        i += 1

octopuses = readup('11.in')
sim(octopuses)
print('------------------------------------')
sim2(octopuses)
