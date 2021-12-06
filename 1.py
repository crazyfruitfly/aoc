def readup(fn):
    with open(fn, 'r') as f:
        l = [int(i.strip()) for i in f.readlines()]
        return l

def f_1(l):
    print([l[i-1] < l[i] for i in range(1,len(l))].count(True))

def f_2(l):
    f_1([sum(l[i: i+3]) for i in range(0, len(l)) if len(l[i: i + 4]) > 2])
    
testl = readup('test1.in')
f_1(testl)
f_2(testl)
print('----------')
l = readup('1.in')
f_1(l)
f_2(l)