
pairs = {'<': '>', '(': ')', '{': '}', '[':']'} 
points = {')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137
        }

points2 = {')': 1,
            ']': 2,
            '}': 3,
            '>': 4
        }

def check_line(line):
    counter = 0
    fifo = []
    for a in line:
        counter += 1
        if a in pairs:
            fifo.append(a)
        else:
            c = fifo.pop()
            if a != pairs[c]:
                return a, counter, fifo
    return None, None, fifo

def readup(fn):
    with open(fn, 'r') as f:
        return [l.strip() for l in f.readlines()]


def f_1(lines):
    s = 0
    for line in lines:
        a, index, fifo = check_line(line)
        if a:
            s += points[a]
    print(s)

def f_2(lines):
    ss = []
    for line in lines:
        s = 0
        a, index, fifo = check_line(line)
        if a:
            continue
        else:
            while fifo != []:
                c = fifo.pop()
                s = s*5 + points2[pairs[c]]
        ss.append(s)
    print(sorted(ss)[int((len(ss) / 2))])

lines = readup('10.in')
f_1(lines)
f_2(lines)