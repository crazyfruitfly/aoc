import pprint
import numpy as np

pp = pprint.PrettyPrinter(indent = 2)
#  1:  dddd
#  2: e    a :3
#  2: e    a :3
#  4:  ffff
#  5: g    b :6
#  5: g    b :6
#  7:  cccc
        #   0, 1, 2, 3, 4, 5, 6, 7, 8, 9
segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

uniques = lambda l: [x for x in l if l.count(x) == 1]

def find_by_length(numlist, l):
    return [x for x in numlist if len(x) == l]

def minus(a, b):
    return ''.join([x for x in a if x not in b])

def get_numbers(numlist):
    return set([a for x in numlist for a in x])

def set_segment(segment, value, segments):
    for i in segments:
        if i in segment:
            nv = ''.join([v for v in value if v in segments[i]])
            segments[i] = nv
        else:
            for v in value:
                segments[i] = segments[i].replace(v, '')

def init_segments(numlist):
    segments = {1:'abcdefg', 2:'abcdefg', 3:'abcdefg', 4:'abcdefg', 5:'abcdefg', 6:'abcdefg', 7:'abcdefg'}
    numbers = {'0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None,}    
    numbers['1'] = find_by_length(numlist, 2)[0]
    numbers['4'] = find_by_length(numlist, 4)[0]
    numbers['7'] = find_by_length(numlist, 3)[0]
    numbers['8'] = find_by_length(numlist, 7)[0]
    
    s1 = minus(numbers['7'], numbers['1'])
    s24 = minus(numbers['4'], numbers['1'])
    s235 = find_by_length(numlist, 5)

    set_segment([1], s1, segments)
    set_segment([3, 6], numbers['1'], segments)
    set_segment([3, 6], numbers['1'], segments)
    set_segment([2, 4], s24, segments)

    for i in s235:
        p = minus(i, numbers['1'])
        if len(p) == 3:
            numbers['3'] = i
            set_segment([1,4,7], p, segments)

    for i in s235:
        s = minus(i, numbers['3'])
        if s == segments[5]:
            numbers['2'] = i
            set_segment([6], minus(segments[3], i), segments)
        elif s == segments[2]:
            numbers['5'] = i
            #set_segment([3], minus(segments[6], i), segments)

    numbers['0'] = minus(numbers['8'], segments[4])
    numbers['6'] = minus(numbers['8'], segments[3])
    numbers['9'] = minus(numbers['8'], segments[5])

    #print(segments)
    return numbers

def calc_number(digits, items):
    num = ''
    #print(digits)
    #print(items)
    for i in items:
        for key, value in digits.items():
            if set(i) == set(value):
                num += key
                break
    return int(num)

def readup(fn):
    with open(fn, 'r') as f:
        return [ (x.split('|')[0].split(), x.split('|')[1].split()) for x in f.readlines()]

def f_1(digits):
    u = uniques(segments)
    print([len(d) in u for l in digits for d in l[1]].count(True))

def f_2(digits):
    num = 0
    for i in digits:
        numbers = init_segments(i[0])
        num += calc_number(numbers, i[1])
    print(num)

digits = readup('8.in')
#pp.pprint(digits)
f_2(digits)

