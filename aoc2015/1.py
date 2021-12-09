def readup(fn):
    floor = 0
    with open(fn, 'r') as f:
        char = 1
        for i in f.read():
            floor += 1 if i == '(' else -1 if i == ')' else 0
            if floor < 0:
                pass
                #comment for b
                #break
            char += 1
    print(floor, char)
readup('1.in')