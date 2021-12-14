import pprint, threading, time

pp = pprint.PrettyPrinter(indent = 2)

def readup(fn):
    d = {}
    with open(fn, 'r') as f:
        ls = f.readlines()
        start = ls[0].strip()
        for l in ls[2:]:
            f, t = l.strip().split(' -> ')
            d[f] = t
    return start, d

def step(input_string, d):
    new_string = ''
    for i in range(len(input_string)-1):
        new_string += input_string[i]
        ss = input_string[i:i+2]
        if ss in d:
            new_string += d[ss]
    new_string += input_string[-1]
    return new_string

def f_1(input_string):
    mc, lc = 0, len(input_string)
    items = set(input_string)
    for item in items:
        c = input_string.count(item)
        mc = c if c > mc else mc
        lc = c if c < lc else lc
    print(mc, lc, mc - lc)

def gen_pairs(start):
    print(start)
    pairs = {}
    for i in range(len(start)-1):
        p = start[i] + start[i+1]
        if p in pairs:
            pairs[p] += 1
        else:
            pairs[p] = 1
    return pairs

def step2(pairs, d):
    nps = {}
    for i in pairs:
        if i in d:
            np1, np2 = i[0] + d[i], d[i] + i[1]
            if np1 in nps:
                nps[np1] += pairs[i]
            else:
                nps[np1] = pairs[i]
            if np2 in nps:
                nps[np2] += pairs[i]
            else:
                nps[np2] = pairs[i]
        else:
            nps[i] = pairs[i]
    return nps


def calc(pairs, start):
    nums = {}
    for i in pairs:
        for c in i:
            if c in nums:
                nums[c] += pairs[i]
            else:
                nums[c] = pairs[i]
    for i in nums:
        if i in [start[0], start[-1]]:
            nums[i] = int(nums[i] / 2) + 1
        else:
            nums[i] = int(nums[i] / 2)
    mc, lc = max([value for key, value in nums.items()]), min([value for key, value in nums.items()])
    print(mc, lc, mc-lc)

start, d = readup('14.in')

def main2(start, d):
    pairs = gen_pairs(start)
    for i in range(40):
        pairs = step2(pairs, d)
    calc(pairs, start)


def main1(start, d):
    for i in range(10):
        start = step(start, d)
    f_1(start)

main2(start, d)
#main1(start, d)